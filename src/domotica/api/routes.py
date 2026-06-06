from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from domotica.core.registry import registry
from domotica.devices.light import Light
from domotica.devices.sensor import TemperatureSensor

router = APIRouter()


class LightCommand(BaseModel):
    on: bool
    brightness: int = 100


class SensorReading(BaseModel):
    temperature: float
    humidity: float | None = None


@router.get("/devices")
def list_devices():
    return [d.to_dict() for d in registry.get_all()]


@router.get("/devices/{device_id}")
def get_device(device_id: str):
    device = registry.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return device.to_dict()


@router.post("/devices/lights/{device_id}/command")
def command_light(device_id: str, command: LightCommand):
    device = registry.get(device_id)
    if not device or not isinstance(device, Light):
        raise HTTPException(status_code=404, detail="Luz no encontrada")
    if command.on:
        device.turn_on(command.brightness)
    else:
        device.turn_off()
    return device.to_dict()


@router.post("/devices/sensors/{device_id}/reading")
def update_sensor(device_id: str, reading: SensorReading):
    device = registry.get(device_id)
    if not device or not isinstance(device, TemperatureSensor):
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    device.update_reading(reading.temperature, reading.humidity)
    return device.to_dict()
