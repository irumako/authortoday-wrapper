from typing import Optional

import httpx


class Base:
    def __init__(self, token: str):
        self.__token = token
        self.__auth_header = {'Authorization': f'Bearer {self.__token}'}

    def get(self, endpoint: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> httpx.Response:
        if headers is None:
            headers = {}
        try:
            response = httpx.get(endpoint, headers=self.__auth_header | headers, params=params)
            response.raise_for_status()

        except httpx.HTTPError as exc:
            raise exc

        return response
