
import re
from dataset import justificaciones, empleados, areas
from idGenerator import generar_id
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


# Funciones


def Ingresar_Numero(mensaje, numero=None):
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
    print(AZUL + "Seleccione una justificacion:" + RESET)
    for justificacion in justificaciones:
        print(CIAN + f"{justificacion[0]} - {justificacion[1]}" + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion: " + RESET)
    return opcion


def Ingresar_Fecha(asunto):
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


def Calcular_cantidad_empleados(empleados, area_id):
    cantidad = 0
    for empleado in empleados:
        if empleado[4] == area_id and empleado[5] == "Activo":
            cantidad += 1
    return cantidad


def verificar_area():
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
    ultimo_codigo = "0"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    return ultimo_codigo



def agregar_entidad_archivo(archivo, columnas):
    try:
        with open(archivo, 'a', encoding='UTF-8') as arch:
            nueva_fila = str(columnas[0])
            for col in range(len(columnas)):
                if col == 0:
                    continue
                else:
                    nueva_fila += ";" + str(columnas[col])
            nueva_fila += "\n"
            arch.write(nueva_fila)
            ok = True
            return ok
    except OSError:
        print("Error al registrar al empleado")
        print(OSError)
        ok = False
        return ok