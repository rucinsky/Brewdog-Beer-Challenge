import requests

def get_test(endpoint:str):
    assert requests.get(endpoint), f"Couldn't get data from {endpoint}, status: {requests.get(endpoint)}"