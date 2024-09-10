from flume.analytics.segment_client import SegmentClient


class FlumeAnalytics(SegmentClient):
    def __init__(self, base_url: str, environment: str = "test"):
        super().__init__(base_url, environment)
