
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from impresion import Buscar_id_archivo,imprimir_archivo, Reemplazo_Id_Valor
# from estadisticas import promedio_licencias_por_empleado
from CRUD.registrar import Eleccion_Justificacion, Ingresar_Fecha, Ingresar_Numero,agregar_entidad_archivo, obtener_ultimo_codigo
from CRUD.buscador import encontrar_elemento
from CRUD.eliminar import eliminar_entidad_archivo
from CRUD.actualizar import editar_entidad_archivo
from estadisticas import cantidad_entidad, promedio_licencias_por_empleado
from dataset import archivos, justificaciones
#Funciones 

#Registrar Licencia
def RegistrarLicencia():
    """
    Registra una nueva licencia para un empleado.
    Solicita datos del empleado, fecha y justificación, luego agrega al archivo CSV.
    """
    id = int(obtener_ultimo_codigo(archivos[2]))
    id = id + 1 if id != 0 else 0
    id_empleado = Ingresar_Numero(MAGENTA + "Ingrese el id del empleado: " + RESET)
    fecha_licencia = Ingresar_Fecha("la licencia")
    justificacion_licencia = Eleccion_Justificacion()

    fila = [id, id_empleado, fecha_licencia, justificacion_licencia, "Activo"]
    ok = agregar_entidad_archivo(archivos[2], fila)
    if ok:
        print(f"Se agrego el la justificacion {justificacion_licencia} para el empleado {Reemplazo_Id_Valor(id_empleado, 1)}!")
    else:
        print("No se pudo registrar la justificacion")

#Buscar Licencia
def BuscarLicencia():
    """
    Menú interactivo para buscar licencias por diferentes criterios.
    Permite buscar por ID, empleado, fecha, o mostrar todas las licencias.
    """
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
            encontrar_elemento(busqueda, archivos[2], 0, 2)
        case 2:
            busqueda = input("Ingrese el id del empleado a buscar: ")
            encontrar_elemento(busqueda, archivos[2], 1, 2)
        case 3:
            busqueda = Ingresar_Fecha("la licencia a buscar")
            encontrar_elemento(busqueda, archivos[2], 2, 2)
        case 4:
            imprimir_archivo(archivos[2], 2)
        case 5:
            return


def EstadisticasLicencias():
    """
    Muestra estadísticas sobre las licencias del sistema.
    Incluye cantidad total y promedio por empleado.
    """
    print("="*46)
    print("MENU PRINCIPAL -> LICENCIAS -> ESTADISTICAS")
    print("="*46)
    print("| Opciones:".ljust(45) + "|")
    print("| 1 - Ver cantidad de licencias".ljust(45) + "|")
    print("| 2 - Ver promedio de licencias por empleado".ljust(45) + "|")
    print("| 0 - Volver".ljust(45) + "|")
    print("="*46)
    opcion = Ingresar_Numero("Seleccione una opcion: ")
    print()
    licencias, licencias_inactivas = cantidad_entidad(2, -1)
    match opcion:
        case 1:
            print(f"La cantidad total de licencias es: {licencias + licencias_inactivas}")
            print(VERDE + f"La cantidad de licencias activas es: {licencias}" + RESET)
            print(AMARILLO + f"La cantidad de licencias inactivas es: {licencias_inactivas}" + RESET)
        case 2:
            empleados, empleados_inactivos = cantidad_entidad(0, 5)
            promedio_licencias_por_empleado(licencias, empleados) ##########################################################   
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
    """
    Edita los datos de una licencia existente.
    Permite modificar la fecha o el empleado asociado a la licencia.
    """

    print("="*26)
    index = int(input('Escriba el id de la licencia a editar: '))
    
    print("Que campo quiere editar?")
    print('1. Fecha')
    print('2. Empleado')
    print('3. Justificacion')
    print('4. Alta Lógica')
    valueTochange = Ingresar_Numero('Seleccione una opcion: ')
    
    if valueTochange == 1:
        newFecha = Ingresar_Fecha("la licencia")
        editado = editar_entidad_archivo(archivos[2], index, 2, 0, newFecha)
        if editado:
            print(f"Licencia actualizada con nueva fecha: {newFecha}")
    elif valueTochange == 2:
        id_empleado = Ingresar_Numero(MAGENTA + "Ingrese el id del empleado: " + RESET)
        editado = editar_entidad_archivo(archivos[2], index, 1, 0, id_empleado)
        if editado:
            print(f"Licencia actualizada con nuevo empleado: {Reemplazo_Id_Valor(id_empleado, 1)}")
    elif valueTochange == 3:
        justificacion = Eleccion_Justificacion()
        editado = editar_entidad_archivo(archivos[2], index, 3, 0, justificacion)
        if editado:
            print(f"Licencia actualizada con nueva justificacion: {justificaciones[justificacion][1]}")

    elif valueTochange == 4:
        editar_entidad_archivo(archivos[2], index, 4, 0, "Activo")
    else:
        print('Opción inválida')

#Eliminar Licencia
def EliminarLicencia():
    """
    Marca una licencia como "Inactivo" en el sistema.
    Permite mostrar la lista completa o eliminar por ID.
    """
    print("="*26)
    licenciaEliminar = input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla: ")
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
        imprimir_archivo(archivos[2], 2)

    elif licenciaEliminar.isnumeric():
        licenciaEliminar = int(licenciaEliminar)
        eliminar_entidad_archivo(archivos[2], licenciaEliminar, 0, 4)
        print(f"Licencia con id {licenciaEliminar} eliminada.")
    else: 
        print(f"Licencia con id {licenciaEliminar} no encontrada.")
        print()