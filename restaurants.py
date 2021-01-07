import json
import re

def get_restaurants_content(soup):
    script = soup.find("script", text=re.compile('window.__WEB_CONTEXT__'))
    json_str = script.contents[0].strip()  # Remove spaces at the beginning and at the end of the string:
    json_str = json_str.split(':{"data":{"restaurants":')[1].strip()  # Start of string
    json_str = json_str.split('}]},"error":')[0].strip()  # End of string
    json_str = json_str + '}]'

    return json.loads(json_str)

