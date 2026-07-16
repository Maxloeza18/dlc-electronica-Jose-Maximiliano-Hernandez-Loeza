from solid_srp_ocp_lsp import (
    SensorReader, DataLogger, 
    SensorReading, ConsoleAlert, FileAlert, AnomalyDetector,
    TemperatureSensor, HumiditySensor, process_sensor
)

# Tests para SRP 
def test_srp_sensor_reader():
    """Prueba que el lector se enfoque solo en retornar un float."""
    reader = SensorReader()
    assert isinstance(reader.read(), float)
    assert reader.read() == 25.5

def test_srp_data_logger():
    """Prueba que el logger pueda recibir el dato sin fallar."""
    logger = DataLogger()
    # Como persist es un dummy (pass), solo validamos que no levante excepciones
    try:
        logger.persist(25.5)
        success = True
    except Exception:
        success = False
    assert success is True

# Tests para OCP 
def test_ocp_console_alert_triggers():
    """Prueba que el detector use correctamente la estrategia de consola."""
    alert_strategy = ConsoleAlert()
    detector = AnomalyDetector(alert=alert_strategy, threshold=30.0)
    reading = SensorReading(sensor_id="TEMP_01", value=35.5)
    
    result = detector.check(reading)
    assert result == "Console: Anomalía en TEMP_01"

def test_ocp_no_alert_below_threshold():
    """Prueba que no se disparen alertas si no se supera el umbral, usando FileAlert."""
    alert_strategy = FileAlert()
    detector = AnomalyDetector(alert=alert_strategy, threshold=50.0)
    reading = SensorReading(sensor_id="HUM_02", value=45.0)
    
    result = detector.check(reading)
    assert result is None

# Tests para LSP 
def test_lsp_temperature_substitution():
    """Prueba que un TemperatureSensor funcione perfectamente donde se espera un BaseSensor."""
    temp_sensor = TemperatureSensor()
    result = process_sensor(temp_sensor)
    assert isinstance(result, float)
    assert result == 22.4

def test_lsp_humidity_substitution():
    """Prueba que un HumiditySensor funcione perfectamente donde se espera un BaseSensor."""
    hum_sensor = HumiditySensor()
    result = process_sensor(hum_sensor)
    assert isinstance(result, float)
    assert result == 45.0