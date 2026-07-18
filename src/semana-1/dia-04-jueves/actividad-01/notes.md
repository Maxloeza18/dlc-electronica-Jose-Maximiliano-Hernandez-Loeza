1. ISP (Interface Segregation Principle - Principio de Segregación de Interfaces)

El problema: Si se crea una clase o interfaz "gorda" llamada DispositivoElectrónico que obliga a tener los métodos read(), write(), calibrate() y reset(). Si se conecta un simple sensor analógico, este solo necesita read(). Obligarlo a heredar métodos inútiles como write() es mala práctica.

La solución (ISP): Dividir esa interfaz gigante en contratos más pequeños y específicos. En Python se usa Protocol de la librería typing para esto. Se crean contratos separados: Readable (para lo que se lee), Writable (para actuadores o pantallas) y Calibratable (para sensores complejos).

2. DIP (Dependency Inversion Principle - Principio de Inversión de Dependencias)

El problema: Si la clase DataProcessor crea internamente una conexión directa a PostgreSQL (broker), el código queda amarrado a esa base de datos. Si se probar el código rápidamente (hacer tests), tendrías que levantar Docker, correr PostgreSQL y borrar datos a cada rato.

La solución (DIP y la "Inyección de Dependencias"): DataProcessor no debe saber dónde se guardan los datos. Solo debe exigir que le pases un objeto que cumpla con el contrato DataRepository (que tenga un método save() y un get_latest()). Si se le pasa una base de datos real, lo guarda ahí; si se le pasa un diccionario en memoria RAM, lo guarda en la RAM. Al procesador le da igual.