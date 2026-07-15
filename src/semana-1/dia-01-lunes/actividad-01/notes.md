Glosario de funciones

-Enum: sirve para representar opciones cerradas, como tipos de sensor (TEMPERATURE,HUMIDITY), evitando strings sueltos y errores de escritura

-@dataclass(frozen=true) : define objetos de datos inmutables, utiles cuando quieres representar una lectura sin modificar despues

-Protocol: define una interfaz por comportamiento, sin herencia forzada; cualquier objeto que tenga el metodo correcto puede cumplirla 

-to_frame(r: Reading) -> bytes : es un ejemplo de funcion pura, por que recibe datos, transforma y devuelve un resultado sin efectos colaterales