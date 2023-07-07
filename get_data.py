import requests
import json

from tests.get_test import get_test
def get_data()->list:
    date = "12-2015"
    endpoint = f"https://api.punkapi.com/v2/beers?brewed_after={date}"
    get_test(endpoint) #testing if endpoint is accessible
    beer_data = requests.get(endpoint).json()
    print(beer_data)

    return beer_data
