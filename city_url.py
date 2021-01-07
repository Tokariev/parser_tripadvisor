import requests
import json
from pathlib import Path


def get_url_by_cities(german_cities):
    if Path("german_cities_url.json").is_file():
        print("File exist")
        return json.load(open("german_cities_url.json"))
    else:
        global city_dict
        # 3.1 Get cookies
        session = requests.Session()
        URL = 'https://www.tripadvisor.de/'
        session.get(URL)
        search_body = json.load(open("search_body.json"))

        list_to_save = []

        total = len(german_cities)
        iteration = 0
        for city in german_cities:
            iteration = iteration + 1
            print(iteration, 'from', total)

            # 3.2 Set city to POST request
            search_body[0]['variables']['request']['query'] = city["city"]
            response = session.post("https://www.tripadvisor.de/data/graphql/batched", json=search_body)

            content_json = json.loads(response.content)

            # 3.3 Check if something was found
            if 'details' not in content_json[0]['data']['Typeahead_autocomplete']['results'][0]:
                continue

            # 3.3 Check if same city was found in TripAdvisor
            if 'results' in content_json[0]['data']['Typeahead_autocomplete']:
                for city_obj in content_json[0]['data']['Typeahead_autocomplete']['results']:
                    if 'details' in city_obj:
                        if city_obj['details']['localizedName'] == city["city"]:
                            # Check if city is in germany
                            if 'Deutschland' in city_obj['details']['localizedAdditionalNames']['longOnlyHierarchy']:
                                # Same city that we search
                                RESTAURANTS_URL = city_obj['details']['RESTAURANTS_URL']

                                city_dict = {"city": city["city"],
                                             "plz": city["plz"],
                                             "city_ta": city_obj['details']['localizedName'],
                                             "city_url_ta": RESTAURANTS_URL}

                                list_to_save.append(city_dict)

        json.dump(list_to_save, open("german_cities_url.json", 'w'))

        return json.load(list_to_save)
