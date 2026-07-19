from abc import ABC, abstractmethod
from dataclasses import dataclass


# 1. SRP: Single Responsibility Principle


# MAL DISEÑO: La clase controla la energía del dispositivo y también hace diagnósticos de red.
class BadDeviceManager:
    def toggle_power(self, state: bool) -> str:
        return "Encendido" if state else "Apagado"
        
    def ping_network(self, ip_address: str) -> bool:
        # Simula un diagnóstico de red
        return True

# BUEN DISEÑO: Separamos el control de energía del diagnóstico de red.
class PowerController:
    def toggle(self, state: bool) -> str:
        return "Encendido" if state else "Apagado"

class NetworkDiagnostic:
    def ping(self, ip_address: str) -> bool:
        # Lógica real de ping de red
        return True



# 2. OCP: Open/Closed Principle


@dataclass
class HomeState:
    time_of_day: str
    home_occupied: bool

# MAL DISEÑO: Si agregamos una rutina "Vacaciones", hay que modificar este método.
class BadRoutineTrigger:
    def execute_routine(self, state: HomeState) -> str:
        if state.time_of_day == "morning":
            return "Cafetera encendida, persianas abiertas."
        elif state.time_of_day == "night" and state.home_occupied:
            return "Luces atenuadas, puertas bloqueadas."
        return "Sin acción."

# BUEN DISEÑO: Usamos una interfaz. Agregar una rutina "Vacaciones" implica crear una clase nueva.
class RoutineStrategy(ABC):
    @abstractmethod
    def execute(self, state: HomeState) -> str | None: ...

class MorningRoutine(RoutineStrategy):
    def execute(self, state: HomeState) -> str | None:
        if state.time_of_day == "morning":
            return "Cafetera encendida, persianas abiertas."
        return None

class NightRoutine(RoutineStrategy):
    def execute(self, state: HomeState) -> str | None:
        if state.time_of_day == "night" and state.home_occupied:
            return "Luces atenuadas, puertas bloqueadas."
        return None

class AutomationSystem:
    def __init__(self, routines: list[RoutineStrategy]):
        self._routines = routines

    def run(self, state: HomeState) -> list[str]:
        actions = []
        for routine in self._routines:
            result = routine.execute(state)
            if result:
                actions.append(result)
        return actions



# 3. LSP: Liskov Substitution Principle


# MAL DISEÑO: La Smart TV hereda de un dispositivo genérico con batería, pero se conecta a la pared.
class BadSmartDevice:
    def recharge_battery(self) -> str:
        return "Recargando al 100%"

class BadSmartTV(BadSmartDevice):
    def recharge_battery(self) -> str:
        raise NotImplementedError("La TV no tiene batería, se conecta a la pared.") # Viola LSP

# BUEN DISEÑO: Un contrato base que todos cumplen y clases especializadas si es necesario.
class SmartDevice(ABC):
    @abstractmethod
    def get_status(self) -> str: ...

class SmartLock(SmartDevice):
    def get_status(self) -> str:
        return "Puerta: Bloqueada"

class SmartThermostat(SmartDevice):
    def get_status(self) -> str:
        return "Termostato: 22°C"

# Función que espera un SmartDevice y funciona sin importar el tipo específico.
def check_device_status(device: SmartDevice) -> str:
    return device.get_status()