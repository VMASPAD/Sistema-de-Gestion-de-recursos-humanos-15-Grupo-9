
import re
from dataset import archivos, justificaciones

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

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


def verificar_telefono(codigo_area = None, telefono = None):
    """
    Solicita y valida un número de teléfono argentino.
    Formato: +54 [código de área] [8 dígitos]
    
    Returns:
        str: Teléfono formateado completo
    """
    if not codigo_area:
        codigo_area = str(Ingresar_Numero(MAGENTA + "Ingrese el codigo de area (sin +54): " + RESET))
    if not telefono:
        telefono = str(Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET))
    patron = re.compile('[0-9]{8}')
    while not patron.match(telefono):
        print(ROJO + "Telefono invalido" + RESET)
        telefono = str(Ingresar_Numero(MAGENTA + "Ingrese el telefono (los ultimos 8 digitos): " + RESET))
    telefono = "+54" + codigo_area + telefono
    return telefono

def obtener_ultimo_codigo(archivo):
    """
    Obtiene el último código/ID del archivo CSV sin cargar todo en memoria.
    Lee línea por línea hasta el final.
    
    Args:
        archivo: Ruta del archivo CSV
    
    Returns:
        str: Último código encontrado ("0" si el archivo no existe o está vacío)
    """
    ultimo_codigo = "0"
    try:
        with open(archivo, 'r', encoding="UTF-8") as arch:
            skip = True
            for linea in arch:
                if skip:
                    skip = False
                    continue
                datos = linea.strip().split(",")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    except IndexError:
        print("Archivo vacío")
    except:
        print("Error!")
    return ultimo_codigo




def agregar_entidad_archivo(archivo, columnas):
    try:
        with open(archivo, 'a', encoding='UTF-8') as arch:
            nueva_fila = str(columnas[0])
            for col in range(len(columnas)):
                if col == 0:
                    continue
                else:
                    nueva_fila += "," + str(columnas[col])
            nueva_fila += "\n"
            arch.write(nueva_fila)
            ok = True
            return ok
    except OSError:
        print("Error al registrar al empleado")
        print(OSError)
        ok = False
        return ok
    

