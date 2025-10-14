
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada, Encontrar_Id_Empleado
from estadisticas import promedio_licencias_por_empleado
from CRUD.registrar import Eleccion_Justificacion, Ingresar_Fecha, Ingresar_Numero
from CRUD.buscador import Encontrar, Id_Empleado
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import empleados, licencias
#Funciones 

#Registrar Licencia
def RegistrarLicencia(licencias):
    nueva_licencia = []
    id_empleado = Id_Empleado(empleados, input("Ingrese el nombre y apellido del empleado: "))
    fecha_licencia = Ingresar_Fecha("la licencia")
    justificacion_licencia = Eleccion_Justificacion()
    A = [generar_id(licencias), id_empleado, fecha_licencia, justificacion_licencia, "Activo"]
    nueva_licencia.extend(A)
    licencias.append(nueva_licencia)
    return licencias

def EstadisticasLicencias(licencias):
    print("="*46)
    print("MENU PRINCIPAL -> LICENCIAS -> ESTADISTICAS")
    print("="*46)
    print("| Opciones:".ljust(45) + "|")
    print("| 1 - Ver cantidad de licencias".ljust(45) + "|")
    print("| 2 - Ver promedio de licencias por empleado".ljust(45) + "|")
    print("| 0 - Volver".ljust(45) + "|")
    print("="*46)
    opcion = Ingresar_Numero("Seleccione una opcion: ")
    match opcion:
        case 1:
            print(f"La cantidad total de licencias es: {len(list(licencia for licencia in licencias if licencia[4] == 'Activo'))}")
        case 2:
            promedio_licencias_por_empleado(licencias, empleados)
        case 0:
            return
        case _:
            print("Opcion no valida.")
            print("="*130)
            print()
            print("ESTADISTICAS FINALIZADAS")
            print("="*130)
    return

#Buscar Licencia
def BuscarLicencia(licencias, empleados):
    print(AZUL + "="*34 + RESET)
    print(AZUL + "MENU PRINCIPAL -> LICENCIAS -> BUSCADOR" + RESET)
    print(AZUL + "="*34 + RESET)
    print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
    print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
    print(CIAN + "| 2 - Empleado".ljust(33) + "|" + RESET)
    print(CIAN + "| 3 - Fecha".ljust(33) + "|" + RESET)
    print(CIAN + "| 4 - Mostrar licencias".ljust(33) + "|" + RESET)
    print(CIAN + "| 5 - Volver".ljust(33) + "|" + RESET)
    print(CIAN + "="*34 + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
    print()
    match opcion:
        case 1:
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
            Encontrar(busqueda, licencias, 0, 2)
        case 2:
            busqueda = input("Ingrese el nombre y apellido del empleado a buscar: ")
            busqueda = busqueda.lower()
            busqueda = Encontrar_Id_Empleado(empleados, busqueda)
            if busqueda:
                Encontrar(busqueda, licencias, 1, 2)
        case 3:
            busqueda = Ingresar_Fecha("la licencia a buscar")
            Encontrar(busqueda, licencias, 2, 2)
        case 4:
            key = lambda fila : fila[0]
            Imprimir_Matriz_Ordenada(licencias, 2, key)
        case 5:
            return

#Editar Licencia
def EditarLicencia():
    print("="*26)
    index = int(input('Escriba el id de la licencia a editar: '))
    if index < len(licencias) and index >= 0:
        print("Que campo quiere editar?")
        print('1. Fecha')
        print('2. Empleado')
        valueTochange = Ingresar_Numero('Seleccione una opcion: ')
        if licencias[index][0] == index:
            print(f"Licencia encontrada: {licencias[index]}")
        if valueTochange == 1:
            newFecha = Ingresar_Fecha("la licencia")
            licencias[index][2] = newFecha
            print(f"Licencia actualizada: {licencias[index]}")
        elif valueTochange == 2:
            newEmpleado = input(f'Ingrese el nombre y apellido del empleado a reemplazar: {licencias[index][1]}: ')
            licencias[index][1] = Id_Empleado(empleados, newEmpleado)
            print(f"Licencia actualizada: {licencias[index]}")
    else:
        print('Licencia no encontrada')
    return licencias

#Eliminar Licencia
def EliminarLicencia():
    print("="*26)
    licenciaEliminar = input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla: ")
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
        Imprimir_Matriz_Ordenada(licencias, 2, lambda fila: fila[0])
    elif licenciaEliminar in [str(licencia[0]) for licencia in licencias]:
        posicion_licencia = licencias[[str(licencia[0]) for licencia in licencias].index(licenciaEliminar)]
        licencias[posicion_licencia[0]][4] = "Inactivo"
        print(f"Licencia con id {licenciaEliminar} de la persona {empleados[posicion_licencia[1]][1]} eliminada.")
    else:
        print(f"Licencia con id {licenciaEliminar} no encontrada.")