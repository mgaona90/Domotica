from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class DeviceType(str, Enum):
    LIGHT = "light"
    SENSOR = "sensor"
    SWITCH = "switch"


class DeviceState(BaseModel):
    is_online: bool = True
    last_seen: datetime = Field(default_factory=datetime.now)
    attributes: dict[str, Any] = Field(default_factory=dict)


class Device(ABC):
    def __init__(self, device_id: str, name: str, device_type: DeviceType) -> None:
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.state = DeviceState()

    @abstractmethod
    def get_status(self) -> dict[str, Any]:
        pass

    def to_dict(self) -> dict[str, Any]:
        return {
            "device_id": self.device_id,
            "name": self.name,
            "type": self.device_type,
            **self.get_status(),
            "is_online": self.state.is_online,
            "last_seen": self.state.last_seen.isoformat(),
        }
