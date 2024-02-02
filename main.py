from src.scraper import WikipediaScraper

if __name__ == "__main__":
    """Created Object of WikipediaScraper class and called its method
    according to the functionality selected when the projrct is 
    executed"""    
    WikipediaScraper_object = WikipediaScraper("https://country-leaders.onrender.com")
    input_indicator = WikipediaScraper_object.fuctionality_input()
    if input_indicator == 1:
        WikipediaScraper_object.check_url_status()
    elif input_indicator == 2:
        countries_list = WikipediaScraper_object.get_countries()
        print(countries_list)
    elif input_indicator == 3:
        leaders_list = WikipediaScraper_object.get_leaders()
        print(leaders_list)
    elif input_indicator == 4:
        WikipediaScraper_object.to_json_file()
    elif input_indicator == 5:
        WikipediaScraper_object.export_json_file()
    elif input_indicator == 6:
        WikipediaScraper_object.to_csv_file() 
    elif input_indicator == 7:
        exit()
    else:
        print("Invalid Number Entered!!!")
