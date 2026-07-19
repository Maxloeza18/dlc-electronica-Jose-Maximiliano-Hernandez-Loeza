from actividad_02_solid import (
    PowerController, NetworkDiagnostic,
    HomeState, MorningRoutine, NightRoutine, AutomationSystem,
    SmartLock, SmartThermostat, check_device_status
)

# --- Tests para SRP ---
def test_srp_power_controller():
    """Prueba que el controlador de energía solo cambie estados."""
    controller = PowerController()
    assert controller.toggle(True) == "Encendido"
    assert controller.toggle(False) == "Apagado"

def test_srp_network_diagnostic():
    """Prueba que el diagnóstico de red devuelva booleanos correctamente."""
    diag = NetworkDiagnostic()
    assert diag.ping("192.168.1.1") is True

# --- Tests para OCP ---
def test_ocp_morning_routine():
    """Prueba que la rutina matutina se dispare correctamente con la estrategia."""
    state = HomeState(time_of_day="morning", home_occupied=True)
    system = AutomationSystem(routines=[MorningRoutine(), NightRoutine()])
    
    actions = system.run(state)
    assert "Cafetera encendida, persianas abiertas." in actions
    assert len(actions) == 1

def test_ocp_no_routine_trigger():
    """Prueba que si no hay coincidencias de estado, el sistema no ejecuta nada."""
    state = HomeState(time_of_day="afternoon", home_occupied=False)
    system = AutomationSystem(routines=[MorningRoutine(), NightRoutine()])
    
    actions = system.run(state)
    assert len(actions) == 0

# --- Tests para LSP ---
def test_lsp_smart_lock_substitution():
    """Prueba que la cerradura inteligente se comporte como un SmartDevice."""
    lock = SmartLock()
    result = check_device_status(lock)
    assert result == "Puerta: Bloqueada"

def test_lsp_thermostat_substitution():
    """Prueba que el termostato inteligente se comporte como un SmartDevice."""
    thermostat = SmartThermostat()
    result = check_device_status(thermostat)
    assert result == "Termostato: 22°C"