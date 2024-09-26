from flume.analytics.segment_client import SegmentClient
from flume.supplier import SupplierService
from flume.quote import QuoteService
from flume.item import ItemService


class FlumeAnalytics(SegmentClient):
    def __init__(self, base_url: str, environment: str = "test"):
        super().__init__(base_url, environment)


class Flume:
    def __init__(self, environment: str = "test"):
        self.supplier = SupplierService(
            "https://supplier-service-85865196271.us-central1.run.app")
        self.quote = QuoteService(
            "https://item-quote-service-85865196271.us-central1.run.app")
        self.item = ItemService(
            "https://item-quote-service-85865196271.us-central1.run.app")
