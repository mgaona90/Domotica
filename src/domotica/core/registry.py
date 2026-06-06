from domotica.core.device import Device


class DeviceRegistry:
    def __init__(self) -> None:
        self._devices: dict[str, Device] = {}

    def register(self, device: Device) -> None:
        self._devices[device.device_id] = device

    def get(self, device_id: str) -> Device | None:
        return self._devices.get(device_id)

    def get_all(self) -> list[Device]:
        return list(self._devices.values())

    def remove(self, device_id: str) -> bool:
        if device_id in self._devices:
            del self._devices[device_id]
            return True
        return False


registry = DeviceRegistry()
