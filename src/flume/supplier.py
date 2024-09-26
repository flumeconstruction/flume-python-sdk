import httpx
from typing import Optional, List
from pydantic import BaseModel


class Address(BaseModel):
    streetAddress: Optional[str] = None
    cityArea: Optional[str] = None
    stateProvince: Optional[str] = None
    zipPostalCode: Optional[str] = None
    countryRegion: Optional[str] = None
    text: Optional[str] = None

    def flatten(self) -> Optional[str]:
        if self.text:
            return self.text

        address_parts = [
            self.streetAddress,
            self.cityArea,
            self.zipPostalCode,
            self.stateProvince,
            self.countryRegion
        ]

        flattened_address = ', '.join(part for part in address_parts if part)
        if flattened_address == "":
            return None
        else:
            return flattened_address


class ContactDetails(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    priority: Optional[int] = -1


class Supplier(BaseModel):
    supplier_id: Optional[str] = None
    name: Optional[str] = None
    website: Optional[str] = None
    address: Optional[Address] = None
    description: Optional[str] = None
    contact_details: Optional[List[ContactDetails]] = None
    profile_status: Optional[str] = None
    data_status: Optional[str] = None
    trust_score: Optional[float] = None
    additional_attributes: Optional[dict] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class SupplierService:
    def __init__(self, base_url):
        self.url = f"{base_url}/suppliers"

    def retrieve(self, supplier_id) -> Supplier:
        with httpx.Client(timeout=30) as client:
            response = client.get(f"{self.url}/get/{supplier_id}")
            if response.status_code == 200:
                return Supplier(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting supplier")


class AsyncSupplierService:
    def __init__(self, base_url):
        self.url = f"{base_url}/suppliers"

    async def retrieve(self, supplier_id) -> Supplier:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get/{supplier_id}")
            if response.status_code == 200:
                return Supplier(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting supplier")
