import pytest
from parsers import ModbusParser, NMEAParser

# --- Tests para ModbusParser ---
def test_modbus_can_parse_valid_frame():
    """Prueba que reconozca una trama de tamaño válido."""
    parser = ModbusParser()
    valid_frame = b'\x01\x03\x00\x00\x00\x02\xC4\x0B' # 8 bytes
    assert parser.can_parse(valid_frame) is True

def test_modbus_parse_invalid_frame():
    """Prueba que rechace tramas demasiado cortas."""
    parser = ModbusParser()
    invalid_frame = b'\x01\x03' # Solo 2 bytes, inválido para Modbus RTU
    with pytest.raises(ValueError, match="Trama inválida"):
        parser.parse(invalid_frame)

def test_modbus_parse_extraction():
    """Prueba la correcta extracción de datos Modbus."""
    parser = ModbusParser()
    frame = b'\x05\x04\x12\x34\xAA\xBB'
    result = parser.parse(frame)
    assert result["slave_address"] == 5
    assert result["function_code"] == 4
    assert result["payload"] == [18, 52] # 0x12 y 0x34 en decimal

# --- Tests para NMEAParser ---
def test_nmea_can_parse_valid_sentence():
    """Prueba que reconozca el inicio correcto de una sentencia NMEA."""
    parser = NMEAParser()
    sentence = b'$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
    assert parser.can_parse(sentence) is True

def test_nmea_parse_invalid_sentence():
    """Prueba que rechace tramas que no son $GPGGA."""
    parser = NMEAParser()
    invalid_sentence = b'$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A'
    with pytest.raises(ValueError, match="La trama no es una sentencia"):
        parser.parse(invalid_sentence)

def test_nmea_parse_extraction():
    """Prueba la correcta extracción de campos NMEA."""
    parser = NMEAParser()
    sentence = b'$GPGGA,123519,4807.038,N,01131.000,E,1'
    result = parser.parse(sentence)
    assert result["time"] == "123519"
    assert result["latitude"] == "4807.038"
    assert result["lat_direction"] == "N"