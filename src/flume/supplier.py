import requests


class SupplierService:
    def __init__(self, base_url):
        self.url = f"{base_url}/suppliers"

    def get(self, supplier_id):
        response = requests.get(f"{self.url}/get/{supplier_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
