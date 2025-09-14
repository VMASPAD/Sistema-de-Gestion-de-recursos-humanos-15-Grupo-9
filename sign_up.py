import re 
from dataset import usuarios

#Funciones
def verificar_usuario(usuarios):
    tag = input("Ingrese su nombre de usuario: ")
    while tag in [usuarios[i]["username"] for i in range(len(usuarios))]:
        print("El usuario ya existe, por favor ingrese otro.")
        tag = input("Ingrese su nombre de usuario: ")
    return tag

def generar_contraseña():
    password = input("Ingrese su contraseña, (debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número): ")
    patron1 = re.compile("[A-Za-z0-9]{8,}")
    patron2 = re.compile("[A-Z]{1,}")
    patron3 = re.compile("[a-z]{1,}")
    patron4 = re.compile("[0-9]{1,}")
    while not patron1.match(password) or not patron2.search(password) or not patron3.search(password) or not patron4.search(password):
        print("Contraseña no válida.")
        password = input("Ingrese su contraseña, (debe contener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número): ")
    return password

def verificar_dni():
    dni=input("ingrese el dni: ")
    patron= re.compile('[0-9]{7,9}')
    while not patron.match(dni):
        print("dni invalido")
        dni=input("ingrese su dni (debe contener de 7 a 9 numeros): ")
    return dni

def asignar_nivel_acceso():
    niveles = { 1 : "admin", 2 : "user", 3 : "guest"}
    print("Niveles de acceso disponibles")
    for key, value in niveles.items():
        print(f"{key} - {value}")
    opcion = int(input("Seleccione el nivel de acceso (1-3): "))
    return niveles.get(opcion)


def crear_usuario(usuarios):
    username = verificar_usuario(usuarios)
    password = generar_contraseña()
    dni = verificar_dni()
    nivel_acceso = asignar_nivel_acceso()
    email = username + "@empresa.com"
    id = len(usuarios)
    print(f"Usuario creado exitosamente:\nID: {id}\nUsername: {username}\nPassword: {password}\nDNI: {dni}\nNivel de acceso: {nivel_acceso}\nEmail: {email}")
    usuarios.append({"id": id, "username": username, "password": password, "dni": dni, "nivel_acceso": nivel_acceso, "email": email, "estado": "activo"})


if __name__ == "__main__":
    crear_usuario(usuarios)
    print(usuarios)