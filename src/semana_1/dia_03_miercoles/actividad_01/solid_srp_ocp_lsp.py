from abc import ABC, abstractmethod
from dataclasses import dataclass


# 1. SRP: Single Responsibility Principle


# MAL DISEÑO: La clase lee el sensor y también maneja la persistencia.
class BadSensorManager:
    def read_data(self) -> float:
        # Simula lectura
        return 25.5
        
    def save_to_db(self, data: float) -> None:
        # Simula guardado
        print(f"Guardando {data} en base de datos...")

# BUEN DISEÑO: Separamos las responsabilidades en dos clases.
class SensorReader:
    def read(self) -> float:
        return 25.5

class DataLogger:
    def persist(self, data: float) -> None:
        # Aquí iría la lógica real de guardado (archivo, DB, etc.)
        pass



# 2. OCP: Open/Closed Principle


@dataclass
class SensorReading:
    sensor_id: str
    value: float

# MAL DISEÑO: Si queremos agregar EmailAlert, debemos modificar esta clase.
class BadAnomalyDetector:
    def __init__(self, threshold: float):
        self._threshold = threshold

    def check(self, reading: SensorReading, alert_type: str) -> str:
        if reading.value > self._threshold:
            if alert_type == "console":
                return f"Console: Anomalía en {reading.sensor_id}"
            elif alert_type == "file":
                return f"FileLog: Anomalía en {reading.sensor_id}"
        return "OK"

# BUEN DISEÑO: Usamos abstracción. Agregar EmailAlert mañana NO toca este código.
class AlertStrategy(ABC):
    @abstractmethod
    def send(self, message: str) -> str: ...

class ConsoleAlert(AlertStrategy):
    def send(self, message: str) -> str:
        return f"Console: {message}"

class FileAlert(AlertStrategy):
    def send(self, message: str) -> str:
        return f"FileLog: {message}"

class AnomalyDetector:
    def __init__(self, alert: AlertStrategy, threshold: float) -> None:
        self._alert = alert
        self._threshold = threshold

    def check(self, reading: SensorReading) -> str | None:
        if reading.value > self._threshold:
            return self._alert.send(f"Anomalía en {reading.sensor_id}")
        return None



# 3. LSP: Liskov Substitution Principle


# MAL DISEÑO: BrokenSensor hereda pero cambia el tipo de retorno/comportamiento.
class BadBaseSensor:
    def get_value(self) -> float:
        return 10.0

class BrokenSensor(BadBaseSensor):
    def get_value(self) -> str: # type: ignore 
        return "Error de lectura"

# BUEN DISEÑO: Ambas clases respetan el contrato de la interfaz.
class BaseSensor(ABC):
    @abstractmethod
    def read(self) -> float: ...

class TemperatureSensor(BaseSensor):
    def read(self) -> float:
        return 22.4  # Grados Celsius

class HumiditySensor(BaseSensor):
    def read(self) -> float:
        return 45.0  # Porcentaje

# Función que espera a la clase base y funciona con CUALQUIER subclase sin saber cuál es
def process_sensor(sensor: BaseSensor) -> float:
    return sensor.read()