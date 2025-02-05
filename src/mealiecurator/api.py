"""API client for Mealie."""

from typing import Any, Dict, List

import httpx


class MealieClient:
    """Client for interacting with the Mealie API."""

    def __init__(self, base_url: str, api_token: str) -> None:
        """Initialize the API client."""
        self.base_url = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {api_token}"}

    def get_all_foods(self) -> List[Dict[str, Any]]:
        """Get all foods from Mealie."""
        url = f"{self.base_url}/api/foods"
        with httpx.Client() as client:
            response = client.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()["items"]

    def update_food(self, food_id: str, food_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a food in Mealie."""
        url = f"{self.base_url}/api/foods/{food_id}"
        with httpx.Client() as client:
            response = client.put(url, headers=self.headers, json=food_data)
            response.raise_for_status()
            return response.json()
