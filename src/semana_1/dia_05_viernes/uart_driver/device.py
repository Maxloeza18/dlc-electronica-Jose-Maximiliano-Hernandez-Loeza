from config import UartConfig
from parsers import MessageParser

class UartDevice:
    """
    Maneja la conexión y lectura simulada de un puerto serial.
    Aplica DIP al recibir sus dependencias por inyección en el constructor.
    """
    
    def __init__(self, config: UartConfig, parser: MessageParser) -> None:
        """
        Inicializa el dispositivo UART con una configuración y un parser específicos.
        """
        self._config = config
        self._parser = parser
        self._is_connected = False

    def connect(self) -> None:
        """Simula la conexión al puerto serial."""
        if not self._is_connected:
            self._is_connected = True
            print(f"UART Conectado: Baudrate {self._config.baudrate}, Timeout {self._config.timeout}s")

    def disconnect(self) -> None:
        """Simula la desconexión del puerto serial."""
        if self._is_connected:
            self._is_connected = False
            print("UART Desconectado.")

    def read_and_parse(self, raw_data: bytes) -> dict:
        """
        Toma datos crudos simulados (bytes), verifica el estado de conexión
        y delega la interpretación al parser inyectado.
        
        Lanza:
            RuntimeError: Si se intenta leer cuando el dispositivo está desconectado.
            ValueError: Si los datos no son válidos para el parser actual (delegado).
        """
        if not self._is_connected:
            raise RuntimeError("No se puede leer: El dispositivo UART está desconectado.")
            
        # El dispositivo no sabe CÓMO parsear, solo le pide al parser que lo haga.
        return self._parser.parse(raw_data)