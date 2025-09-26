# src/Armando_Clemente_pg2_tecba/validators.py
import re

class ValidadorBase:
    def validar_solo_numeros(self, valor: str) -> bool:
        return valor.isdigit()

    def validar_solo_letras(self, valor: str) -> bool:
        return valor.isalpha()

    def validar_alfanumerico(self, valor: str) -> bool:
        return valor.isalnum()


class ValidadorDatosPersonales(ValidadorBase):
    def validar_edad(self, edad: str) -> bool:
        return self.validar_solo_numeros(edad) and 0 < int(edad) < 120

    def validar_nombre(self, nombre: str) -> bool:
        return self.validar_solo_letras(nombre.replace(" ", ""))

    def validar_documento_identidad(self, doc: str) -> bool:
        return self.validar_alfanumerico(doc)


class ValidadorDatosContacto(ValidadorBase):
    def validar_email(self, email: str) -> bool:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email) is not None

    def validar_celular(self, celular: str) -> bool:
        return self.validar_solo_numeros(celular) and len(celular) in [8, 9]

    def validar_direccion(self, direccion: str) -> bool:
        return len(direccion.strip()) > 5
