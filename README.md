**Wikipedia Scraper**

**Description**

This is a scraper that builds a JSON file with the political leaders of each country you get from an API ("https://country-leaders.onrender.com") 
It checks the status of base URL.
Request cookie then access countries endpoint to fetch the list of countries. 
For each of country fetch the details of leaders. 
 It picks the Wiki URL from the leader's details and fetches first Paragraph from Wikipedia page. 
Create a json file from all the details.

**Installation**

Go to the directory where you want the cloned directory and execute the below command in Terminal.
git clone https://github.com/MahakBehl/Wikipedia_Scraper
Install requirements.txt

**Usage**

To execute project excute the below command:
python main.py
This will give you a list of features those can be executed. Below is the screenshot for the same.

![image](https://github.com/MahakBehl/Wikipedia_Scraper/assets/156779788/de5f7c2e-1492-4c18-a498-2a83ec3c58b9)

 
As output you can get:
1)	Status of the Base URL.
2)	List of countries fetched from countries endpoint.
3)	Details of Leaders with respect to each country listed above.
4)	A json file with detailed information of all the leader with respect to each country along with the first paragraph from Wikipedia.
5)	Get the result of json file on the screen.
6)	A CSV file with detailed information of all the leader with respect to each country along with the first paragraph from Wikipedia.
7)	To exit the project.

**Technologies Used:** Python 
**Contact Details** : mahakbehl@gmail.com
Created on 2nd Feb 2024
By Mahak Behl

