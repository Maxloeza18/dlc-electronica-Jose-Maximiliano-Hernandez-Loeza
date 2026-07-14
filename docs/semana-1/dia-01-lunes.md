# Día 01 - Lunes

## Objetivo del día

Trabajar Python idiomático para ingeniería, practicando el uso de `Enum`, `@dataclass(frozen=True)`, `Protocol` y funciones puras con type hints completos sobre un mini ejercicio de lecturas de sensores. También se debía validar el código con `mypy` y `ruff`.

## Actividades realizadas

- Organicé la estructura inicial de trabajo para la semana 1 dentro del repositorio.
- Configuré el entorno en Linux usando un entorno virtual `.venv`.
- Instalé y ejecuté herramientas de análisis estático con:
  - `python3 -m mypy .`
  - `python3 -m ruff check .`
- Implementé los archivos `functions.py` y `main.py` para modelar lecturas de sensores.
- Definí `SensorType` con `Enum`.
- Definí `Reading` con `@dataclass(frozen=True)`.
- Definí `Transport` con `Protocol`.
- Implementé funciones puras para:
  - convertir una lectura a bytes,
  - convertir temperatura a Fahrenheit,
  - detectar si una lectura supera un umbral,
  - serializar una lectura a diccionario,
  - normalizar una lectura redondeando su valor.

## Problemas encontrados

- Al inicio, en Linux no funcionaban los comandos `pip`, `python` y `ruff` como se esperaba.
- Apareció un error relacionado con entorno administrado externamente al intentar instalar paquetes de Python.
- VS Code siguió mostrando errores de imports y nombres no definidos aunque la terminal ya validaba correctamente.
- Al ejecutar `main.py`, apareció un error de importación relacionado con `Reading` desde `functions.py`.

## Soluciones aplicadas

- Cambié el flujo de trabajo para Linux usando `python3` en lugar de `python`.
- Creé y activé un entorno virtual con:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
- Instalé dependencias dentro del entorno virtual con:
  - `python3 -m pip install mypy ruff`
- Revisé y corregí la estructura de `functions.py` para asegurar que `SensorType` y `Reading` estuvieran definidos correctamente.
- Ajusté imports y pruebas en `main.py`.
- Verifiqué nuevamente hasta obtener validaciones limpias.

## Aprendizajes del día

- Python idiomático no se trata solo de sintaxis, sino de modelar mejor los datos y comportamientos.
- `Enum` ayuda a evitar valores ambiguos o errores por cadenas de texto.
- `@dataclass(frozen=True)` permite representar datos inmutables de manera clara.
- `Protocol` sirve para definir contratos de comportamiento sin forzar herencia.
- `mypy` ayuda a revisar tipos de forma estática antes de ejecutar.
- `ruff` permite detectar problemas de calidad y estilo rápidamente.
- En Linux es importante trabajar con `python3` y preferiblemente dentro de un entorno virtual.

## Evidencias

- Captura de validación de `mypy`.
- Captura de validación de `ruff`.
- Capturas de errores resueltos en VS Code y terminal.
- Ejecución funcional de `main.py`.

## Estado final

Se completó la práctica base del lunes, se resolvieron los problemas del entorno y se dejó funcionando el ejemplo principal con validación estática satisfactoria.