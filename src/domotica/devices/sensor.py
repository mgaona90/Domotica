from datetime import datetime
from typing import Any

from domotica.core.device import Device, DeviceType


class TemperatureSensor(Device):
    def __init__(self, device_id: str, name: str) -> None:
        super().__init__(device_id, name, DeviceType.SENSOR)
        self._temperature: float | None = None
        self._humidity: float | None = None

    def update_reading(self, temperature: float, humidity: float | None = None) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.state.last_seen = datetime.now()

    def get_status(self) -> dict[str, Any]:
        return {
            "temperature": self._temperature,
            "humidity": self._humidity,
        }
