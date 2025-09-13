from dataset import usuarios
from CRUD.buscador import Encontrar_diccionario
from impresion import Imprimir_Diccionario_Ordenada, Imprimir_Matriz_Ordenada   
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


if __name__ == "__main__":
    Imprimir_Diccionario_Ordenada(usuarios, "id")
    