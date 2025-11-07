
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

import re
import json
from CRUD.registrar import Ingresar_Numero
from CRUD.buscador import Encontrar_diccionario
from impresion import Imprimir_Diccionario_Ordenada, formato_dni   
from sign_up import verificar_usuario, generar_contraseña, asignar_nivel_acceso, verificar_dni
from main import JSON_USUARIOS

def leer_usuarios():
    """Lee usuarios desde el archivo JSON."""
    try:
        with open(JSON_USUARIOS, "r", encoding="UTF-8") as usu:
            return json.load(usu)
    except (OSError, FileNotFoundError) as error:
        print(ROJO + "Error al leer usuarios:" + RESET, error)
        return []

def guardar_usuarios(usuarios):
    """Guarda usuarios en el archivo JSON."""
    try:
        with open(JSON_USUARIOS, "w", encoding="UTF-8") as usu:
            json.dump(usuarios, usu, ensure_ascii=False, indent=4)
        return True
    except (OSError, FileNotFoundError) as error:
        print(ROJO + "Error al guardar usuarios:" + RESET, error)
        return False

def buscar_usuarios():
    usuarios = leer_usuarios()
    if not usuarios:
        return
        
    print(AZUL + "MENU  PRINCIPAL -> USUARIOS -> BUSCADOR" + RESET)            # id, username, password, dni, nivel_acceso, email
    print(AZUL + "="*34 + RESET)
    print(CIAN + "|Opciones:" .ljust(33)+"|" + RESET)
    print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
    print(CIAN + "| 2 - Username".ljust(33) + "|" + RESET)
    print(CIAN + "| 3 - DNI".ljust(33) + "|" + RESET)
    print(CIAN + "| 4 - Mail".ljust(33) + "|" + RESET)
    print(CIAN + "| 5 - Nivel de Acceso".ljust(33) + "|" + RESET)
    print(CIAN + "| 6 - Volver" .ljust(33)+"|" + RESET)
    print(AZUL + "="*34 + RESET)
    opcion=Ingresar_Numero(MAGENTA + "ingrese la opcion por la cual quiere buscar: " + RESET)
    print()
    match opcion:
        case 1:
            busqueda = Ingresar_Numero(MAGENTA + "ingrese el ID a buscar: " + RESET)
            Encontrar_diccionario(busqueda, "id", 0)
        case 2:
            busqueda = input(MAGENTA + "ingrese el Username" + RESET)
            busqueda=busqueda.lower()
            Encontrar_diccionario(busqueda, "username", 0)
        case 3:
            busqueda = Ingresar_Numero(MAGENTA + "ingrese el DNI a buscar: " + RESET)
            Encontrar_diccionario(busqueda, "dni", 0)
        case 4:
            busqueda = input(MAGENTA + "ingrese el Mail a buscar: " + RESET)
            busqueda=busqueda.lower()
            Encontrar_diccionario(busqueda, "email", 0)
        case 5:
            busqueda = input(MAGENTA + "ingrese el Nivel de Acceso a buscar: " + RESET)
            Encontrar_diccionario(busqueda, "nivel_acceso", 0)
        case 6:
            print(CIAN + "Volviendo al menu principal..." + RESET)
        case _:
            print(AMARILLO + "Opcion no valida." + RESET)
            print(AZUL + "="*130 + RESET)
            print()
            print(VERDE + "BUSQUEDA FINALIZADA" + RESET)
            print(AZUL + "="*130 + RESET)

def eliminar_usuario():
    usuarios = leer_usuarios()
    if not usuarios:
        return
    
    print(AZUL + "="*26 + RESET)
    usuarioEliminar = input(MAGENTA + "Escriba el id del usuario a eliminar: " + RESET)
    if usuarioEliminar in [str(fila["id"]) for fila in usuarios]:
        usuarioEliminar=int(usuarioEliminar)
        usuarios[usuarioEliminar]["estado"]= "Inactivo"
        print(VERDE + f"usuario con id {usuarioEliminar} del usuario {usuarios[usuarioEliminar]['username']} eliminado (Inactivo)" + RESET)
        guardar_usuarios(usuarios)
    else:
        print(ROJO + f"No se encontró un usuario con ID {usuarioEliminar}." + RESET)

def editar_usuario():
    usuarios = leer_usuarios()
    if not usuarios:
        return
    
    print(AZUL + "="*26 + RESET)
    index=Ingresar_Numero(MAGENTA + "Escriba el id del usuario a editar: " + RESET)
    if index < len(usuarios) and index >=0:
        print(AZUL + "¿Que campo quiere editar?" + RESET)
        print(CIAN + "1. username" + RESET)
        print(CIAN + '2. password' + RESET)
        print(CIAN + '3. dni' + RESET)
        print(CIAN + '4. nivel acceso' + RESET)
        print(CIAN + '5. alta lógica')
        campo = Ingresar_Numero(MAGENTA + "Seleccione el campo a editar (1-4): " + RESET)

        if campo == 1:
            username_pasado=usuarios[index]["username"]
            usuarios[index]["username"]=verificar_usuario(usuarios)
            print(VERDE + f"el usuario {username_pasado} ha sido cambiado por {usuarios[index]['username']}" + RESET)

        if campo == 2:
            password_pasado=usuarios[index]["password"]
            usuarios[index]["password"]=generar_contraseña()
            patron = re.compile(usuarios[index]["password"])
            encriptar = patron.sub(usuarios[index]["password"][:3] + '*'*len(usuarios[index]["password"][3:]), usuarios[index]["password"])
            print(VERDE + f"la contraseña anterior {password_pasado} ha sido cambiada por {encriptar}" + RESET)

        if campo == 3:
            dni_pasado=formato_dni(usuarios[index]["dni"])
            usuarios[index]["dni"]= verificar_dni(usuarios)
            dni_punteado=formato_dni(usuarios[index]["dni"])
            print(VERDE + f"dni {dni_pasado} ha sido modificado a {dni_punteado}" + RESET)

        if campo == 4:
            nivel_acceso_pasado=usuarios[index]["nivel_acceso"]
            usuarios[index]["nivel_acceso"]=asignar_nivel_acceso()
            print(VERDE + f"el nivel de acceso de {usuarios[index]['username']} ha sido modificado de {nivel_acceso_pasado} a {usuarios[index]['nivel_acceso']}" + RESET)
        
        if campo == 5:
            usuarios[index]["estado"] = "Activo"
            print(VERDE + f"El usuario {usuarios[index]['username']} esta activo" + RESET)
        guardar_usuarios(usuarios)
    else:
        print(ROJO + "Usuario no encontrado" + RESET)

    return usuarios

if __name__ == "__main__":
    buscar_usuarios()
