from datetime import datetime
from typing import Any, Dict, List, Optional
import httpx
from pydantic import BaseModel


class Image(BaseModel):
    id: str
    url: str
    ai_description: Optional[Dict[str, Any]] = None


class BaseAttribute(BaseModel):
    id: str
    label: str
    value: Any


class LogisticalAttribute(BaseAttribute):
    carton_weight: Optional[float]
    carton_length: Optional[float]
    carton_width: Optional[float]
    carton_height: Optional[float]
    sqft_per_carton: Optional[float]
    total_cartons: Optional[int]
    carton_per_pallet: Optional[int]
    pass


class Product(BaseModel):
    master_product_id: str
    product_id: str
    supplier_id: str
    name: str  # MasterProdName + [Variation Option Values]
    hero_image: Image
    hts_code: str
    pricing: str
    product_type: Optional[str]
    variation: Optional[Dict[str, str]] = {}
    images: Optional[List[Image]] = []
    additional_attributes: Optional[dict] = {}
    logistical_data: Optional[List[LogisticalAttribute]] = []
    created_at: datetime
    updated_at: datetime
    is_active: Optional[bool]
    is_reviewed: Optional[bool]


class ProductService:
    def __init__(self, base_url):
        self.url = f"{base_url}/master_product"

    def retrieve(self, product_id) -> Product:
        with httpx.Client(timeout=30) as client:
            response = client.get(f"{self.url}/get_product/{product_id}")
            if response.status_code == 200:
                return Product(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting Product")


class AsyncProductService:
    def __init__(self, base_url):
        self.url = f"{base_url}/master_product"

    async def retrieve(self, product_id) -> Product:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get_product/{product_id}")
            if response.status_code == 200:
                return Product(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting Product")
