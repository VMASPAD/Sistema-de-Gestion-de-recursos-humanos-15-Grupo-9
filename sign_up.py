
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

import re 
from dataset import usuarios

#Funciones
def verificar_usuario(usuarios):
    usernames = {usuarios[i]["username"] for i in range(len(usuarios))}
    try:
        tag = input(MAGENTA + "Ingrese su nombre de usuario: " + RESET)
    except ValueError:
        print(ROJO + "Entrada inválida. Por favor, ingrese un nombre de usuario válido." + RESET)
        return verificar_usuario(usuarios)
    while tag in usernames:
        print(ROJO + "El usuario ya existe, por favor ingrese otro." + RESET)
        try:
            tag = input(MAGENTA + "Ingrese su nombre de usuario: " + RESET)
        except ValueError:
            print(ROJO + "Entrada inválida. Por favor, ingrese un nombre de usuario válido." + RESET)
            return verificar_usuario(usuarios)
    return tag.strip()

def generar_contraseña():
    try:
        password = input(MAGENTA + "Ingrese su contraseña, (debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número): " + RESET)
    except ValueError:
        print(ROJO + "Entrada inválida. Por favor, ingrese una contraseña válida." + RESET)
        return generar_contraseña()
    patron1 = re.compile("[A-Za-z0-9]{8,}")
    patron2 = re.compile("[A-Z]{1,}")
    patron3 = re.compile("[a-z]{1,}")
    patron4 = re.compile("[0-9]{1,}")
    while not patron1.match(password) or not patron2.search(password) or not patron3.search(password) or not patron4.search(password):
        print(ROJO + "Contraseña no válida." + RESET)
        password = input(MAGENTA + "Ingrese su contraseña, (debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número): " + RESET)
    return password.strip()

def verificar_dni():
    dni_ensistema = {usuarios[i]["dni"] for i in range(len(usuarios))}
    try:
        dni=input(MAGENTA + "ingrese el dni: " + RESET)
    except ValueError:
        print(ROJO + "Entrada inválida. Por favor, ingrese un DNI válido." + RESET)
        return verificar_dni()
    patron= re.compile('[0-9]{7,9}')
    while not patron.match(dni) or dni in dni_ensistema:
        if dni in dni_ensistema:
            print(ROJO + "El dni ya existe en el sistema, por favor ingrese otro." + RESET)
        else:
            print(ROJO + "dni invalido" + RESET)
        dni=input(MAGENTA + "ingrese su dni (debe contener de 7 a 9 numeros): " + RESET)
    return dni

def asignar_nivel_acceso():
    niveles = { 1 : "admin", 2 : "user", 3 : "guest"}
    print(AZUL + "Niveles de acceso disponibles" + RESET)
    for key, value in niveles.items():
        print(CIAN + f"{key} - {value}" + RESET)
    try:
        opcion = int(input(MAGENTA + "Seleccione el nivel de acceso (1-3): " + RESET))
    except ValueError:
        print(ROJO + "Entrada inválida. Por favor, ingrese un número válido." + RESET)
        return asignar_nivel_acceso()
    return niveles.get(opcion)


def crear_usuario(usuarios):
    username = verificar_usuario(usuarios)
    password = generar_contraseña()
    dni = verificar_dni()
    nivel_acceso = asignar_nivel_acceso()
    email = username + "@empresa.com"
    id = len(usuarios)
    print(VERDE + f"Usuario creado exitosamente:\nID: {id}\nUsername: {username}\nPassword: {password}\nDNI: {dni}\nNivel de acceso: {nivel_acceso}\nEmail: {email}" + RESET)
    usuarios.append({"id": id, "username": username, "password": password, "dni": dni, "nivel_acceso": nivel_acceso, "email": email, "estado": "Activo"})


if __name__ == "__main__":
    crear_usuario(usuarios)
    print(usuarios)