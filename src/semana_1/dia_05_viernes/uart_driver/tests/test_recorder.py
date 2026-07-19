import json
from recorder import DataRecorder

def test_recorder_creates_file(tmp_path):
    """Prueba que el grabador cree el archivo si no existe."""
    filepath = tmp_path / "test_log.jsonl"
    recorder = DataRecorder(filepath)
    
    recorder.record({"status": "ok"})
    assert filepath.exists()

def test_recorder_writes_valid_json(tmp_path):
    """Prueba que los datos se guarden en formato JSON válido."""
    filepath = tmp_path / "test_log.jsonl"
    recorder = DataRecorder(filepath)
    
    test_data = {"protocol": "NMEA", "value": 123}
    recorder.record(test_data)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        loaded_data = json.loads(content)
        
    assert loaded_data == test_data

def test_recorder_appends_multiple_lines(tmp_path):
    """Prueba que múltiples escrituras se añadan como líneas nuevas."""
    filepath = tmp_path / "test_log.jsonl"
    recorder = DataRecorder(filepath)
    
    recorder.record({"id": 1})
    recorder.record({"id": 2})
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    assert len(lines) == 2
    assert json.loads(lines[0])["id"] == 1
    assert json.loads(lines[1])["id"] == 2