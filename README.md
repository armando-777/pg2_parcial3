
#  Armando_Clemente_pg2_tecba

Librería en Python para validación de datos personales y de contacto usando el patrón Builder.  
P. Academico de Programación.



* Instalación desde PyPI 

```bash
pip install -i https://test.pypi.org/simple/ Armando-Clemente-pg2-tecba==0.0.2
``` 

* Instalación desde código fuente

```bash
# Clonar el repositorio
git clone https://github.com/armando-777/pg2_parcial3.git
cd src/colormixer

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias (ninguna requerida para funcionamiento básico)
pip install -r requirements.txt  # Solo para desarrollo/testing
```

# tests

```bash

python -m pytest tests/test_persona.py -v

```

# interfaces expuestas para la clase principal del módulo core.
Interfaces expuestas – Clase Persona (módulo core)

La clase Persona expone una serie de métodos que permiten construir objetos paso a paso aplicando validaciones en cada atributo.

set_nombre(nombre: str): permite asignar el nombre de la persona validando que contenga únicamente letras.

set_edad(edad: str): asigna la edad de la persona, validando que sea numérica y dentro de un rango válido.

set_documento(doc: str): establece el documento de identidad, asegurando que sea alfanumérico.

set_email(email: str): asigna el correo electrónico, verificando que cumpla con el formato estándar de email.

set_celular(celular: str): asigna el número de celular, validando que sea numérico y tenga la longitud adecuada.

set_direccion(direccion: str): asigna la dirección de la persona, validando que contenga caracteres alfanuméricos.

build(): construye el objeto final y devuelve un diccionario con todos los datos validados de la persona.

#  ejemplo de uso de la clase Persona

```bash
from Armando_Clemente_pg2_tecba.core import Persona

# Construcción de una persona con validaciones
persona = (
    Persona()
    .set_nombre("Armando")
    .set_edad("25")
    .set_documento("ABC12345")
    .set_email("armando@example.com")
    .set_celular("76543210")
    .set_direccion("Calle Falsa 123")
    .build()
)

print(persona)

```
salida esperada

```bash
{
    'nombre': 'Armando',
    'edad': 25,
    'documento': 'ABC12345',
    'email': 'armando@example.com',
    'celular': '76543210',
    'direccion': 'Calle Falsa 123'
}

```