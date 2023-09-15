import math
from abc import ABC, abstractmethod


class ServerResponse(ABC):
    def __init__(self, status_code, data=None, message=None, limit=None):
        self.status_code = status_code
        self.data = data
        self.message = message
        self.limit = limit

    @abstractmethod
    async def _to_dict(self):
        pass

    @abstractmethod
    async def to_dict_many(self):
        pass

    @abstractmethod
    async def to_dict_one(self):
        pass


class SuccessResponse(ServerResponse):
    async def _to_dict(self) -> dict:
        response_dict = {
            "status_code": self.status_code,
            "quantity": None,
            "pages": None,
            "content": [],
        }
        if self.message:
            response_dict["message"] = self.message

        if self.data:
            response_dict["content"] = self.data

        return response_dict

    async def to_dict_one(self):
        response_dict = await self._to_dict()
        if self.data:
            response_dict["quantity"] = 1
            response_dict["content"] = self.data

        return response_dict

    async def to_dict_many(self):
        response_dict = await self._to_dict()
        if self.data:
            response_dict["quantity"] = len(self.data)

        if self.limit:
            response_dict["pages"] = math.ceil(len(self.data) / self.limit)

        return response_dict


class ErrorResponse(ServerResponse):
    async def _to_dict(self):
        response_dict = {
            "status": "error",
            "status_code": self.status_code,
        }
        if self.data:
            response_dict["data"] = self.data
        if self.message:
            response_dict["message"] = self.message
        return response_dict

    async def to_dict_many(self):
        response_dict = await self._to_dict()
        return response_dict

    async def to_dict_one(self):
        response_dict = await self._to_dict()
        return response_dict
