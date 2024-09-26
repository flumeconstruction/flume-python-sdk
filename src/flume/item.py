import requests


class ItemService:
    def __init__(self, base_url):
        self.url = f"{base_url}/item"

    def get_item(self, item_id):
        response = requests.get(f"{self.url}/get/{item_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_items_by_customer_id(self, customer_id):
        response = requests.get(f"{self.url}/get_all/{customer_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
