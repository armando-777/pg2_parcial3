# src/Armando_Clemente_pg2_tecba/core.py
from .validators import ValidadorDatosPersonales, ValidadorDatosContacto

class Persona:
    def __init__(self):
        self._nombre = None
        self._edad = None
        self._documento = None
        self._email = None
        self._celular = None
        self._direccion = None

        self._val_personales = ValidadorDatosPersonales()
        self._val_contacto = ValidadorDatosContacto()

    # --- Métodos Builder para datos personales ---
    def set_nombre(self, nombre: str):
        if self._val_personales.validar_nombre(nombre):
            self._nombre = nombre
        else:
            raise ValueError("Nombre inválido, solo letras permitidas")
        return self

    def set_edad(self, edad: str):
        if self._val_personales.validar_edad(edad):
            self._edad = int(edad)
        else:
            raise ValueError("Edad inválida")
        return self

    def set_documento(self, doc: str):
        if self._val_personales.validar_documento_identidad(doc):
            self._documento = doc
        else:
            raise ValueError("Documento inválido")
        return self

    # --- Métodos Builder para datos de contacto ---
    def set_email(self, email: str):
        if self._val_contacto.validar_email(email):
            self._email = email
        else:
            raise ValueError("Email inválido")
        return self

    def set_celular(self, celular: str):
        if self._val_contacto.validar_celular(celular):
            self._celular = celular
        else:
            raise ValueError("Celular inválido")
        return self

    def set_direccion(self, direccion: str):
        if self._val_contacto.validar_direccion(direccion):
            self._direccion = direccion
        else:
            raise ValueError("Dirección inválida")
        return self

    
    def build(self):
        return {
            "nombre": self._nombre,
            "edad": self._edad,
            "documento": self._documento,
            "email": self._email,
            "celular": self._celular,
            "direccion": self._direccion,
        }
