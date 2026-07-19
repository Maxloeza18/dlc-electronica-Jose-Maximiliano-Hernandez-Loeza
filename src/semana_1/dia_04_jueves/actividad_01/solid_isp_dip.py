from typing import Protocol
from dataclasses import dataclass
from datetime import datetime

# 1. Definimos la estructura de la lectura del sensor
@dataclass
class SensorReading:
    sensor_id: str
    value: float
    timestamp: str = datetime.now().isoformat()

# 2. ISP: Dividimos la interfaz "gorda" en piezas pequeñas usando Protocol
class Readable(Protocol):
    def read(self) -> float: 
        ...

class Writable(Protocol):
    def write(self, value: float) -> None: 
        ...

class Calibratable(Protocol):
    def calibrate(self) -> None: 
        ...
    
    def reset(self) -> None: 
        ...

# 3. DIP: Definimos la abstracción del almacenamiento (El Contrato)
class DataRepository(Protocol):
    def save(self, reading: SensorReading) -> None: 
        ...
    
    def get_latest(self, sensor_id: str) -> SensorReading | None: 
        ...

# 4. DIP: Inyección de dependencias en el procesador principal
class DataProcessor:
    """Depende de la abstraccion, no de una implementacion concreta."""
    def __init__(self, repository: DataRepository) -> None:
        self._repo = repository  # inyeccion de dependencias
        
    def process_and_store(self, reading: SensorReading) -> None:
        # Aquí puedes imaginar que filtras ruido de la señal analógica o escalas el valor
        print(f"Procesando lectura del sensor {reading.sensor_id}: {reading.value}")
        
        # Guardamos el dato usando la abstracción. 
        # ¡A DataProcessor no le importa si es PostgreSQL, MySQL o una lista en RAM!
        self._repo.save(reading)

# 5. DIP en acción: Implementación de un repositorio para pruebas (en memoria RAM)
class InMemoryRepository:
    def __init__(self) -> None:
        # Simulamos una base de datos usando un diccionario simple de Python
        self._storage: dict[str, SensorReading] = {}
        
    def save(self, reading: SensorReading) -> None:
        self._storage[reading.sensor_id] = reading
        print(f"[BD Memoria] Guardado exitosamente: {reading.sensor_id} -> {reading.value}")
        
    def get_latest(self, sensor_id: str) -> SensorReading | None:
        return self._storage.get(sensor_id)

# 6. Prueba de ejecución
if __name__ == "__main__":
    print("--- Iniciando sistema ---")
    
    # A. Creamos nuestra "base de datos" falsa
    repo_prueba = InMemoryRepository()
    
    # B. Inyectamos esa dependencia al procesador principal
    procesador = DataProcessor(repository=repo_prueba)
    
    # C. Simulamos la lectura de un sensor en tu hardware
    lectura_simulada = SensorReading(sensor_id="SnP_zona_1", value=23.7)
    
    # D. Procesamos y guardamos
    procesador.process_and_store(lectura_simulada)
    
    # E. Verificamos que se pueda recuperar de la base de datos
    resultado = repo_prueba.get_latest("SnP_zona_1")
    print(f"--- Dato recuperado del repositorio: {resultado.value} ---") # type: ignore
    