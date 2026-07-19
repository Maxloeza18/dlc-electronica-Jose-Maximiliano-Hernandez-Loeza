from dataclasses import dataclass

@dataclass(frozen=True)
class UartConfig:
    """
    Configuración inmutable para el driver UART.
    
    Atributos:
        baudrate (int): Velocidad de transmisión en baudios (ej. 9600, 115200).
        parity (str): Tipo de paridad ('N' para None, 'E' para Even, 'O' para Odd).
        stop_bits (int): Número de bits de parada (1 o 2).
        timeout (float): Tiempo de espera en segundos para las lecturas.
    """
    baudrate: int
    parity: str
    stop_bits: int
    timeout: float

    def __post_init__(self) -> None:
        """
        Valida los parámetros de configuración después de la instanciación.
        """
        valid_baudrates = {9600, 19200, 38400, 57600, 115200}
        
        if self.baudrate not in valid_baudrates:
            raise ValueError(f"Baudrate inválido. Valores permitidos: {valid_baudrates}")
            
        if self.parity not in {'N', 'E', 'O'}:
            raise ValueError(f"Parity '{self.parity}' inválido. Debe ser 'N', 'E' u 'O'")
            
        if self.stop_bits not in {1, 2}:
            raise ValueError(f"stop_bits {self.stop_bits} inválido. Debe ser 1 o 2")
            
        if self.timeout <= 0:
            raise ValueError("El timeout debe ser estrictamente mayor a 0")