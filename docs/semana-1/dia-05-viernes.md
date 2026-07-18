# Día 05 - Viernes

## Objetivo del día

Desarrollar el ejercicio integrador "El Driver Modernizado". El propósito fue tomar un concepto de un driver UART acoplado y monolítico, y transformarlo en una arquitectura limpia utilizando Python moderno, aplicando todos los principios SOLID y garantizando una cobertura total con pruebas unitarias aisladas.

## Actividades realizadas

- Configuré el entorno de trabajo dentro de `src/semana-1/dia-05-viernes/uart_driver/`.
- Desarrollé `config.py` implementando SRP, usando `@dataclass(frozen=True)` para garantizar la inmutabilidad de la configuración y validando los baudrates.
- Implementé `parsers.py` utilizando el módulo `abc` para aplicar OCP, LSP e ISP a través de la clase abstracta `MessageParser`, soportando los protocolos Modbus RTU y NMEA.
- Desarrollé `device.py` inyectando dependencias por el constructor (DIP) para desacoplar el hardware de la lógica de parseo.
- Implementé `recorder.py` asegurando el SRP para persistir los datos de manera exclusiva en formato JSON-lines.
- Construí una suite de pruebas de más de 12 tests en el directorio `tests/`, garantizando aislamiento con el uso de Mocks y fixtures.

## Problemas encontrados

1. Warning de Ruff (F401): El linter detectó que la librería `pytest` fue importada pero no utilizada dentro del archivo `test_recorder.py`.
2. ModuleNotFoundError en Pytest: Al correr las pruebas, Pytest arrojaba que no encontraba el módulo `config` (`No module named 'config'`). Esto se debió a que el comando se ejecutaba desde la raíz del proyecto, impidiendo que Python resolviera correctamente la ruta de los módulos locales al estar en directorios anidados.

## Soluciones aplicadas

1. Solución a Ruff:Se eliminó la importación `import pytest` de `test_recorder.py`, ya que el fixture `tmp_path` es inyectado automáticamente por la herramienta sin necesidad de importar el módulo en la cabecera
2. Solución a Pytest: Se realizó un cambio de directorio (`cd`) directamente hacia `src/semana-1/dia-05-viernes/uart_driver/` para que la terminal estuviera posicionada junto a los módulos locales, lo que permitió que las importaciones funcionaran correctamente

## Aprendizajes del día

- La Inyección de Dependencias (DIP) es indispensable si se desea testear componentes aislados sin depender de infraestructura real (como puertos de hardware reales).
- Los fixtures nativos de Pytest (como `tmp_path`) facilitan enormemente las pruebas de manejo de archivos sin ensuciar nuestro directorio de trabajo real.
- Las importaciones locales en Python dependen fuertemente del directorio de trabajo actual; ejecutar comandos desde el directorio correcto (o configurar el `PYTHONPATH`) es vital para la resolución de módulos.

## Evidencias

- Captura de la ejecución del linter Ruff completamente limpia.
- Captura de la ejecución exitosa (en verde) de los tests usando `python -m pytest tests/ -v`.
- Archivo `README.md` actualizado con instrucciones de instalación y reflexión de los principios SOLID.

## Estado final

- Se concluyó el 100% de la actividad del viernes y con ello la primera semana. El código está altamente desacoplado, modular, validado estáticamente y completamente cubierto por pruebas unitarias. Listo para el commit final de la semana.