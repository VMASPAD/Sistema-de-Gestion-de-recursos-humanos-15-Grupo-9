
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from idGenerator import generar_id
from impresion import Buscar_id_archivo,imprimir_archivo
from estadisticas import promedio_licencias_por_empleado
from CRUD.registrar import Eleccion_Justificacion, Ingresar_Fecha, Ingresar_Numero,agregar_entidad_archivo
from CRUD.buscador import encontrar_elemento
from CRUD.eliminar import eliminar_entidad_archivo
from dataset import archivos
#Funciones 

#Registrar Licencia
def RegistrarLicencia():
    empleado = Ingresar_Numero(MAGENTA + "Ingrese el nombre y apellido del empleado: " + RESET)
    id_empleado = encontrar_elemento(empleado, archivos[0], 0, 0)
    fecha_licencia = Ingresar_Fecha("la licencia")
    justificacion_licencia = Eleccion_Justificacion(archivos[3])

    fila = [generar_id(archivos[2]), id_empleado, fecha_licencia, justificacion_licencia, "Activo"]
    ok = agregar_entidad_archivo(archivos[3], fila)
    if ok:
        print(f"Se agrego el la justificacion {justificacion_licencia} para el empleado {empleado}!")
    else:
        print("No se pudo registrar la justificacion")

#Buscar Licencia
def BuscarLicencia():
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
            encontrar_elemento(busqueda, archivos[2], 0, 0)
        case 2:
            busqueda = input("Ingrese el nombre y apellido del empleado a buscar: ")
            busqueda = busqueda.lower()
            busqueda = Buscar_id_archivo(archivos[0], busqueda)
            if busqueda:
                encontrar_elemento(busqueda, archivos[2], 1, 0)
        case 3:
            busqueda = Ingresar_Fecha("la licencia a buscar")
            encontrar_elemento(busqueda, archivos[2], 2, 0)
        case 4:
            imprimir_archivo(archivos[2], 0)
        case 5:
            return


def EstadisticasLicencias():
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
            print(f"La cantidad total de licencias es: {len(list(licencia for licencia in archivos[2] if licencia[4] == 'Activo'))}")
        case 2:
            promedio_licencias_por_empleado(archivos[2], archivos[0])
        case 0:
            return
        case _:
            print("Opcion no valida.")
            print("="*130)
            print()
            print("ESTADISTICAS FINALIZADAS")
            print("="*130)
    return

#Editar Licencia
def EditarLicencia():
    print("="*26)
    index = int(input('Escriba el id de la licencia a editar: '))
    if index < len(archivos[2]) and index >= 0:
        print("Que campo quiere editar?")
        print('1. Fecha')
        print('2. Empleado')
        valueTochange = Ingresar_Numero('Seleccione una opcion: ')
        if archivos[2][index][0] == index:
            print(f"Licencia encontrada: {archivos[2][index]}")
        if valueTochange == 1:
            newFecha = Ingresar_Fecha("la licencia")
            archivos[2][index][2] = newFecha
            print(f"Licencia actualizada: {archivos[2][index]}")
        elif valueTochange == 2:
            newEmpleado = input(f'Ingrese el nombre y apellido del empleado a reemplazar: {archivos[2][index][1]}: ')
            archivos[2][index][1] = encontrar_elemento(newEmpleado, archivos[0], 0, 0)
            print(f"Licencia actualizada: {archivos[2][index]}")
    else:
        print('Licencia no encontrada')
    return archivos[2]

#Eliminar Licencia
def EliminarLicencia():
    print("="*26)
    licenciaEliminar = input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla: ")
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
        imprimir_archivo(archivos[2], 2)

    elif licenciaEliminar.isnumeric():
        licenciaEliminar = int(licenciaEliminar)
        eliminar_entidad_archivo(archivos[2], licenciaEliminar, 1, 4)
        print(f"Licencia con id {licenciaEliminar} eliminada.")
    else: 
        print(f"Licencia con id {licenciaEliminar} no encontrada.")
        print()