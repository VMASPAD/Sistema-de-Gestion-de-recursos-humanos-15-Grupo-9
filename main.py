from account import userLog
from CRUD import registrar, buscador, editar, eliminar
from dataset import empleados, areas
#region Menu
def Menu():
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    print()
    nivel_acceso = userLog(user, password)
    match nivel_acceso:
        case 2:
            opcion = int(input("Seleccione una opcion: "))
            while opcion != 5: 
                if opcion == 1:
                    registrar.Registrar()
                if opcion == 2:
                    buscador.Buscador(empleados, areas)
                if opcion == 3:
                    editar.Editar()
                if opcion == 4:
                    eliminar.Eliminar()
                # if opcion == 5:
                #     print("-"*26)
                #     return 0
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
        case 1:
            opcion = int(input("Seleccione una opcion: "))
            while opcion != 4:
                if opcion == 1:
                    registrar.Registrar()
                if opcion == 2:
                    buscador.Buscador(empleados, areas)
                if opcion == 3:
                    editar.Editar()
                # if opcion == 4:
                #     print("-"*26)
                #     return 0
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
        case 0:
            opcion = int(input("Seleccione una opcion: "))
            while opcion != 2:
                if opcion == 1:
                    buscador.Buscador(empleados, areas)
                # if opcion == 2:
                #     print("-"*26)
                #     return 0
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
    print("-"*26)
    return 0
                
#Programa principal
if __name__ == "__main__":

    Menu()