import pytest
from CRUD.registrar import Ingresar_Numero, verificar_telefono
from impresion import Reemplazo_Id_Valor
from account import userLog
from sign_up import generar_contraseña 

# Funciones auxiliares para leer archivos

@pytest.fixture
def cuenta():
    user = "juanp"
    password = "juanp"
    return user, password

@pytest.fixture
def cuenta2():
    user = "maria.g"
    password = "mg2024"
    return user, password

def test_verificar_telefono():
    #Arrange
    codigo_area = "11"
    telefono = "62112344"

    #Act
    tel = verificar_telefono(codigo_area, telefono)

    #Assert
    assert tel == "+541162112344"

def test_ingreso_num():
    #Arrange
    numero = 90
    #Act, Assert
    assert Ingresar_Numero("ingresado", numero=numero) == numero


def test_userlog(cuenta, cuenta2):
    #Arrange
    user, password = cuenta
    user2, password2 = cuenta2

    #Act
    nivel_acceso = userLog(user, password)
    nivel_acceso2 = userLog(user2, password2)

    #Assert
    assert nivel_acceso == 2
    assert nivel_acceso2 == 1

def test_generar_contraseña():
    #Arrange 
    password = "Meeh2025"

    #Act, Assert
    assert generar_contraseña(password) == password 


def test_Reemplazo_Id_Valor():
    #Arrange 
    area = 6
    #Act 
    nombre = Reemplazo_Id_Valor(6, 4)
    #Assert
    assert nombre == "Compras"
