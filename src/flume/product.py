from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import httpx
from pydantic import BaseModel


class SizeVariation(BaseModel):
    height: float | None
    width: float | None


class Image(BaseModel):
    id: str
    url: str
    is_external: Optional[bool] = False


class Document(BaseModel):
    id: str
    url: str


class ProductCategories(str, Enum):
    tile = "tile"
    granite = "granite"
    marble = "marble"
    ceramic = "ceramic"
    stones = "stones"


class PricingUnit(str, Enum):
    sqft = 'sqft'
    piece = 'piece'
    kg = 'kg'
    m2 = 'm2'


class Currency(str, Enum):
    USD = "USD"
    INR = "INR"
    EUR = "EUR"
    GBP = "GBP"
    CAD = "CAD"
    AUD = "AUD"


class PriceRange(BaseModel):
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    pricing_unit: PricingUnit
    currency: Currency


class Product(BaseModel):
    collection_id: str
    product_id: str
    supplier_id: str
    product_name: str
    variation: Dict[str, str | SizeVariation]
    main_image: Image
    images: Optional[List[Image]]
    price_range: PriceRange
    description: Optional[str] = None
    additional_attributes: Optional[dict]
    is_active: Optional[bool] = True
    is_best_seller: Optional[bool] = True
    is_reviewed: Optional[bool] = True
    created_at: datetime
    updated_at: datetime


class ProductCollection(BaseModel):
    collection_id: str
    collection_name: str
    collection_description: str
    collection_category: ProductCategories
    main_image: Image
    images: List[Image]
    specifications: Dict[str, str]
    supplier_id: str
    variations: Dict[str, List[str | SizeVariation]]
    files: List[Document]
    price_range: PriceRange
    is_active: Optional[bool] = True
    is_best_seller: Optional[bool] = True
    is_reviewed: Optional[bool] = True
    created_at: datetime
    updated_at: datetime


class ProductCollectionWithProducts(ProductCollection):
    products: List[Product]

class GetManyProductsPayload(BaseModel):
    product_ids: List[str]


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

    async def retrieve_product(self, product_id) -> Product:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get_product/{product_id}")
            if response.status_code == 200:
                return Product(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting Product")

    async def retrieve_many_products(self, payload: GetManyProductsPayload) -> List[Product]:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(f"{self.url}/get_many_products", json=payload.model_dump())
            if response.status_code == 200:
                return [Product(**product) for product in response.json()]
            else:
                response.raise_for_status()
                raise Exception("Error getting Products")

    async def retrieve_product_collection(self, collection_id) -> ProductCollection:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get/{collection_id}")
            if response.status_code == 200:
                return ProductCollectionWithProducts(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting Product Collection")
