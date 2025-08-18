from account import userLog
from CRUD import registrar, buscador, editar, eliminar
#region Menu
def Menu():
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    nivel_acceso = userLog(user, password)
    match nivel_acceso:
        case 2:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                registrar.Registrar()
            if opcion == 2:
                buscador.Buscador()
            if opcion == 3:
                editar.Editar()
            if opcion == 4:
                eliminar.Eliminar()
            if opcion == 5:
                print("-"*26)
                return 0
            pass
        case 1:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                registrar.Registrar()
            if opcion == 2:
                buscador.Buscador()
            if opcion == 3:
                editar.Editar()
            if opcion == 4:
                print("-"*26)
                return 0
            pass
        case 0:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                editar.Buscador()
            if opcion == 2:
                print("-"*26)
                return 0
            pass
#Programa principal
if __name__ == "__main__":

    Menu()