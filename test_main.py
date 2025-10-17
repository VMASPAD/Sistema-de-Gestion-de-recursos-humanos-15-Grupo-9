import pytest
from idGenerator import generar_id
from CRUD.registrar import Ingresar_Numero
from CRUD.buscador import Id_Empleado
from dataset import usuarios, empleados
from account import userLog
from sign_up import generar_contraseña

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

def test_generar_id():
    #Arrange
    matriz = usuarios
    #Act
    id = generar_id(matriz)
    #Assert
    assert id == len(matriz)

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
    nivel_acceso = userLog(usuarios, user, password)
    nivel_acceso2 = userLog(usuarios, user2, password2)

    #Assert
    assert nivel_acceso == 2
    assert nivel_acceso2 == 1

def test_generar_contraseña():
    #Arrange 
    password = "Meeh2025"

    #Act, Assert
    assert generar_contraseña(password) == password 


def test_id_empleado():
    #Arrange 
    matriz = empleados
    empleado = "Martin Sosa"
    #Act 
    id = Id_Empleado(matriz, empleado)
    #Assert
    assert id == 5
