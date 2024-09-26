import requests


class QuoteService:
    def __init__(self, base_url):
        self.url = f"{base_url}/quote"

    def get(self, quote_id):
        response = requests.get(f"{self.url}/get/{quote_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_quotes_by_item_id(self, item_id):
        response = requests.get(f"{self.url}/get_all_by_item_id/{item_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
