from flume.analytics.segment_client import SegmentClient
from flume.product import AsyncProductService, ProductService
from flume.supplier import SupplierService, AsyncSupplierService
from flume.quote import QuoteService, AsyncQuoteService
from flume.item import ItemService, AsyncItemService
from flume.customer import CustomerService, AsyncCustomerService
from flume.auth import FirebaseAuth


class FlumeAnalytics(SegmentClient):
    def __init__(self, base_url: str, environment: str = "test"):
        super().__init__(base_url, environment)


class Flume:
    def __init__(self, environment: str = "test", service_account_info=None):
        self.supplier = SupplierService(
            "https://supplier-service-85865196271.us-central1.run.app")
        self.quote = QuoteService(
            "https://item-quote-service-85865196271.us-central1.run.app")
        self.item = ItemService(
            "https://item-quote-service-85865196271.us-central1.run.app")
        self.customer = CustomerService(
            "https://customer-service-85865196271.us-central1.run.app")
        self.product = ProductService(
            "https://product-service-hv5ml7mvya-uc.a.run.app")
        if service_account_info is not None:
            self.auth = FirebaseAuth(service_account_info)


class AsyncFlume:
    def __init__(self, environment: str = "test", service_account_info=None):
        self.supplier = AsyncSupplierService(
            "https://supplier-service-85865196271.us-central1.run.app")
        self.quote = AsyncQuoteService(
            "https://item-quote-service-85865196271.us-central1.run.app")
        self.item = AsyncItemService(
            "https://item-quote-service-85865196271.us-central1.run.app")
        self.customer = AsyncCustomerService(
            "https://customer-service-85865196271.us-central1.run.app")
        self.product = AsyncProductService(
            "https://product-service-hv5ml7mvya-uc.a.run.app")
        if service_account_info is not None:
            self.auth = FirebaseAuth(service_account_info)
