from account import userLog
from CRUD import registrar, buscador, editar, eliminar
from dataset import empleados, areas, licencias, usuarios
#region Menu
def Menu():
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    print()
    nivel_acceso = userLog(user, password, usuarios)
    match nivel_acceso:
        case 2:

            opcion = int(input("Seleccione una opcion: "))
            while opcion != 5: 
                
                if opcion == 0:
                    opcion = int(input("Seleccione una opcion xx: "))

                if opcion == 1:
                    print()
                    print("MENU PRINCIPAL -> REGISTRAR")
                    print("="*34)
                    print('| Que elemento quiere Registrar? |')
                    print('| 1. Area                        |')
                    print('| 2. Empleado                    |')
                    print('| 3. Volver                      |')
                    print("="*34)
                    tipo = int(input("Seleccione una opcion: "))
                    registrar.Registrar(tipo)

                if opcion == 2:
                    buscador.Buscador(empleados, areas, licencias)
                if opcion == 3:
                    print()
                    print("MENU PRINCIPAL -> EDITAR")
                    print("="*34)
                    print('| Que elemento quiere editar?    |')
                    print('| 1. Area                        |')
                    print('| 2. Licencia                    |')
                    print('| 3. Empleado                    |')
                    print('| 4. Volver                      |')
                    print("="*34)
                    tipo = int(input("Seleccione una opcion: "))
                    editar.Editar(tipo)
                if opcion == 4:
                    print()
                    print("MENU PRINCIPAL -> ELIMINAR")
                    print("="*34)
                    print('| Que elemento quiere eliminar?  |')
                    print('| 1. Area                        |')
                    print('| 2. Licencia                    |')
                    print('| 3. Empleado                    |')
                    print('| 4. Volver                      |')
                    print("="*34)
                    tipo = int(input("Seleccione una opcion: "))
                    eliminar.Eliminar(tipo)
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
        case 1:
            opcion = int(input("Seleccione una opcion: "))
            while opcion != 5: 
                if opcion == 1:
                    registrar.Registrar(2)
                if opcion == 2:
                    buscador.Buscador(empleados, areas, licencias)
                if opcion == 3:
                    print()
                    print("MENU PRINCIPAL -> EDITAR")
                    print("="*34)
                    print('| Que elemento quiere editar?    |')
                    print('| 2. Licencia                    |')
                    print('| 3. Empleado                    |')
                    print('| 4. Volver                      |')
                    print("="*34)
                    tipo = int(input("Seleccione una opcion: "))
                    editar.Editar(tipo)
                if opcion == 4:
                    eliminar.Eliminar(3)
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
        case 0:
            opcion = int(input("Seleccione una opcion: "))
            while opcion != 2:
                if opcion == 1:
                    buscador.Buscador(empleados, areas, licencias)
                userLog(user, password)
                opcion = int(input("Seleccione una opcion: "))
    print("-"*26)
    return 0
                
#Programa principal
if __name__ == "__main__":
    
    Menu()