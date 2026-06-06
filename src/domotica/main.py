import logging

import uvicorn
from fastapi import FastAPI

from domotica.api.routes import router
from domotica.config import settings
from domotica.core.registry import registry
from domotica.devices.light import Light
from domotica.devices.sensor import TemperatureSensor

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def seed_demo_devices() -> None:
    registry.register(Light("luz-living", "Luz Living"))
    registry.register(Light("luz-cocina", "Luz Cocina"))
    registry.register(TemperatureSensor("sensor-temp-01", "Sensor Temperatura Habitación"))
    logger.info("Dispositivos demo registrados")


@app.get("/")
def health():
    return {"status": "ok", "app": settings.app_name}


if __name__ == "__main__":
    uvicorn.run("domotica.main:app", host=settings.app_host, port=settings.app_port, reload=settings.app_debug)
