from src.Armando_Clemente_pg2_tecba.core import Persona

import pytest

def test_crear_persona_con_datos_validos():
    """Prueba que un objeto Persona se puede crear correctamente."""
    persona = Persona(
        nombre="Juan Perez",
        edad=30,
        documento="1234567",
        email="juan.perez@example.com",
        celular="12345678",
        direccion="Calle Falsa 123"
    )
    
    # Usa la aserción nativa de Python
    assert persona._nombre == "Juan Perez"
    assert persona._edad == 30
    assert persona._documento == "1234567"
    assert persona._email == "juan.perez@example.com"
    assert persona._celular == "12345678"
    assert persona._direccion == "Calle Falsa 123"

def test_validar_celular_valido():
    """Prueba la validación de celular válido."""
    persona = Persona()
    resultado = persona.set_celular("12345678")
    assert resultado is not None
    assert persona._celular == "12345678"

def test_validar_celular_invalido():
    """Prueba la validación de celular inválido."""
    persona = Persona()
    with pytest.raises(ValueError):
        persona.set_celular("123")  # Muy corto

def test_metodo_build_devuelve_diccionario():
    """Prueba que el método build() devuelve un diccionario."""
    persona = Persona(
        nombre="Ana Garcia",
        edad=25,
        documento="7654321",
        email="ana.garcia@example.com",
        celular="87654321",
        direccion="Avenida Principal 456"
    )
    
    resultado = persona.build()
    esperado = {
        "nombre": "Ana Garcia",
        "edad": 25,
        "documento": "7654321",
        "email": "ana.garcia@example.com",
        "celular": "87654321",
        "direccion": "Avenida Principal 456"
    }
    
    assert resultado == esperado

def test_validar_nombre_valido():
    """Prueba la validación de nombre válido."""
    persona = Persona()
    resultado = persona.set_nombre("Juan Perez")
    assert resultado is not None
    assert persona._nombre == "Juan Perez"

def test_validar_nombre_invalido():
    """Prueba la validación de nombre inválido."""
    persona = Persona()
    with pytest.raises(ValueError):
        persona.set_nombre("Juan123")  # Contiene números

def test_validar_edad_valida():
    """Prueba la validación de edad válida."""
    persona = Persona()
    resultado = persona.set_edad("25")
    assert resultado is not None
    assert persona._edad == 25

def test_validar_edad_invalida():
    """Prueba la validación de edad inválida."""
    persona = Persona()
    with pytest.raises(ValueError):
        persona.set_edad("150")  # Muy alta

def test_validar_email_valido():
    """Prueba la validación de email válido."""
    persona = Persona()
    resultado = persona.set_email("test@example.com")
    assert resultado is not None
    assert persona._email == "test@example.com"

def test_validar_email_invalido():
    """Prueba la validación de email inválido."""
    persona = Persona()
    with pytest.raises(ValueError):
        persona.set_email("email_invalido")  # Sin @