from src.scraper import WikipediaScraper


if __name__ == "__main__":
    WikipediaScraper_object = WikipediaScraper("https://country-leaders.onrender.com")
    WikipediaScraper_object.check_url_status()

    countries_list = WikipediaScraper_object.get_countries()
    print(countries_list)

    leaders_list = WikipediaScraper_object.get_leaders()
    #print(leaders_list)

    first_paragraph = WikipediaScraper_object.get_first_paragraph()
    print(first_paragraph)
