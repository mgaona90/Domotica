from domotica.devices.light import Light
from domotica.devices.sensor import TemperatureSensor


def test_light_turn_on():
    light = Light("luz-1", "Luz Test")
    light.turn_on(brightness=80)
    status = light.get_status()
    assert status["on"] is True
    assert status["brightness"] == 80


def test_light_turn_off():
    light = Light("luz-1", "Luz Test")
    light.turn_on()
    light.turn_off()
    assert light.get_status()["on"] is False


def test_light_brightness_clamp():
    light = Light("luz-1", "Luz Test")
    light.turn_on(brightness=999)
    assert light.get_status()["brightness"] == 100


def test_sensor_reading():
    sensor = TemperatureSensor("sensor-1", "Sensor Test")
    sensor.update_reading(temperature=22.5, humidity=60.0)
    status = sensor.get_status()
    assert status["temperature"] == 22.5
    assert status["humidity"] == 60.0


def test_sensor_no_reading():
    sensor = TemperatureSensor("sensor-1", "Sensor Test")
    assert sensor.get_status()["temperature"] is None
