import requests
import bs4
from bs4 import BeautifulSoup
import json



def get_alphabet():
    URL = 'https://www.deutsche-staedte.de/staedte.php?city=A'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    alphabet = soup.find(style="text-align:center; margin-top:12px; margin-bottom:12px;")
    alphabet_list = []
    for elem in alphabet:
        if type(elem) is bs4.element.Tag:
            character = str(elem.contents[0])
            alphabet_list.append(character.strip("\r\n"))

    return alphabet_list


def remove_spaces(string):
    string = string.strip()
    return string


def get_german_cities():
    try:
        file = json.load(open("german_cities.json"))
        return file
    except IOError:
        print("File not accessible")
        print("Parsing https://www.deutsche-staedte.de ...")

        german_cities = get_all_cities()
        save(german_cities)

        return german_cities


def save(german_cities):
    json.dump(german_cities, open("german_cities.json", 'w'))


def get_all_cities():
    alphabet = get_alphabet()
    cities_list = []
    for character in alphabet:
        url = 'https://www.deutsche-staedte.de/staedte.php?city=' + character
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        cities_tags = soup.find_all('li', style="padding-bottom:6px;")

        for city_tag in cities_tags:
            city = city_tag.contents[0].contents[0]

            plz = city_tag.contents[2].contents[0]
            plz = remove_spaces(plz)

            city = {
                "city": str(city),
                "plz": plz
            }

            cities_list.append(city)

    return cities_list
