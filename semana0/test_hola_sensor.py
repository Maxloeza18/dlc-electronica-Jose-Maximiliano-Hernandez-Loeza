from hola_sensor import Sensor

def test_read_sensor():
    sensor = Sensor()
    assert sensor.read() == 23.5
