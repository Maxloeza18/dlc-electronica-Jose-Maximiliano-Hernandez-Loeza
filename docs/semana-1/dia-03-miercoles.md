# Día 03 - Miércoles

## Objetivo del día

Desarrollar la implementación práctica de los tres primeros principios SOLID (Single Responsibility, Open/Closed, y Liskov Substitution). La actividad principal se centra en un dominio de sensores, aplicando ejemplos de "mal" y "buen" diseño, respaldados por pruebas unitarias. Adicionalmente, validar la calidad del código y la ejecución de los tests antes de preparar el commit, reforzando el aprendizaje con un segundo dominio práctico (Smart Home).

## Actividades realizadas

- Revisé la consigna del día para implementar los principios S, O y L
- Creé la estructura de carpetas correspondiente al día de hoy dentro de `src/semana-1/dia-03-miercoles/'.
- Implementé el archivo `solid_srp_ocp_lsp.py` con el dominio de sensores, demostrando el contraste entre un diseño acoplado y uno basado en responsabilidades separadas e interfaces.
- Desarrollé 6 pruebas unitarias en `test_solid.py` (2 por cada principio) para validar el comportamiento del diseño correcto.
- Ejecuté la verificación de estilo y calidad con `ruff check src/semana-1/dia-03-miercoles/`.
- Corrí las pruebas unitarias detalladas usando `pytest src/semana-1/dia-03-miercoles/ -v` para obtener el desglose por test.
- Desarrollé una segunda actividad (Actividad 02) para aplicar los mismos principios SOLID en un dominio de un Sistema de Hogar Inteligente (Smart Home).
- Escribí el código para rutinas y dispositivos inteligentes en `actividad_02_solid.py` y sus respectivos tests en `test_actividad_02.py`.

## Problemas encontrados

- Era importante asegurar el orden de las validaciones locales (ruff y pytest) antes de realizar cualquier commit al repositorio, para evitar subir código con errores.
- **Soluciones aplicadas:**
  - Posponer el comando de commit que marcaba la guía original[cite: 19].
  - Ejecutar primero el linter y después los tests en modo detallado (verbose) para tener capturas claras.
  - Agrupar los cambios de ambas actividades en un único commit al finalizar la sesión.

## Aprendizajes del día

- Es fundamental separar las responsabilidades (SRP) para evitar clases infladas (ej. separar lectura de sensor y guardado en DB).
- El principio Abierto/Cerrado (OCP) se facilita mucho utilizando clases abstractas (`ABC`), permitiendo agregar nuevas lógicas (como alertas o rutinas) sin modificar el código que ya funciona.
- El principio de Sustitución de Liskov (LSP) exige que al usar herencia, la clase hija debe poder usarse exactamente igual que la clase padre sin romper el comportamiento esperado de la aplicación.
- Incorporar la bandera `-v` en Pytest permite observar individualmente el éxito de cada prueba, ideal para generar evidencias detalladas.

## Evidencias

- Captura de la estructura de carpetas del proyecto.
- Captura de la terminal limpia tras ejecutar `ruff check`.
- Captura de la ejecución de `pytest -v` con los tests aprobados (PASSED) en verde.
- Archivos `.py` creados para ambas actividades y sus respectivos tests.

## Estado final

- Se completaron y verificaron exitosamente ambas prácticas de los principios SOLID. Los archivos están listos, evaluados estáticamente y con pruebas pasando. El paso final es realizar el `git add`, `git commit` y `git push` para registrar el avance de este día en el repositorio.