from solid_isp_dip import SensorReading, DataProcessor, InMemoryRepository

def test_procesador_guarda_lectura_correctamente():
    # 1. Preparamos el entorno de prueba (Arrange)
    repo_prueba = InMemoryRepository()
    procesador = DataProcessor(repository=repo_prueba)
    lectura = SensorReading(sensor_id="sensor_test_01", value=100.5)
    
    # 2. Ejecutamos la acción (Act)
    procesador.process_and_store(lectura)
    
    # 3. Verificamos el resultado (Assert)
    resultado = repo_prueba.get_latest("sensor_test_01")
    
    assert resultado is not None
    assert resultado.sensor_id == "sensor_test_01"
    assert resultado.value == 100.5