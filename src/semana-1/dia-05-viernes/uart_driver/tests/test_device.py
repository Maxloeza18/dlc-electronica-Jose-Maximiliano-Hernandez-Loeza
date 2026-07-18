import pytest
from config import UartConfig
from device import UartDevice
from parsers import MessageParser

class MockParser(MessageParser):
    """Parser falso para inyectar en el UartDevice (DIP)."""
    def can_parse(self, data: bytes) -> bool:
        return True
        
    def parse(self, data: bytes) -> dict:
        return {"mocked": True, "data": data.decode('ascii')}

def test_device_connect_disconnect():
    """Prueba los cambios de estado de conexión."""
    config = UartConfig(9600, 'N', 1, 1.0)
    device = UartDevice(config, MockParser())
    
    assert device._is_connected is False
    device.connect()
    assert device._is_connected is True
    device.disconnect()
    assert device._is_connected is False

def test_device_read_disconnected_raises_error():
    """Prueba que intentar leer desconectado lance un error."""
    config = UartConfig(9600, 'N', 1, 1.0)
    device = UartDevice(config, MockParser())
    
    with pytest.raises(RuntimeError, match="El dispositivo UART está desconectado"):
        device.read_and_parse(b'test_data')

def test_device_read_delegates_to_parser():
    """Prueba que el dispositivo inyecte los datos al parser correctamente."""
    config = UartConfig(9600, 'N', 1, 1.0)
    device = UartDevice(config, MockParser())
    
    device.connect()
    result = device.read_and_parse(b'hello')
    assert result["mocked"] is True
    assert result["data"] == "hello"