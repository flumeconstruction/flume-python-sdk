import requests
from typing import Optional, Union, Dict
from datetime import datetime

class SegmentClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def identify(self, 
                 user_id: Union[str, int], 
                 traits: Optional[Dict] = None, 
                 context: Optional[Dict] = None, 
                 timestamp: Optional[datetime] = None, 
                 anonymous_id: Optional[Union[str, int]] = None, 
                 integrations: Optional[Dict] = None):
        url = f"{self.base_url}/identify/"
        payload = {
            "user_id": user_id,
            "traits": traits if traits is not None else {},
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat() 
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        print(f"Payload sent: {payload}")        
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
        payload = {
            "user_id": user_id,
            "event": event,
            "properties": properties if properties is not None else {},
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        print(f"Payload sent: {payload}")        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def page(self, 
             user_id: Union[str, int],
             category: Optional[str] = None,
             name: Optional[str] = None,
             properties: Optional[Dict] = None,
             context: Optional[Dict] = None,
             timestamp: Optional[datetime] = None,
             anonymous_id: Optional[Union[str, int]] = None,
             integrations: Optional[Dict] = None):
        url = f"{self.base_url}/page/"
        payload = {
            "user_id": user_id,
            "category": category,
            "name": name,
            "properties": properties if properties is not None else {},
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        print(f"Payload sent: {payload}")        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def screen(self, 
               user_id: Union[str, int, float], 
               category: Optional[str] = None,
               name: Optional[str] = None,
               properties: Optional[Dict] = None,
               context: Optional[Dict] = None,
               timestamp: Optional[datetime] = None,
               anonymous_id: Optional[Union[str, int]] = None,
               integrations: Optional[Dict] = None):
        url = f"{self.base_url}/screen/"
        payload = {
            "user_id": user_id,
            "category": category,
            "name": name,
            "properties": properties if properties is not None else {},
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        print(f"Payload sent: {payload}")        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def group(self, 
              user_id: Union[str, int, float], 
              group_id: Union[str, int, float], 
              traits: Optional[Dict] = None, 
              context: Optional[Dict] = None, 
              timestamp: Optional[datetime] = None,
              anonymous_id: Optional[Union[str, int]] = None, 
              integrations: Optional[Dict] = None):
        url = f"{self.base_url}/group/"
        payload = {
            "user_id": user_id,
            "group_id": group_id,
            "traits": traits if traits is not None else {},
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        if anonymous_id is not None:
            payload["anonymous_id"] = anonymous_id
        print(f"Payload sent: {payload}")        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def alias(self, 
              previous_id: str, 
              user_id: str, 
              context: Optional[Dict] = None, 
              timestamp: Optional[datetime] = None, 
              integrations: Optional[Dict] = None):
        url = f"{self.base_url}/alias/"
        payload = {
            "previous_id": previous_id,
            "user_id": user_id,
            "context": context if context is not None else {},
            "integrations": integrations if integrations is not None else {},
        }
        if timestamp is not None:
            payload["timestamp"] = timestamp.isoformat()
        print(f"Payload sent: {payload}")

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def flush(self):
        url = f"{self.base_url}/flush/"
        
        response = requests.post(url)
        response.raise_for_status()
        return response.json()
