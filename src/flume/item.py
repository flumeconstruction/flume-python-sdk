import requests
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class SearchItemData(BaseModel):
    item_name: str
    item_description: str
    delivery_location: str
    quantity: int
    delivery_date: str
    other: Optional[str] = None


class Item(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    item_id: str
    customer_id: str
    item_data: SearchItemData
    item_phase: str
    created_at: str
    updated_at: str


class ItemService:
    def __init__(self, base_url):
        self.url = f"{base_url}/item"

    def retrieve(self, item_id) -> Item:
        response = requests.get(f"{self.url}/get/{item_id}")
        if response.status_code == 200:
            return Item(**response.json())
        else:
            response.raise_for_status()
            raise Exception("Error getting item")

    def retrieve_items_by_customer_id(self, customer_id) -> List[Item]:
        response = requests.get(f"{self.url}/get_all/{customer_id}")
        if response.status_code == 200:
            return [Item(**item) for item in response.json()]
        else:
            response.raise_for_status()
            raise Exception("Error getting items by customer id")
