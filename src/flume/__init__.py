from analytics.client import SegmentClient


class FlumeAnalytics(SegmentClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)
