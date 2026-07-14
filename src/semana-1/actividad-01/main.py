from functions import (
    Reading,
    SensorType,
    celsius_to_fahrenheit,
    is_above_threshold,
    normalize_reading,
    to_dict,
    to_frame,
)


def main() -> None:
    reading = Reading(
        sensor_id="sensor-1",
        value=23.567,
        sensor_type=SensorType.TEMPERATURE,
    )

    print("Reading original:")
    print(reading)

    print("\nFrame en bytes:")
    print(to_frame(reading))

    print("\nTemperatura en Fahrenheit:")
    print(celsius_to_fahrenheit(reading.value))

    print("\n¿Supera el umbral de 20.0?")
    print(is_above_threshold(reading, 20.0))

    print("\nReading como diccionario:")
    print(to_dict(reading))

    print("\nReading normalizado:")
    print(normalize_reading(reading))


if __name__ == "__main__":
    main()