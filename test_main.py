import pytest
import json
from idGenerator import generar_id
from CRUD.registrar import Ingresar_Numero
from CRUD.buscador import Id_Empleado
from account import userLog
from sign_up import generar_contraseña

# Funciones auxiliares para leer archivos
def leer_usuarios():
    try:
        with open("dataset/usuarios.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def leer_empleados():
    empleados = []
    try:
        with open("Matrices/empleados.csv", "r", encoding="utf-8") as f:
            next(f, None)
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                if len(datos) >= 6:
                    datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                    datos[4] = int(datos[4]) if datos[4].isdigit() else datos[4]
                empleados.append(datos)
    except FileNotFoundError:
        pass
    return empleados

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
    matriz = leer_usuarios()
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
    usuarios = leer_usuarios()
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
    empleado = "Martin Sosa"
    #Act 
    id = Id_Empleado(empleado)
    #Assert
    assert id == 5
