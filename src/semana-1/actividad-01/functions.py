from dataclasses import dataclass
from enum import Enum, auto
from typing import Protocol


class SensorType(Enum):
    TEMPERATURE = auto()
    HUMIDITY = auto()


@dataclass(frozen=True)
class Reading:
    sensor_id: str
    value: float
    sensor_type: SensorType


class Transport(Protocol):
    def send(self, payload: bytes) -> None:
        ...


def to_frame(r: Reading) -> bytes:
    return f"{r.sensor_id},{r.value:.2f},{r.sensor_type.name}".encode()


def celsius_to_fahrenheit(value: float) -> float:
    return (value * 9 / 5) + 32


def is_above_threshold(r: Reading, threshold: float) -> bool:
    return r.value > threshold


def to_dict(r: Reading) -> dict[str, str | float]:
    return {
        "sensor_id": r.sensor_id,
        "value": r.value,
        "sensor_type": r.sensor_type.name,
    }


def normalize_reading(r: Reading) -> Reading:
    return Reading(
        sensor_id=r.sensor_id,
        value=round(r.value, 2),
        sensor_type=r.sensor_type,
    )