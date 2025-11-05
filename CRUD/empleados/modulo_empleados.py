
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from impresion import imprimir_archivo
from estadisticas import cantidad_empleados, porcentaje_empleados_activos, cantidad_empleados_area, promedio_de_edad
from CRUD.registrar import Ingresar_Fecha, verificar_telefono, Ingresar_Numero, agregar_entidad_archivo
from CRUD.csv_utils import obtener_ultimo_id
from CRUD.buscador import encontrar_elemento
from CRUD.actualizar import editar_entidad_archivo
from CRUD.eliminar import eliminar_entidad_archivo, Modificar_cantidad_area
from config import CSV_EMPLEADOS, CSV_AREAS, CSV_LICENCIAS
#Funciones 

#Registrar empleado
def RegistrarEmpleado(archivo):
    """
    Registra un nuevo empleado en el sistema.
    Solicita todos los datos necesarios y actualiza la cantidad del área.
    
    Args:
        archivo: Ruta del archivo CSV donde se guardará el empleado
    """
    id = obtener_ultimo_id(archivo)
    id = id + 1 if id != 0 else 0
    nombre_empleado = input("Ingrese el nombre del empleado: ").strip().capitalize()
    apellido_empleado = input("Ingrese el apellido del empleado: ").strip().capitalize()
    telefono_empleado = verificar_telefono()
    posicion_empleado = input("Ingrese la posicion del empleado: ").strip().capitalize()
    num_area_empleado = Ingresar_Numero("Ingrese el numero del area del empleado: " )
    fecha_ingreso_empleado = Ingresar_Fecha("el ingreso del empleado")
    fecha_nacimiento_empleado = Ingresar_Fecha("la fecha de nacimiento del empleado")
    fila = [id, nombre_empleado + " " + apellido_empleado, telefono_empleado, posicion_empleado, num_area_empleado, "Activo", fecha_ingreso_empleado, fecha_nacimiento_empleado]
    ok = agregar_entidad_archivo(archivo, fila)
    if ok:
        print(f"Se agrego el empleado {nombre_empleado + " " + apellido_empleado} exitosamente!")
        Modificar_cantidad_area(True, num_area_empleado)
    else:
        print("No se pudo registrar al empleado")

#Buscar empleado
def BuscarEmpleado():
    """
    Menú interactivo para buscar empleados por diferentes criterios.
    Permite buscar por ID, nombre/apellido, área, o mostrar todos los empleados.
    """
    print(AZUL + "MENU PRINCIPAL -> EMPLEADOS -> BUSCADOR" + RESET)
    print(AZUL + "="*34 + RESET)
    print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
    print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
    print(CIAN + "| 2 - Nombre/Apellido".ljust(33) + "|" + RESET)
    print(CIAN + "| 3 - Area".ljust(33) + "|" + RESET)
    print(CIAN + "| 4 - Mostrar empleados".ljust(33) + "|" + RESET)
    print(CIAN + "| 5 - Volver".ljust(33) + "|" + RESET)
    print(AZUL + "="*34 + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
    print()
    match opcion: 
        case 1:
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
            encontrar_elemento(busqueda, CSV_EMPLEADOS, 0, 0)
        case 2:
            busqueda = input(MAGENTA + "Ingrese el nombre o apellido a buscar: " + RESET)
            busqueda = busqueda.lower()
            encontrar_elemento(busqueda, CSV_EMPLEADOS, 1, 0)
        case 3: 
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el numero de area a buscar: " + RESET)
            encontrar_elemento(busqueda, CSV_EMPLEADOS, 4, 0)
        case 4:
            imprimir_archivo(CSV_EMPLEADOS, 0)

            # print(CIAN + "="*34 + RESET)
            # print(CIAN + "| Opciones ascendentemente:".ljust(33) + "|" + RESET)
            # print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
            # print(CIAN + "| 2 - Area".ljust(33) + "|" + RESET)
            # print(CIAN + "| 3 - Apellido".ljust(33) + "|" + RESET)
            # print(CIAN + "| 4 - Volver".ljust(33) + "|" + RESET)
            # print(CIAN + "="*34 + RESET)
            # opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de ordenado: " + RESET)
            # print()
            # match opcion :
            #     case 1:
            #         key = lambda fila : fila[0]
            #         Imprimir_Matriz_Ordenada(empleados, 0,  key)
            #     case 2:
            #         key = lambda fila : fila[4]
            #         Imprimir_Matriz_Ordenada(empleados, 0,  key)
            #     case 3: 
            #         key = lambda fila: fila[1].rsplit(" ", 1)[-1]
            #         Imprimir_Matriz_Ordenada(empleados, 0,  key)

def EstadisticasEmpleados():
    """
    Muestra estadísticas sobre los empleados del sistema.
    Incluye cantidad total, activos/inactivos, por área y promedio de edad.
    
    Returns:
        int: 0 al finalizar
    """
    print("="*43)
    print("MENU PRINCIPAL -> EMPLEADOS -> ESTADISTICAS")
    print("="*43)
    print("| Opciones:".ljust(42) +"|")
    print("| 1. Ver cantidad de empleados totales".ljust(42) +"|")
    print("| 2. Ver estado actual de empleados".ljust(42) +"|")
    print("| 3. Ver cantidad de empleados por area".ljust(42) +"|")
    print("| 4. Ver Promedio de edad".ljust(42) +"|")
    print("| 0. Volver".ljust(42) +"|")
    print("="*43)
    activos, inactivos = cantidad_empleados()
    opcion = Ingresar_Numero("Seleccione una opcion: ")
    print()
    match opcion:
        case 1: 
            print(f'Cantidad de empleados totales: {activos + inactivos}')
        case 2:
            print(f'Cantidad de empleados Activos: {activos}')
            print(f'Cantidad de empleado Inactivos: {inactivos}')
            porcentaje_empleados_activos(activos, inactivos)
        case 3:
            print("Cantidad de empleados por area: ")
            print()
            cantidad_empleados_area()
        case 4:
            promedio_de_edad()
        case 0:
            print("Volviendo al menu principal...")
        case _:
            print("Opcion no valida")
        
    return 0
#Editar empleado
def EditarEmpleado():
    """
    Edita los datos de un empleado existente.
    Permite modificar nombre, teléfono, posición, área, estado, o fechas.
    """
    print("="*26)
    index = Ingresar_Numero("Escriba el id del empleado a editar:  ")
    print("Que campo quiere editar?")
    print('1. Nombre y Apellido')
    print('2. Telefono')
    print('3. Posición')
    print('4. Area')
    print('5. Alta Lógica')
    print('6. Fecha de ingreso')
    print('7. Fecha de nacimiento')
    print('0. Volver')
    campo = Ingresar_Numero("Seleccione el campo a editar (1-7): ")
    match campo:
        case 1:
            nuevo_valor = input("Ingrese el nuevo nombre y apellido: ").strip().capitalize()
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 2:
            nuevo_valor = verificar_telefono()
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 3:
            nuevo_valor = input("Ingrese la nueva posición: ").strip().capitalize()
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 4:
            nuevo_valor = input("Ingrese la nueva area: ").strip().capitalize()
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 5:
            editado = editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, "Activo")
            if editado:
                editar_entidad_archivo(CSV_LICENCIAS, index, 4, 1, "Activo")
        case 6:
            nuevo_valor = Ingresar_Fecha("fecha de ingreso")
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 7:
            nuevo_valor = Ingresar_Fecha("fecha de nacimiento")
            editar_entidad_archivo(CSV_EMPLEADOS, index, campo, 0, nuevo_valor)
        case 0:
            print("\n volviendo...")
        case _:
            print("Opcion no existente")

    
#Eliminar empleado
def EliminarEmpleado():
    """
    Marca un empleado como "Inactivo" en el sistema.
    También marca sus licencias como inactivas en cascada.
    """
    print("="*26)
    empleadoEliminar = input("Escriba el id del empleado o escriba \"Lista\" para obtener la planilla: ").lower()
    if empleadoEliminar == "lista":
        print("Lista de empleados:")
        imprimir_archivo(CSV_EMPLEADOS, 0)
    elif empleadoEliminar.isnumeric():
        empleadoEliminar = int(empleadoEliminar)
        eliminado = eliminar_entidad_archivo(CSV_EMPLEADOS, empleadoEliminar, 0, 5)
        if eliminado:
            eliminar_entidad_archivo(CSV_LICENCIAS, empleadoEliminar, 1, 4)
    else: 
        print("Ingrese una opción válida ")
        print()
             
if __name__ == "__main__":
    EstadisticasEmpleados()