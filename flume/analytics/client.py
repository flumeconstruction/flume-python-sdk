import requests
from typing import Optional, Union, Dict
from datetime import datetime

class SegmentClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def _get_headers(self):
        return {
            "Content-Type": "application/json",
            "x-api-key": self.api_key  # Add the API key to the headers
        }

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
            "traits": traits,
            "context": context,
            "timestamp": timestamp,
            "anonynmous_id": anonymous_id,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def track(self, 
              user_id: str, 
              event: str, 
              properties: Optional[Dict] = None, 
              context: Optional[Dict] = None, 
              timestamp: Optional[datetime] = None,
              anonymous_id: Optional[Union[str,int]] = None, 
              integrations: Optional[Dict] = None):
        url = f"{self.base_url}/track/"
        payload = {
            "user_id": user_id,
            "event": event,
            "properties": properties,
            "context": context,
            "timestamp": timestamp,
            "anonymous_id": anonymous_id,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    
    def page(self, 
             user_id: str,
             category: Optional[str] = None,
             name: Optional[str] = None,
             properties: Optional[dict] = None,
             context: Optional[dict] = None,
             timestamp: Optional[datetime] = None,
             anonymous_id: Optional[Union[str,int]] = None,
             integrations: Optional[dict] = None):
        url = f"{self.base_url}/page/"
        payload = {
            "user_id": user_id,
            "category": category,
            "name": name,
            "properties": properties,
            "context": context,
            "timestamp": timestamp,
            "anonymous_id": anonymous_id,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    
    def screen(self, 
               user_id: Union[str, int, float], 
               category: Optional[str] = None,
               name: Optional[str] = None,
               properties: Optional[dict] = None,
               context: Optional[dict] = None,
               timestamp: Optional[datetime] = None,
               anonymous_id: Optional[Union[str,int]] = None,
               integrations: Optional[dict] = None):
        url = f"{self.base_url}/screen/"
        payload = {
            "user_id": user_id,
            "category": category,
            "name": name,
            "properties": properties,
            "context": context,
            "timestamp": timestamp,
            "anonymous_id": anonymous_id,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    
    def group(self, 
              user_id: Union[str, int, float], 
              group_id: Union[str, int, float], 
              traits: Optional[dict] = None, 
              context: Optional[dict] = None, 
              timestamp: Optional[datetime] = None,
              anonymous_id: Optional[Union[str,int]] = None, 
              integrations: Optional[dict] = None):
        url = f"{self.base_url}/group/"
        payload = {
            "user_id": user_id,
            "group_id": group_id,
            "traits": traits,
            "context": context,
            "timestamp": timestamp,
            "anonymous_id": anonymous_id,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    
    def alias(self, 
              previous_id: str, 
              user_id: str, 
              context: Optional[dict] = None, 
              timestamp: Optional[datetime] = None, 
              integrations: Optional[dict] = None):
        url = f"{self.base_url}/alias/"
        payload = {
            "previous_id": previous_id,
            "user_id": user_id,
            "context": context,
            "timestamp": timestamp,
            "integrations": integrations
        }
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    
    def flush(self):
        url = f"{self.base_url}/flush/"
        response = requests.post(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
