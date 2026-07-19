Al rediseñar un driver UART tradicional con Python moderno logre entender el enorme valor de la arquitectura limpia a través de los principios SOLID:

SRP (Single Responsibility): Se aplicó de manera estricta aislando responsabilidades. La clase UartConfig tiene como única responsabilidad contener y validar la configuración , mientras que DataRecorder se encarga exclusivamente de la persistencia de datos en archivos. Esto previene que los cambios en la lógica de guardado afecten al hardware.

OCP (Open/Closed): Gracias a la interfaz MessageParser, el sistema está abierto a la extensión. Si mañana requerimos soportar un nuevo protocolo (como CAN), podemos crear un nuevo parser heredando de la clase base sin tocar una sola línea del código existente.
* LSP (Liskov Substitution): Cualquier clase en el sistema que requiera procesar mensajes funciona perfectamente sin importar si le entregamos un ModbusParser o un NMEAParser, garantizando un comportamiento predecible.
* ISP (Interface Segregation): La interfaz MessageParser se diseñó pequeña y específica, obligando a las clases derivadas a implementar únicamente los métodos estrictamente necesarios (can_parse y parse).

DIP (Dependency Inversion): Fue el cambio más radical. La clase UartDevice ya no instancia sus propios parsers ni su configuración, sino que depende de abstracciones (la interfaz del parser y el objeto de configuración) inyectadas en su constructor. Esto fue clave para lograr aislar el sistema y permitió inyectar un "Parser Falso" (Mock) para realizar pruebas unitarias robustas sin depender de hardware real.