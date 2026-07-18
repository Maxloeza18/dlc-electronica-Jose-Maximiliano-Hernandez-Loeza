import pytest
from dataclasses import FrozenInstanceError
from config import UartConfig

def test_uart_config_valid_instantiation():
    """Prueba que una configuración válida se cree correctamente."""
    config = UartConfig(baudrate=115200, parity='N', stop_bits=1, timeout=1.5)
    assert config.baudrate == 115200
    assert config.timeout == 1.5

def test_uart_config_invalid_baudrate():
    """Prueba que un baudrate no estándar levante un ValueError[cite: 73]."""
    with pytest.raises(ValueError, match="Baudrate inválido"):
        UartConfig(baudrate=12345, parity='N', stop_bits=1, timeout=1.0)

def test_uart_config_immutability():
    """Prueba que intentar modificar un atributo levante un error (inmutabilidad)[cite: 74]."""
    config = UartConfig(baudrate=9600, parity='E', stop_bits=1, timeout=2.0)
    
    with pytest.raises(FrozenInstanceError):
        config.baudrate = 115200 # No se puede modificar tras la creación