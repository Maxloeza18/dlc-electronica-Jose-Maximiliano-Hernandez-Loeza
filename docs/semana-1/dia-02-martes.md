# Día 02 - Martes

## Objetivo del día

Desarrollar una nueva actividad basada en máquinas de estados finitas, reutilizando los conceptos trabajados el día anterior, pero ahora con una implementación orientada a objetos y con pruebas separadas por archivo dentro de una subcarpeta dedicada. También se debía validar el código con ruff y pytest antes de preparar el commit.

## Actividades realizadas

-Revisé la consigna del día a partir de la imagen proporcionada.
-Reimplementé la máquina de estados finita del semáforo usando una clase orientada a objetos.
-Definí TrafficLightState con Enum.
-Definí TrafficLightFSM con estado interno encapsulado.
-Implementé el estado inicial en RED.
-Programé la transición cíclica:
RED -> GREEN
GREEN -> YELLOW
YELLOW -> RED
-Agregué el contador de ciclos completos.
-Organicé los tests en una subcarpeta pruebas/, separando cada validación en su propio archivo.
-Creé pruebas individuales para:
estado inicial,
transición de RED a GREEN,
ciclo completo,
conteo de ciclos.
-Ejecuté la verificación de calidad con ruff check ..
-Ejecuté las pruebas con python -m pytest pruebas/.
-Confirmé que las 4 pruebas pasaron correctamente.

## Problemas encontrados

-pytest no aparecía como comando disponible de forma directa en el entorno, aunque el proyecto sí estaba bien estructurado.
-Fue necesario ajustar el comando de ejecución para usar python -m pytest en lugar de pytest directo.
-También se detectó que era importante correr primero la verificación de calidad antes de ejecutar los tests, para mantener un flujo ordenado de trabajo.
-Soluciones aplicadas
-Se corrigió la ruta de acceso al proyecto y se trabajó desde el directorio correcto.
-Se validó el código con ruff antes de correr las pruebas.
-Se cambió la ejecución de pruebas a:
python -m pytest pruebas/
-Se confirmó que el código estaba correcto y que los tests pasaban sin errores.
-Se mantuvo una organización clara del proyecto usando una carpeta específica para pruebas.

## Aprendizajes del día
-Las máquinas de estados finitas pueden modelarse de forma clara usando Enum y una clase con estado interno.
-Separar los tests en archivos individuales ayuda a mantener el proyecto ordenado.
-Antes de ejecutar pruebas, conviene revisar calidad con herramientas como ruff.
-En algunos entornos es mejor usar python -m pytest en lugar de pytest directo.
-La estructura de carpetas influye bastante en la facilidad de trabajo y en la ejecución correcta de comandos.
-El flujo correcto de desarrollo fue: escribir código, validar calidad, ejecutar pruebas y luego preparar el commit.

# Evidencias

-Captura de la estructura de carpetas del proyecto.
-Captura de la ejecución de ruff check ..
-Captura de la ejecución de python -m pytest pruebas/.
-Captura del resultado con 4 passed.
-Archivos creados para la FSM y los tests separados.

# Estado final

-Se completó la actividad del martes correctamente. El proyecto quedó estructurado con el archivo principal de la FSM y los tests separados dentro de la carpeta pruebas/, pasando tanto la verificación de calidad como las pruebas automáticas. El siguiente paso es documentar la actividad y preparar el commit correspondiente.