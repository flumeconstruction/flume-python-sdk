import httpx
from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    email: str
    phone: str


class Address(BaseModel):
    streetAddress: str
    cityArea: str
    stateProvince: str
    zipPostalCode: str
    countryRegion: str
    text: str


class Customer(BaseModel):
    customer_id: str
    company_name: str
    address: Address
    website: str
    contact: Contact
    annual_procurement_value: int
    is_active: bool = True
    created_at: str
    updated_at: str


class CustomerService:
    def __init__(self, base_url):
        self.url = f"{base_url}/customer"

    def retrieve(self, customer_id) -> Customer:
        with httpx.Client(timeout=30) as client:
            response = client.get(f"{self.url}/get/{customer_id}")
            if response.status_code == 200:
                return Customer(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting customer")


class AsyncCustomerService:
    def __init__(self, base_url):
        self.url = f"{base_url}/customer"

    async def retrieve(self, customer_id) -> Customer:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(f"{self.url}/get/{customer_id}")
            if response.status_code == 200:
                return Customer(**response.json())
            else:
                response.raise_for_status()
                raise Exception("Error getting customer")
