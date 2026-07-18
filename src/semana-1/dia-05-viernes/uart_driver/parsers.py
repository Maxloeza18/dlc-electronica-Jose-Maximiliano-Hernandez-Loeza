from abc import ABC, abstractmethod

class MessageParser(ABC):
    """Interfaz abstracta (ISP) para los procesadores de mensajes del UART."""

    @abstractmethod
    def can_parse(self, data: bytes) -> bool:
        ...

    @abstractmethod
    def parse(self, data: bytes) -> dict:
        ...


class ModbusParser(MessageParser):
    """Implementación concreta para parsear tramas del protocolo Modbus RTU."""

    def can_parse(self, data: bytes) -> bool:
        """
        Verifica si la trama parece ser Modbus RTU basándose en longitud y estructura básica.
        """
        # Una trama Modbus RTU mínima tiene 4 bytes: [Dirección, Función, CRC_L, CRC_H]
        return len(data) >= 4

    def parse(self, data: bytes) -> dict:
        """
        Extrae la dirección del esclavo, el código de función y los datos de la trama Modbus.
        """
        if not self.can_parse(data):
            raise ValueError("Trama inválida o demasiado corta para Modbus RTU")
            
        # Extraemos asumiendo el formato estándar: ID (1 byte), Func (1 byte), Payload (n bytes), CRC (2 bytes)
        return {
            "protocol": "Modbus RTU",
            "slave_address": data[0],
            "function_code": data[1],
            "payload": list(data[2:-2])
        }


class NMEAParser(MessageParser):
    """Implementación concreta para parsear sentencias NMEA de GPS (específicamente $GPGGA)."""

    def can_parse(self, data: bytes) -> bool:
        """
        Verifica si la trama comienza con '$GPGGA'.
        """
        return data.startswith(b"$GPGGA")

    def parse(self, data: bytes) -> dict:
        """
        Extrae la latitud, longitud y calidad de la señal de una sentencia $GPGGA.
        """
        if not self.can_parse(data):
            raise ValueError("La trama no es una sentencia $GPGGA de NMEA válida")
            
        try:
            # Decodificamos de bytes a string y removemos espacios o saltos de línea
            decoded_string = data.decode('ascii').strip()
            # NMEA separa sus valores por comas
            parts = decoded_string.split(',')
            
            return {
                "protocol": "NMEA $GPGGA",
                "time": parts[1],
                "latitude": parts[2],
                "lat_direction": parts[3],
                "longitude": parts[4],
                "lon_direction": parts[5],
                "quality": parts[6]
            }
        except (IndexError, UnicodeDecodeError) as e:
            raise ValueError(f"Error al parsear los campos de la trama NMEA: {e}")