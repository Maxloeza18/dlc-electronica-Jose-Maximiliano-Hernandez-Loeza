# Día 04 - Jueves

## Objetivo del día

Completar el estudio de los principios SOLID aplicando los dos últimos: el Principio de Segregación de Interfaces (ISP) y el Principio de Inversión de Dependencias (DIP). El objetivo práctico fue refactorizar una "interfaz gorda" en interfaces más pequeñas (ISP) y utilizar inyección de dependencias a través de un `Protocol` para desacoplar la lógica de negocio de la persistencia de datos, permitiendo así crear tests usando repositorios en memoria.

## Actividades realizadas

- Creé la estructura de carpetas requerida en la ruta `src/semana-1/dia-04-jueves/actividad-01/`.
- Creé el archivo `notes.md` para documentar la teoría, además de los archivos de código principal (`solid_isp_dip.py`) y de pruebas (`test_solid_isp_dip.py`).
- Implementé el código para ISP dividiendo comportamientos generales en interfaces específicas (`Readable`, `Writable`, `Calibratable`).
- Implementé el código para DIP utilizando `Protocol` para definir la abstracción `DataRepository`, permitiendo inyectar esta dependencia en la clase `DataProcessor`.
- Escribí las pruebas unitarias que simulan un entorno de producción usando una clase `InMemoryRepository`, confirmando la utilidad del DIP para el testing.
- Agregué el bloque de ejecución `if __name__ == '__main__':` en el archivo principal para poder instanciar las clases e imprimir resultados directamente en la consola.
- Ejecuté exitosamente la verificación de calidad estática y las pruebas unitarias.

## Problemas encontrados

- Al intentar ejecutar `ruff`, `pytest` o el script de Python, la terminal no reconocía los comandos o arrojaba errores al no encontrar los archivos. Esto se debió a estar ejecutando los comandos de manera directa estando fuera de la raíz del proyecto o sin el enlace correcto del entorno virtual para las subcarpetas profundas.

## Soluciones aplicadas

- Me aseguré de posicionar la terminal en la raíz absoluta del proyecto y de verificar que el entorno virtual `(.venv)` estuviera activo.
- Cambié la estrategia de ejecución utilizando el módulo de Python (`python -m`) para asegurar que el entorno detectara correctamente las dependencias globales y las rutas.
- Comandos corregidos que solucionaron el problema:
  - `python -m ruff check src/semana-1/dia-04-jueves/actividad-01/`
  - `python -m pytest src/semana-1/dia-04-jueves/actividad-01/ -v`
  - `python src/semana-1/dia-04-jueves/actividad-01/solid_isp_dip.py`

## Aprendizajes del día

- ISP: Forzar a un cliente a depender de interfaces que no utiliza genera código frágil. Es mejor tener muchas interfaces pequeñas y específicas que una sola interfaz grande y de propósito general.
- DIP:Los módulos de alto nivel no deben depender de los módulos de bajo nivel; ambos deben depender de abstracciones. Utilizar la inyección de dependencias hace que el código sea infinitamente más fácil de probar, ya que podemos intercambiar bases de datos reales por "falsas" (en memoria) sin alterar el procesador de datos.

## Evidencias

- Captura de la ejecución exitosa del script en la terminal (impresión en consola).
- Captura del análisis de calidad limpio con `ruff check`.
- Captura de la ejecución con `pytest -v` mostrando todos los tests en verde (PASSED).

## Estado final

- Se completó la actividad del jueves correctamente. El código comprende los principios de ISP y DIP, está completamente testeado y se han superado los problemas de ejecución del entorno. Listo para empaquetar todo y realizar el commit final del día.