# Día 06 - Sábado

## Objetivo del día

Realizar la validación global y el cierre de la Semana 1. El objetivo principal fue asegurar el cumplimiento de los entregables requeridos en la rúbrica para el "Estándar esperado", lo cual implicaba tener el linter `ruff` limpio, lograr una cobertura de pruebas superior al 70% con `pytest` y conseguir un análisis de tipado estático sin errores utilizando `mypy`.

## Actividades realizadas

- Revisión del checklist de entregables (FSM, principios SOLID, y driver modernizado).
- Ejecución global de `ruff check` sobre el directorio de la semana 1.
- Instalación de `pytest-cov` y ejecución de las pruebas globales para medir la cobertura del código.
- Ejecución global de `mypy` para la verificación estricta de tipado.
- Renombramiento general de directorios (de *kebab-case* a *snake_case*) para alinearse con los estándares de Python.
- Creación y configuración de los archivos `pytest.ini` y `mypy.ini` en la raíz del proyecto para instruir a las herramientas sobre las rutas de los módulos locales.

## Problemas encontrados

- Al ejecutar `pytest` y `mypy` desde la raíz, se presentaron múltiples errores de resolución de rutas (`ModuleNotFoundError` e `import-not-found`) debido a la estructura anidada de carpetas.
- Mypy generó un error de colisión de módulos (`Duplicate module named "__main__"`) al intentar procesar los directorios base que aún contenían archivos `__init__.py`.
- Mypy detectó exitosamente errores lógicos genuinos: una violación del principio LSP introducida intencionalmente (retorno de `str` en lugar de `float`) y un riesgo de acceder al atributo `.value` en un objeto que podría ser `None`.

## Soluciones aplicadas

- Se crearon los archivos `pytest.ini` y `mypy.ini` mapeando las rutas exactas de cada actividad (ej. `src/semana_1/dia_05_viernes/uart_driver`).
- Se eliminaron los archivos `__init__.py` redundantes dentro de las subcarpetas de las actividades para evitar que Mypy las tratara como paquetes conflictivos.
- Se añadió el comentario `# type: ignore` en las líneas intencionalmente incorrectas (ejemplo LSP) y se ajustó el código con condicionales para resolver los riesgos de tipo `None`.

## Aprendizajes del día

- Es crucial configurar correctamente las herramientas de testing y análisis estático en proyectos con múltiples subdirectorios mediante archivos `.ini`.
- Los nombres de carpetas en Python deben utilizar *snake_case* (guiones bajos) en lugar de guiones medios para ser reconocidos correctamente por las herramientas del ecosistema.
- `mypy` es una herramienta excepcionalmente estricta y valiosa; no solo verifica sintaxis, sino que previene *crashes* en producción al obligar a manejar tipos opcionales (`None`) y respetar firmas de herencia.

## Evidencias

- Captura de la terminal limpia tras ejecutar `ruff check`.
- Captura de la ejecución de `pytest` mostrando los tests en verde y la tabla de cobertura superando el 70%.
- Captura de la terminal limpia (0 issues) tras la ejecución y corrección de `mypy`.

## Estado final

- Semana 1 concluida exitosamente. El repositorio cumple con todos los requisitos de arquitectura, pruebas aisladas, validación de calidad y documentación exigidos por la rúbrica del curso.