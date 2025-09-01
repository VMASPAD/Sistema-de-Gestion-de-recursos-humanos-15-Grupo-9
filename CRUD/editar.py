from dataset import empleados, areas, licencias
from CRUD.buscador import Imprimir_Matriz_Ordenada

def Es_Entero(valor):
    if len(valor) == 0:
        return False
    i = 0
    if valor[0] == '-':
        if len(valor) == 1:
            return False
        i = 1
    while i < len(valor):
        c = valor[i]
        if c < '0' or c > '9':
            return False
        i += 1
    return True

def Editar(tipo):
    print("="*26)

    match tipo:
        case 1:
            EditarArea()
        case 2:
            EditarLicencias()
        case 3:
            index = input("Escriba el id del empleado a editar o escriba \"Ver\" para obtener toda la lista ")
            if index == "Ver":
                print("Lista de empleados:")
                Imprimir_Matriz_Ordenada(empleados, 0, lambda fila: fila[0])
            else:
                if Es_Entero(index):
                    index = int(index)
                    if index < len(empleados):
                        empleado = empleados[index]
                        print(f"Empleado encontrado: {empleado}")
                        print("Que campo quiere editar?")
                        print('1. Nombre')
                        print('2. Apellido')
                        print('3. Telefono')
                        print('4. Area')
                        print('5. Estado')
                        print('6. Fecha de ingreso')
                        print('7. Fecha de nacimiento')
                        campo = int(input("Seleccione el campo a editar (1-7): "))
                        nuevo_valor = input("Ingrese el nuevo valor: ")
                        empleado[campo] = nuevo_valor
                        print("Empleado actualizado:", empleado)
                    else:
                        print("Empleado no encontrado.")
                else:
                    print("Entrada inválida.")
        case 4:
            return 0
        case _:
            print("Opcion no valida")
            print()
            return 0


def EditarArea():
    print("="*26)
    index = input('Escriba el id de la area a editar o escriba \"Ver\" para obtener toda la lista: ')
    if index == "Ver":
        print('Ver todas las areas')
        Imprimir_Matriz_Ordenada(areas, 1, lambda fila: fila[0])
    elif Es_Entero(index):
        index = int(index)
        print("Que campo quiere editar?")
        print('1. Nombre')
        print('2. Cantidad')
        valueTochange = int(input('Seleccione una opcion: '))
        for i in range(len(areas)):
            if areas[i][0] == index:
                print(f"Area encontrada: {areas[i]}")
                if valueTochange == 1:
                    newName = input('Ingrese el nuevo nombre: ')
                    areas[i][1] = newName
                    print(f"Area actualizada: {areas[i]}")
                elif valueTochange == 2:
                    newCantidad = input('Ingrese la nueva cantidad: ')
                    areas[i][2] = newCantidad
                    print(f"Area actualizada: {areas[i]}")
                break
        else:
            print("Area no encontrada.")
    else:
        print("Entrada inválida.")

def EditarLicencias():
    print("="*26)
    index = input('Escriba el id de la licencia a editar o escriba \"Ver\" para obtener toda la lista: ')
    if index == "Ver":
        print('Todas las licencias')
        Imprimir_Matriz_Ordenada(licencias, 2, lambda fila: fila[0])
    elif Es_Entero(index):
        index = int(index)
        print("Que campo quiere editar?")
        print('1. Fecha')
        print('2. Empleado')
        valueTochange = int(input('Seleccione una opcion: '))
        for i in range(len(licencias)):
            if licencias[i][0] == index:
                print(f"Licencia encontrada: {licencias[i]}")
                if valueTochange == 1:
                    newFecha = input(f'Ingrese la nueva fecha (YEAR/DAY/MONTH): {licencias[i][2]}): ')
                    licencias[i][2] = newFecha
                    print(f"Licencia actualizada: {licencias[i]}")
                elif valueTochange == 2:
                    newEmpleado = input(f'Ingrese el nuevo id del empleado: {licencias[i][1]}: ')
                    licencias[i][1] = int(newEmpleado)
                    print(f"Licencia actualizada: {licencias[i]}")
                break
        else:
            print("Licencia no encontrada.")
    else:
        print("Entrada inválida.")