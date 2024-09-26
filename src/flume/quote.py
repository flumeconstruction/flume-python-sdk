import requests
from typing import Optional, List
from pydantic import BaseModel


class SupplierData(BaseModel):
    supplier_id: Optional[str] = None


class SizeSchema(BaseModel):
    length_in_inches: Optional[float] = None
    width_in_inches: Optional[float] = None
    height_in_inches: Optional[float] = None


class OrderCalculationData(BaseModel):
    unit_price_in_dollars: Optional[float] = None
    lead_time_in_days: Optional[int] = None
    quantity: Optional[int] = None
    size: Optional[SizeSchema] = None
    weight_in_grams: Optional[float] = None
    hts_code: Optional[str] = None
    origin: Optional[str] = None
    destination: Optional[str] = None


class CostBreakdownSchema(BaseModel):
    base_price: Optional[float] = None
    shipping_cost: Optional[float] = None
    tariffs: Optional[float] = None
    insurance: Optional[float] = None
    total_cost: Optional[float] = None


class Container(BaseModel):
    container_type: Optional[str] = None
    cubic_meters: Optional[float] = None
    weight_in_kg: Optional[float] = None


class OrderFulfillmentData(BaseModel):
    per_unit_price: Optional[float] = None
    containers: Optional[List[Container]] = None
    cost_breakdown: Optional[CostBreakdownSchema] = None


class Quote(BaseModel):
    quote_id: Optional[str] = None
    customer_id: Optional[str] = None
    search_item_id: Optional[str] = None
    product_id: Optional[str] = None
    supplier_data: Optional[SupplierData] = None
    order_calculation_data: Optional[OrderCalculationData] = None
    order_fulfillment_data: Optional[OrderFulfillmentData] = None
    quote_state: Optional[str] = None
    is_active: Optional[bool] = None
    quote_pdf_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class QuoteService:
    def __init__(self, base_url):
        self.url = f"{base_url}/quote"

    def retrieve(self, quote_id) -> Quote:
        response = requests.get(f"{self.url}/get/{quote_id}")
        if response.status_code == 200:
            return Quote(**response.json())
        else:
            response.raise_for_status()
            raise Exception("Error getting quote")

    def retrieve_quotes_by_item_id(self, item_id) -> List[Quote]:
        response = requests.get(f"{self.url}/get_all_by_item_id/{item_id}")
        if response.status_code == 200:
            return [Quote(**quote) for quote in response.json()]
        else:
            response.raise_for_status()
            raise Exception("Error getting quotes by item id")
