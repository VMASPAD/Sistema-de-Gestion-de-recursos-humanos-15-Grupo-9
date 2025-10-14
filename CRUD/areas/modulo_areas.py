
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada
from estadisticas import promedio_empleados_por_area
from CRUD.registrar import Ingresar_Numero, verificar_area
from CRUD.buscador import Encontrar
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import areas, empleados, licencias
#Funciones 

#Registrar Area
def RegistrarArea(areas):
    nueva_area = []
    nombre_area = verificar_area()
    cantidad_empleados = 0
    A = [generar_id(areas), nombre_area, cantidad_empleados, "Activo"]
    nueva_area.extend(A)
    areas.append(nueva_area)
    return areas

def EstadisticasAreas(areas):
    print(AZUL + "="*43 + RESET)
    print(AZUL + "MENU PRINCIPAL -> AREAS -> ESTADISTICAS" + RESET)
    print(AZUL + "="*43 + RESET)
    print(CIAN + "| Opciones:".ljust(42) + "|" + RESET)
    print(CIAN + "| 1 - Ver promedio de empleados por area".ljust(42) + "|" + RESET)
    print(CIAN + "| 0 - Volver".ljust(42) + "|" + RESET)
    print(AZUL + "="*43 + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
    match opcion:
        case 1:
            promedio_empleados_por_area(empleados, areas)
        case 0:
            return
        case _:
            print(AMARILLO + "Opcion no valida." + RESET)
            print(AZUL + "="*130 + RESET)
            print()
            print(VERDE + "ESTADISTICAS FINALIZADAS" + RESET)
            print(AZUL + "="*130 + RESET)
    
#Buscar Area
def BuscarArea(areas):
    print(AZUL + "MENU PRINCIPAL -> AREAS -> BUSCADOR" + RESET)
    print(AZUL + "="*34 + RESET)
    print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
    print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
    print(CIAN + "| 2 - Nombre".ljust(33) + "|" + RESET)
    print(CIAN + "| 3 - Mostrar areas".ljust(33) + "|" + RESET)
    print(CIAN + "| 4 - Volver".ljust(33) + "|" + RESET)
    print(AZUL + "="*34 + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
    print()
    match opcion:
        case 1:
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
            Encontrar(busqueda, areas, 0, 1)
        case 2:
            busqueda = input(MAGENTA + "Ingrese el nombre a buscar: " + RESET)
            busqueda = busqueda.lower()
            Encontrar(busqueda, areas, 1, 1)
        case 3:
            key = lambda fila : fila[0]
            Imprimir_Matriz_Ordenada(areas, 1, key)
        case 4:
            return 
        
#Editar Area
def EditarArea():
    print(AZUL + "="*26 + RESET)
    index = input(MAGENTA + 'Escriba el id de la area a editar: ' + RESET)
    index = int(index)
    if index < len(areas) and index >= 0:
        print(AZUL + "Que campo quiere editar?" + RESET)
        print(CIAN + '1. Nombre' + RESET)
        print(CIAN + '2. Cantidad' + RESET)
        valueTochange = Ingresar_Numero(MAGENTA + 'Seleccione una opcion: ' + RESET)
        for i in range(len(areas)):
            if areas[i][0] == index:
                print(CIAN + f"Area encontrada: {areas[i]}" + RESET)
        if valueTochange == 1:
            newName = input(MAGENTA + 'Ingrese el nuevo nombre: ' + RESET)
            areas[index][1] = newName
            print(VERDE + f"Area actualizada: {areas[index]}" + RESET)
        elif valueTochange == 2:
            newCantidad = Ingresar_Numero(MAGENTA + 'Ingrese la nueva cantidad: ' + RESET)
            areas[index][2] = newCantidad
            print(VERDE + f"Area actualizada: {areas[index]}" + RESET)
    else: print(ROJO + "El id ingresado no es valido" + RESET)
    
#Eliminar Area
def EliminarArea():
    print(AZUL + "="*26 + RESET)
    areaEliminar = str(input(MAGENTA + "Escriba el nombre del area o escriba \"Lista\" para obtener la planilla: " + RESET)).lower()
    if areaEliminar == "lista":
        print(AZUL + "Lista de areas:" + RESET)
        Imprimir_Matriz_Ordenada(areas, 1, lambda fila: fila[0])
    elif areaEliminar in [area[1].lower() for area in areas]:
        posicion_area = areas[[area[1].lower() for area in areas].index(areaEliminar)]
        areas[posicion_area[0]][3] = "Inactivo"
        Eliminar_ClaveForanea(posicion_area[0], empleados, 4)
        id_empleados_afectados = [empleado[0] for empleado in empleados if empleado[4] == posicion_area[0]]
        for empleado_id in id_empleados_afectados:
            Eliminar_ClaveForanea(empleado_id, licencias, 1)
        print(VERDE + f"Area con id {areaEliminar} eliminada." + RESET)
    else:
        print(ROJO + f"Area {areaEliminar} no encontrada." + RESET)
    

if __name__ == "__main__":
    RegistrarArea(areas)