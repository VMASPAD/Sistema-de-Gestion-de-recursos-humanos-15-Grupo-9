from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada
from CRUD.buscador import Encontrar
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import areas, empleados, licencias
#Funciones 

#Registrar Area
def RegistrarArea(areas):
    nueva_area = []
    nombre_area = input("Ingrese el nombre del área: ")
    cantidad_empleados = 0
    A = [generar_id(areas), nombre_area, cantidad_empleados, "Activo"]
    nueva_area.extend(A)
    areas.append(nueva_area)
    return areas

#Buscar Area
def BuscarArea(areas):
    print("MENU PRINCIPAL -> AREAS -> BUSCADOR")
    print("="*34)
    print("| Opciones:".ljust(33) + "|")
    print("| 1 - Id".ljust(33) + "|")
    print("| 2 - Nombre".ljust(33) + "|")
    print("| 3 - Mostrar areas".ljust(33) + "|")
    print("| 4 - Volver".ljust(33) + "|")
    print("="*34)
    opcion = int(input("Ingrese la opcion de busqueda: "))
    print()
    match opcion:
        case 1:
            busqueda = int(input("Ingrese el Id a buscar: "))
            Encontrar(busqueda, areas, 0, 1)
        case 2:
            busqueda = input("Ingrese el nombre a buscar: ")
            busqueda = busqueda.lower()
            Encontrar(busqueda, areas, 1, 1)
        case 3:
            key = lambda fila : fila[0]
            Imprimir_Matriz_Ordenada(areas, 1, key)
        case 4:
            return 
        
#Editar Area
def EditarArea():
    print("="*26)
    index = input('Escriba el id de la area a editar: ')
    index = int(index)
    if index < len(areas) and index >= 0:
        print("Que campo quiere editar?")
        print('1. Nombre')
        print('2. Cantidad')
        valueTochange = int(input('Seleccione una opcion: '))
        for i in range(len(areas)):
            if areas[i][0] == index:
                print(f"Area encontrada: {areas[i]}")
        if valueTochange == 1:
            newName = input('Ingrese el nuevo nombre: ')
            areas[index][1] = newName
            print(f"Area actualizada: {areas[index]}")
        elif valueTochange == 2:
            newCantidad = input('Ingrese la nueva cantidad: ')
            areas[index][2] = newCantidad
            print(f"Area actualizada: {areas[index]}")
    else: print("El id ingresado no es valido")
    
#Eliminar Area
def EliminarArea():
    print("="*26)
    areaEliminar = str(input("Escriba el nombre del area: ")).lower()
    if areaEliminar == "lista":
        print("Lista de areas:")
        Imprimir_Matriz_Ordenada(areas, 1, lambda fila: fila[0])
    elif areaEliminar in [area[1].lower() for area in areas]:
        posicion_area = areas[[area[1].lower() for area in areas].index(areaEliminar)]
        areas[posicion_area[0]][3] = "Inactivo"
        Eliminar_ClaveForanea(posicion_area[0], empleados, 4)
        id_empleados_afectados = [empleado[0] for empleado in empleados if empleado[4] == posicion_area[0]]
        for empleado_id in id_empleados_afectados:
            Eliminar_ClaveForanea(empleado_id, licencias, 1)
        print(f"Area con id {areaEliminar} eliminada.")
    else:
        print(f"Area {areaEliminar} no encontrada.")