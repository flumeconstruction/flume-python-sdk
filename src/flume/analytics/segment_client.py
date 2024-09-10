import requests
from typing import Optional, Union, Dict, Any
from datetime import datetime


class SegmentClient:
    def __init__(self, base_url: str, environment: str):
        self.base_url = base_url
        self.environment = environment

    def _serialize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Convert datetime objects to ISO format strings in the payload."""
        for key, value in payload.items():
            if isinstance(value, datetime):
                payload[key] = value.isoformat()
            elif isinstance(value, dict):
                payload[key] = self._serialize_payload(value)
        return payload

    def identify(self,
                 user_id: Union[str, int],
                 traits: Optional[Dict] = None,
                 context: Optional[Dict] = None,
                 timestamp: Optional[datetime] = None,
                 anonymous_id: Optional[Union[str, int]] = None,
                 integrations: Optional[Dict] = None):
        url = f"{self.base_url}/identify/"

        # Add environment to context
        if context is None:
            context = {}
        context['environment'] = self.environment

        payload = {
            "user_id": user_id,
            "traits": traits if traits is not None else {},
            "context": context,
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        payload = self._serialize_payload(payload)
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def track_event(self,
                    user_id: Union[str, int],
                    event: str,
                    properties: Optional[Dict] = None,
                    context: Optional[Dict] = None,
                    timestamp: Optional[datetime] = None,
                    anonymous_id: Optional[Union[str, int]] = None,
                    integrations: Optional[Dict] = None):
        url = f"{self.base_url}/track_event/"

        # Add environment to context
        if context is None:
            context = {}
        context['environment'] = self.environment

        payload = {
            "user_id": user_id,
            "event": event,
            "properties": properties if properties is not None else {},
            "context": context,
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        payload = self._serialize_payload(payload)
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
