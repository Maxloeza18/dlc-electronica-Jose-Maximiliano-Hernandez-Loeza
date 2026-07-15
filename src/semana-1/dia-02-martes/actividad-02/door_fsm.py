from enum import Enum, auto


# Define los estados posibles de la puerta
class DoorState(Enum):
    CLOSED = auto()   # Puerta cerrada
    OPEN = auto()     # Puerta abierta
    LOCKED = auto()   # Puerta cerrada con seguro


# Clase que modela la máquina de estados de la puerta
class DoorFSM:
    def __init__(self):
        # Estado inicial de la puerta
        self._state = DoorState.CLOSED

    @property
    def state(self):
        # Devuelve el estado actual
        return self._state

    def open(self):
        # Solo se puede abrir si está cerrada
        if self._state == DoorState.CLOSED:
            self._state = DoorState.OPEN
        return self._state

    def close(self):
        # Solo se puede cerrar si está abierta
        if self._state == DoorState.OPEN:
            self._state = DoorState.CLOSED
        return self._state

    def lock(self):
        # Solo se puede poner seguro si está cerrada
        if self._state == DoorState.CLOSED:
            self._state = DoorState.LOCKED
        return self._state

    def unlock(self):
        # Solo se puede quitar seguro si está bloqueada
        if self._state == DoorState.LOCKED:
            self._state = DoorState.CLOSED
        return self._state