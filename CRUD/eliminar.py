from dataset import empleados, areas, licencias
from CRUD.buscador import Imprimir_Matriz_Ordenada
def Eliminar(index):
    match index:
        case 1:
            EliminarArea()
        case 2:
            EliminarLicencia()
        case 3:
            EliminarEmpleado()
        case 4:
            return 0
        case _:
            print("Opcion no valida")
            print()
            return 0

def EliminarEmpleado():
    print("="*26)
    empleadoEliminar = input("Escriba el nombre y apellido del empleado o escriba \"Lista\" para obtener la planilla: ").lower()
    if empleadoEliminar == "lista":
        print("Lista de empleados:")
        Imprimir_Matriz_Ordenada(empleados, lambda fila: fila[0])
    elif empleadoEliminar in [empleado[1].lower() for empleado in empleados]:
        posicion_empleados = empleados[[empleado[1].lower() for empleado in empleados].index(empleadoEliminar)]
        # print(posicion_empleados)
        empleados[posicion_empleados[0]][5] = "Inactivo"
        Eliminar_ClaveForanea(posicion_empleados[0], licencias)
        print(f"Empleado {empleadoEliminar} eliminado.")
    else:
        print(f"Empleado {empleadoEliminar} no encontrado.")

def EliminarArea():
    print("="*26)
    areaEliminar = int(input("Escriba el id del area o escriba Lista para obtener la planilla: "))
    if areaEliminar == "Lista":
        print("Lista de areas:")
        Imprimir_Matriz_Ordenada(areas, 0, lambda fila: fila[0])
    else:
        del areas[areaEliminar]
        print(f"Area con id {areaEliminar} eliminada.")

def EliminarLicencia():
    print("="*26)
    licenciaEliminar = int(input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla"))
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
    else:
        del licencias[licenciaEliminar]
        print(f"Licencia con id {licenciaEliminar} eliminada.")

def Eliminar_ClaveForanea(id, matriz):
    for i in range(len(matriz)):
        if id in matriz[i]:
            posicion = matriz[i].index("Activo")
            matriz[i][posicion] = "Inactivo"
    return matriz

if __name__ == "__main__":
    Eliminar(3)