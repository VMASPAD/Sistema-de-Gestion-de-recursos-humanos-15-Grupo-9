
import re
from idGenerator import generar_id
from config import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS, CSV_JUSTIFICACIONES
from CRUD.csv_utils import leer_csv, obtener_ultimo_id, agregar_linea_csv

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

# Funciones auxiliares para leer archivos

def leer_justificaciones_csv():
    """Lee el archivo justificaciones.csv y retorna una lista de listas."""
    return leer_csv(CSV_JUSTIFICACIONES, skip_header=True, convertir_numeros=[0])

def leer_areas_csv():
    """Lee el archivo areas.csv y retorna una lista de listas."""
    return leer_csv(CSV_AREAS, skip_header=True, convertir_numeros=[0, 2])

def leer_empleados_csv():
    """Lee el archivo empleados.csv y retorna una lista de listas."""
    return leer_csv(CSV_EMPLEADOS, skip_header=True, convertir_numeros=[0, 4])


# Funciones


def Ingresar_Numero(mensaje, numero=None):
    """
    Solicita al usuario un número entero positivo.
    Valida que sea un entero >= 0.
    
    Args:
        mensaje: Texto a mostrar al usuario
        numero: Número opcional para testing
    
    Returns:
        int: Número entero positivo ingresado
    """
    while True:
        try:
            #Esto es para poder probar la función en las pruebas unitarias
            if not numero:
                numero = int(input(mensaje))
            if numero < 0:
                numero = None
                raise ValueError
            return numero
        except ValueError:
            print()
            print(ROJO + "Entrada invalida. Por favor, ingrese un numero entero." + RESET)
            print()


def Eleccion_Justificacion():
    """
    Muestra las justificaciones disponibles y solicita al usuario que elija una.
    Lee del archivo justificaciones.csv.
    
    Returns:
        int: ID de la justificación seleccionada
    """
    justificaciones = leer_justificaciones_csv()
    print(AZUL + "Seleccione una justificacion:" + RESET)
    for justificacion in justificaciones:
        print(CIAN + f"{justificacion[0]} - {justificacion[1]}" + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion: " + RESET)
    return opcion


def Ingresar_Fecha(asunto):
    """
    Solicita al usuario una fecha válida (año, mes, día).
    Valida el rango de cada componente y años bisiestos.
    
    Args:
        asunto: Descripción de la fecha (ej: "el ingreso del empleado")
    
    Returns:
        str: Fecha en formato AAAA-M-D
    """
    año = Ingresar_Numero(MAGENTA + f"Ingrese el año (AAAA) de {asunto}: " + RESET)
    while año < 1930 or año > 2025:
        print("Ingrese un año valido")
        año = Ingresar_Numero(MAGENTA + f"Ingrese el año (AAAA) de {asunto}: " + RESET)
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        febrero = 29
    else:
        febrero = 28

    mes = Ingresar_Numero(MAGENTA + f"Ingrese el mes (MM) de {asunto}: " + RESET)
    while mes > 12:
        print("Ingrese un mes válido")
        mes = Ingresar_Numero(MAGENTA + f"Ingrese el mes (MM) de {asunto}: " + RESET)
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            max = 31
        case 4 | 6 | 9 | 11:
            max = 30
        case 2:
            max = febrero
    dia = Ingresar_Numero(MAGENTA + f"Ingrese el dia (DD) de {asunto}: " + RESET)
    while dia > max:
        print("Ingrese un dia válido")
        dia = Ingresar_Numero(MAGENTA + f"Ingrese el dia (DD) de {asunto}: " + RESET)
    return f"{año}-{mes}-{dia}"


def Calcular_cantidad_empleados(area_id):
    """
    Calcula la cantidad de empleados activos en un área específica.
    Lee el archivo empleados.csv línea por línea.
    
    Args:
        area_id: ID del área a consultar
    
    Returns:
        int: Cantidad de empleados activos en el área
    """
    empleados = leer_empleados_csv()
    cantidad = 0
    for empleado in empleados:
        if empleado[4] == area_id and empleado[5] == "Activo":
            cantidad += 1
    return cantidad


def verificar_area():
    """
    Solicita y valida el nombre de un área nueva.
    Verifica que no exista ya en el sistema y que no esté vacío.
    
    Returns:
        str: Nombre del área validado y capitalizado
    """
    areas = leer_areas_csv()
    nombres_areas = {areas[i][1].lower() for i in range(len(areas))}
    nombre_area = input(MAGENTA + "Ingrese el nombre del área: " + RESET).strip().lower()
    while nombre_area in nombres_areas or nombre_area == "":
        if nombre_area in nombres_areas:
            print(ROJO + "El nombre del área ya existe, por favor ingrese otro." + RESET)
        else:
            print(ROJO + "El nombre del área no puede estar vacío." + RESET)
        nombre_area = input(
            MAGENTA + "Ingrese el nombre del área: " + RESET).strip().lower()
    return nombre_area.capitalize()


def verificar_telefono():
    """
    Solicita y valida un número de teléfono argentino.
    Formato: +54 [código de área] [8 dígitos]
    
    Returns:
        str: Teléfono formateado completo
    """
    codigo_area = str(Ingresar_Numero(MAGENTA + "Ingrese el codigo de area (sin +54): " + RESET))
    telefono = str(Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET))
    patron = re.compile('[0-9]{8}')
    while not patron.match(telefono):
        print(ROJO + "Telefono invalido" + RESET)
        telefono = str(Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET))
    telefono = "+54" + codigo_area + telefono
    # telefonos_en_sistema = {empleados[i][2] for i in range(len(empleados))}
    # while telefono in telefonos_en_sistema:
    #     print(ROJO + "El telefono ya existe en el sistema, por favor ingrese otro." + RESET)
    #     codigo_area = Ingresar_Numero(MAGENTA + "Ingrese el codigo de area (sin +54): " + RESET)
    #     telefono = Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET)
    #     while not patron.match(telefono):
    #         print(ROJO + "Telefono invalido" + RESET)
    #         telefono = Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET)
    #     telefono = "+54" + codigo_area + telefono
    return telefono

def obtener_ultimo_codigo(archivo):
    """
    Obtiene el último código/ID del archivo CSV.
    Usa csv_utils para evitar duplicación.
    
    Args:
        archivo: Ruta del archivo CSV
    
    Returns:
        str: Último código encontrado ("0" si no existe)
    """
    return str(obtener_ultimo_id(archivo))



def agregar_entidad_archivo(archivo, columnas):
    """
    Agrega una nueva entidad al archivo CSV.
    Usa csv_utils para reducir duplicación.
    
    Args:
        archivo: Ruta del archivo CSV
        columnas: Lista con los valores de cada columna de la nueva entidad
    
    Returns:
        bool: True si se agregó exitosamente, False en caso de error
    """
    return agregar_linea_csv(archivo, columnas)