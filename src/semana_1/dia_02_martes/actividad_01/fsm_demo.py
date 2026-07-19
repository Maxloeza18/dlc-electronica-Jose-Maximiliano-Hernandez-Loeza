from enum import Enum, auto


# Enum que define los estados posibles del semáforo
class TrafficLightState(Enum):
    RED = auto()      # Estado rojo
    YELLOW = auto()   # Estado amarillo
    GREEN = auto()    # Estado verde


# Clase que modela la máquina de estados finita del semáforo
class TrafficLightFSM:
    def __init__(self):
        # El semáforo comienza en rojo
        self._state = TrafficLightState.RED

        # Contador de ciclos completos; inicia en 0
        self._cycle_count = 0

    @property
    def state(self):
        # Devuelve el estado actual del semáforo
        return self._state

    @property
    def cycle_count(self):
        # Devuelve cuántos ciclos completos se han realizado
        return self._cycle_count

    def transition(self):
        # Diccionario que define la siguiente transición para cada estado
        transitions = {
            TrafficLightState.RED: TrafficLightState.GREEN,
            TrafficLightState.GREEN: TrafficLightState.YELLOW,
            TrafficLightState.YELLOW: TrafficLightState.RED,
        }

        # Actualizamos el estado al siguiente según el diccionario
        self._state = transitions[self._state]

        # Si el nuevo estado es RED, significa que se cerró un ciclo completo
        if self._state == TrafficLightState.RED:
            self._cycle_count += 1

        # Regresamos el nuevo estado por comodidad
        return self._state
    