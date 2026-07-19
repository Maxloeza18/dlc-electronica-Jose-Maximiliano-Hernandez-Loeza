import json
from pathlib import Path

class DataRecorder:
    """
    Persiste datos parseados en un archivo de texto.
    Aplica SRP al tener como única responsabilidad el guardado de datos.
    """
    
    def __init__(self, filepath: str | Path) -> None:
        """
        Inicializa el grabador de datos con la ruta del archivo destino.
        """
        self._filepath = Path(filepath)
        
        # Opcional: Asegurarnos de que el directorio padre exista
        self._filepath.parent.mkdir(parents=True, exist_ok=True)

    def record(self, data: dict) -> None:
        """
        Guarda un diccionario como una nueva línea JSON (JSON-lines) en el archivo.
        
        Args:
            data (dict): Diccionario con los datos parseados de la trama.
        """
        # Usamos el modo 'a' (append) para no sobreescribir datos anteriores
        with open(self._filepath, 'a', encoding='utf-8') as f:
            json_line = json.dumps(data)
            f.write(json_line + '\n')