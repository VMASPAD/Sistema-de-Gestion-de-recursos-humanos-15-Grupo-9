import re
from dataset import usuarios
from CRUD.buscador import Encontrar_diccionario
from impresion import Imprimir_Diccionario_Ordenada, Imprimir_Matriz_Ordenada, formato_dni   
from sign_up import verificar_usuario, generar_contraseña, asignar_nivel_acceso, verificar_dni

def buscar_usuarios(usuarios):
    print("MENU  PRINCIPAL -> USUARIOS -> BUSCADOR")            # id, username, password, dni, nivel_acceso, email
    print("="*34)
    print("|Opciones:" .ljust(33)+"|")
    print("| 1 - Id".ljust(33) + "|")
    print("| 2 - Username".ljust(33) + "|")
    print("| 3 - DNI".ljust(33) + "|")
    print("| 4 - Mail".ljust(33) + "|")
    print("| 5 - Nivel de Acceso".ljust(33) + "|")
    print("| 6 - Volver" .ljust(33)+"|")
    print("="*34)
    opcion=int(input("ingrese la opcion por la cual quiere buscar: ")) 
    print()
    match opcion:
        case 1:
            busqueda = int(input("ingrese el ID a buscar: "))
            Encontrar_diccionario(busqueda, usuarios, 0, 0)
            Imprimir_Diccionario_Ordenada(usuarios, 0, 0)
        case 2:
            busqueda = input("ingrese el Username")
            busqueda=busqueda.lower()
            Encontrar_diccionario(busqueda, usuarios, 1, 0)
            Imprimir_Diccionario_Ordenada(usuarios, 0, 1)
        case 3:
            busqueda = int(input("ingrese el DNI a buscar: "))
            Encontrar_diccionario(busqueda, usuarios, 3, 0)
            Imprimir_Diccionario_Ordenada(usuarios, 0, 3)
        case 4:
            busqueda = input("ingrese el Mail a buscar: ")
            busqueda=busqueda.lower()
            Encontrar_diccionario(busqueda, usuarios, 4, 0)
            Imprimir_Diccionario_Ordenada(usuarios, 0, 4 )
        case 5:
            busqueda = int(input("ingrese el Nivel de Acceso a buscar: "))
            Encontrar_diccionario(busqueda, usuarios, 5, 0)
            Imprimir_Diccionario_Ordenada(usuarios, 0, 5)
        case 6:
            print("Volviendo al menu principal...")
        case _:
            print("Opcion no valida.")
            print("="*130)
            print()
            print("BUSQUEDA FINALIZADA")
            print("="*130)

def eliminar_usuario(usuarios):
    print("="*26)
    usuarioEliminar = input("Escriba el id del usuario a eliminar: ")
    if usuarioEliminar in [str(fila["id"]) for fila in usuarios]:
        usuarioEliminar=int(usuarioEliminar)
        usuarios[usuarioEliminar]["estado"]= "Inactivo"
        print(f"usuario con id {usuarioEliminar} del usuario {usuarios[usuarioEliminar]["username"]} eliminado (Inactivo)")
    else:
        print(f"No se encontró un usuario con ID {usuarioEliminar}.")

def editar_usuario(usuarios):
    print("="*26)
    index=int(input("Escriba el id del usuario a editar: "))
    if index < len(usuarios) and index >=0:
        print("¿Que campo quiere editar?")
        print("1. username")
        print('2. password')
        print('3. dni')
        print('4. nivel acceso')
        campo = int(input("Seleccione el campo a editar (1-4): "))

        if campo == 1:
            username_pasado=usuarios[index]["username"]
            usuarios[index]["username"]=verificar_usuario(usuarios)
            print(f"el usuario {username_pasado} ha sido cambiado por {usuarios[index]["username"]}")

        if campo == 2:
            password_pasado=usuarios[index]["password"]
            usuarios[index]["password"]=generar_contraseña()
            patron = re.compile(usuarios[index]["password"])
            encriptar = patron.sub(usuarios[index]["password"][:3] + '*'*len(usuarios[index]["password"][3:]), usuarios[index]["password"])
            print(f"la contraseña anterior {password_pasado} ha sido cambiada por {encriptar}")

        if campo == 3:
            dni_pasado=formato_dni(usuarios[index]["dni"])
            usuarios[index]["dni"]= verificar_dni()
            dni_punteado=formato_dni(usuarios[index]["dni"])
            print(f"dni {dni_pasado} ha sido modificado a {dni_punteado}")



        if campo == 4:
            nivel_acceso_pasado=usuarios[index]["nivel_acceso"]
            usuarios[index]["nivel_acceso"]=asignar_nivel_acceso()
            print(f"el nivel de acceso de {usuarios[index]["username"]} ha sido modificado a {usuarios[index]["nivel_acceso"]}")
    else:
        print("Usuario no encontrado")

    return usuarios

if __name__ == "__main__":
    buscar_usuarios(usuarios)
