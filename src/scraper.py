import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
import re
import pandas as pd

class WikipediaScraper:
    """
        Class allows to structurally retrieving data from the API. It 
        checks the status of base URL (https://country-leaders.onrender.com),
        request cookie then access countries endpoint to fetch the list of 
        countries. Then for each of country fetch the details of leaders. 
        It then picks the Wiki URL from the leader's details and fetches 
        little information from Wikipedia page. Create a json or CSV file 
        from all the details.
    """
    def __init__(self,base_url):
        self.base_url = base_url
        self.cookies_endpoint = "/cookie"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.leaders_data = []
    
    def check_url_status(self):
        """Check if the URL is up and running by checking its status"""
        self.status_url = "status" 
        self.response = requests.get(f"{self.base_url}/{self.status_url}")
        self.request_status = self.response.status_code

        if self.request_status == 200:
            print("Everything went okay, and the result has been returned (if any)")
            print(self.response.text)
        else:
            print(f"The request failed with error code: {self.request_status}")
    
    def refresh_cookie(self):
        """Refresh the cookies using endpoint /cookie"""
        self.cookie_response = requests.get(f"{self.base_url}{self.cookies_endpoint}")
        self.cookies = self.cookie_response.cookies
        return self.cookies

    def get_countries(self):
        """Gets the list of countries using /countries endpoint"""
        self.countries_url = self.base_url + self.country_endpoint
        self.cookies = self.refresh_cookie()
        self.countries_response = requests.get(self.countries_url, cookies=self.cookies)
        return(self.countries_response.json())
    
    def get_leaders(self):
        """Get leaders information from /leaders endpoint for all the countries"""
        #self.cookies = self.refresh_cookie()
        leader_details = []
        country_list = self.get_countries()
        for countries in country_list:
            params={'country' : countries }
            leader_response = requests.get(f"{self.base_url}{self.leaders_endpoint}", cookies=self.refresh_cookie(),params=params)
            leader_details.append({"Country" : countries,"Leader_details" : leader_response.text})
        return(leader_details)
    
    def get_first_paragraph(self):
        """For all the leaders get the first Paragraph of their wikipedia Page"""
        leader_details = self.get_leaders()
        for leaders in leader_details:
            leader_country = leaders["Country"]
            leader_dict = json.loads(leaders["Leader_details"])
            self.leader_info = []
            for leader in leader_dict:
                leader_info_merge = {}
                wiki_url = leader["wikipedia_url"] 
                leader_fullname = leader["first_name"] +"-"+ leader["last_name"]
                wiki_content = requests.get(wiki_url).content
                soup = BeautifulSoup(wiki_content, "html.parser")
                first_paragraph = ''
                for tag in soup.find_all("p"):
                    if re.search(r"^<p><b>.*</b>",str(tag)):
                        first_paragraph = tag.get_text()
                        break                
                leader_info_merge = leader
                leader_info_merge["Wiki_First_Paragraph"] = first_paragraph
                self.leader_info.append({leader_fullname : leader_info_merge})
            self.leaders_data.append({leader_country :  self.leader_info})
        return(self.leaders_data)
    

    def to_json_file(self):
        """Creates a json file with all the leaders information along with the first paragraph of their Wikipedia Page"""
        self.get_first_paragraph()
        with open("leaders_data.json", "w") as outfile: 
            json.dump(self.leaders_data, outfile)

        outfile.close()                
    
    def export_json_file(self):
        """Exports the json file and show the results on the screen"""
        self.to_json_file()
        file_data = open('leaders_data.json')
        data = json.load(file_data)
        for i in data:
            pprint(i)
        file_data.close()

    def to_csv_file(self):
        """Creates a CSV file with all the leaders information along with the first paragraph of their Wikipedia Page"""
        self.to_json_file()
        with open('leaders_data.json') as json_file:
            json_data = json.load(json_file)

        df = pd.json_normalize(json_data)
        df.to_csv('leaders_data.csv', mode='w')
        json_file.close()
        
        
    def fuctionality_input(self):
        """Display information on the screen when the project is executed"""
        print("Input Options:")
        print("1. Check the status of base URL.")
        print("2. Get the list of countries.")
        print("3. Get the complete list of Leaders for each country.")
        print("4. Create a json file with details of all the leaders and short description about them.")
        print("5. Export the json file and print the result on Screen.")
        print("6. Get the result in CSV.")
        print("7. Exit")
        input_indicator = int(input("Enter the Number with respect to functionally you want to execute: "))
        return input_indicator
        
        