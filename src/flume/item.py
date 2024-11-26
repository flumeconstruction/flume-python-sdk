import httpx
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class SearchItemData(BaseModel):
    item_name: str
    item_description: str
    delivery_location: str
    quantity: int
    delivery_date: str
    other: Optional[str] = None
    item_image_url: Optional[str] = None


class Item(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    item_id: str
    customer_id: str
    item_data: SearchItemData
    item_phase: str
    created_at: str
    updated_at: str


class CreateItemPayload(BaseModel):
    customer_id: str
    project_id: str
    item_data: SearchItemData


class ItemService:
    def __init__(self, base_url):
        self.url = f"{base_url}/item"

    def retrieve(self, item_id) -> Item:
        with httpx.Client(timeout=30) as client:
            response = client.get(f"{self.url}/get/{item_id}")
            if response.status_code == 200:
                return Item(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting item")

    def retrieve_items_by_customer_id(self, customer_id) -> List[Item]:
        with httpx.Client(timeout=30) as client:
            response = client.get(f"{self.url}/get_all/{customer_id}")
            if response.status_code == 200:
                return [Item(**item) for item in response.json()]
            else:
                response.raise_for_status()
                raise Exception("Error getting items by customer id")


class AsyncItemService:
    def __init__(self, base_url):
        self.url = f"{base_url}/item"

    async def retrieve(self, item_id) -> Item:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get/{item_id}")
            if response.status_code == 200:
                return Item(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting item")

    async def create(self, item: CreateItemPayload) -> Item:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(f"{self.url}/create", json=item.model_dump())
            if response.status_code == 200:
                return Item(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error creating item")

    async def retrieve_items_by_customer_id(self, customer_id) -> List[Item]:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get_all/{customer_id}")
            if response.status_code == 200:
                return [Item(**item) for item in response.json()]
            else:
                response.raise_for_status()
                raise Exception("Error getting items by customer id")
