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
    empleadoEliminar = input("Escriba el nombre y apellido del empleado o escriba \"Lista\" para obtener la planilla: ")
    if empleadoEliminar == "Lista":
        print("Lista de empleados:")
        Imprimir_Matriz_Ordenada(empleados, 0, lambda fila: fila[0])
    elif empleadoEliminar in [empleado[1] for empleado in empleados]:
        posicion_empleados = empleados[[empleado[1] for empleado in empleados].index(empleadoEliminar)]
        empleados[posicion_empleados[0]][5] = "Inactivo"
        print(f"Empleado {empleadoEliminar} eliminado.")
    else:
        print(f"Empleado {empleadoEliminar} no encontrado.")

def EliminarArea():
    print("="*26)
    areaEliminar = input("Escriba el id del area o escriba Lista para obtener la planilla: ")
    if areaEliminar == "Lista":
        print("Lista de areas:")
        Imprimir_Matriz_Ordenada(areas, 1, lambda fila: fila[0])
    else:
        areaEliminar = int(areaEliminar)
        del areas[areaEliminar]
        print(f"Area con id {areaEliminar} eliminada.")

def EliminarLicencia():
    print("="*26)
    licenciaEliminar = input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla")
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
        Imprimir_Matriz_Ordenada(licencias, 2, lambda fila: fila[0])
    else:
        licenciaEliminar = int(licenciaEliminar)
        del licencias[licenciaEliminar]
        print(f"Licencia con id {licenciaEliminar} eliminada.")


if __name__ == "__main__":
    Eliminar(3)