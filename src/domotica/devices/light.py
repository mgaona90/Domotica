from typing import Any

from domotica.core.device import Device, DeviceType


class Light(Device):
    def __init__(self, device_id: str, name: str) -> None:
        super().__init__(device_id, name, DeviceType.LIGHT)
        self._on: bool = False
        self._brightness: int = 100  # 0-100

    def turn_on(self, brightness: int = 100) -> None:
        self._on = True
        self._brightness = max(0, min(100, brightness))

    def turn_off(self) -> None:
        self._on = False

    def set_brightness(self, brightness: int) -> None:
        self._brightness = max(0, min(100, brightness))

    def get_status(self) -> dict[str, Any]:
        return {
            "on": self._on,
            "brightness": self._brightness,
        }
