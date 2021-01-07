import requests
import bs4
from bs4 import BeautifulSoup as BS


from german_cities import *
from city_url import *
from page_numb import *
from restaurants import *
from ads import *

# 1.Get response with all germans cities
german_cities = get_german_cities()

# 2.Save cities to MongoDB

# 3.Go through all cities and get city URL by TripAdvisor
cities_url_list = get_url_by_cities(german_cities)


for city in cities_url_list:
    page = requests.get('https://www.tripadvisor.de' + city["city_url_ta"])

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        last_numb = get_last_numb_on_page(soup)
        restaurants = get_restaurants_content(soup)
        restaurants = remove_ads_restaurants(restaurants)

# 4.Save them to MongoDB
# 5. Get info from restaurant
