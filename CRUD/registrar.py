
import re
from idGenerator import generar_id
from main import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS, CSV_JUSTIFICACIONES

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
    justificaciones = []
    try:
        with open(CSV_JUSTIFICACIONES, "r", encoding="utf-8") as f:
            next(f, None)  # Saltar header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir id a int
                datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                justificaciones.append(datos)
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {CSV_JUSTIFICACIONES} no existe." + RESET)
    return justificaciones

def leer_areas_csv():
    """Lee el archivo areas.csv y retorna una lista de listas."""
    areas = []
    try:
        with open(CSV_AREAS, "r", encoding="utf-8") as f:
            next(f, None)  # Saltar header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir campos numéricos
                datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                datos[2] = int(datos[2]) if datos[2].isdigit() else datos[2]
                areas.append(datos)
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {CSV_AREAS} no existe." + RESET)
    return areas

def leer_empleados_csv():
    """Lee el archivo empleados.csv y retorna una lista de listas."""
    empleados = []
    try:
        with open(CSV_EMPLEADOS, "r", encoding="utf-8") as f:
            next(f, None)  # Saltar header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir campos numéricos
                if len(datos) >= 6:
                    datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                    datos[4] = int(datos[4]) if datos[4].isdigit() else datos[4]
                empleados.append(datos)
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {CSV_EMPLEADOS} no existe." + RESET)
    return empleados


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
    """
    Agrega una nueva entidad al archivo CSV usando archivo temporal.
    Lee línea por línea el archivo original, copia todo al temporal y agrega la nueva línea.
    Luego reemplaza el original con el temporal.
    
    Args:
        archivo: Ruta del archivo CSV
        columnas: Lista con los valores de cada columna de la nueva entidad
    
    Returns:
        bool: True si se agregó exitosamente, False en caso de error
    """
    import os
    copia = 'matrices/copia_agregar.csv'
    
    try:
        # Construir la nueva fila
        nueva_fila = str(columnas[0])
        for col in range(len(columnas)):
            if col == 0:
                continue
            else:
                nueva_fila += "," + str(columnas[col])
        nueva_fila += "\n"
        
        # Copiar archivo existente y agregar nueva línea
        try:
            with open(archivo, 'r', encoding='UTF-8') as arch, \
                 open(copia, 'w', encoding='UTF-8') as cop:
                # Copiar todo el contenido existente línea por línea
                for linea in arch:
                    cop.write(linea)
                # Agregar la nueva fila
                cop.write(nueva_fila)
        except FileNotFoundError:
            # Si el archivo no existe, crear uno nuevo con header básico
            with open(copia, 'w', encoding='UTF-8') as cop:
                # Detectar tipo de archivo y escribir header apropiado
                if 'areas' in archivo:
                    cop.write("id,nombre,cantidad,estado\n")
                elif 'empleados' in archivo:
                    cop.write("id,nombre,telefono,posicion,area,estado,fecha_ingreso,fecha_nacimiento\n")
                elif 'licencias' in archivo:
                    cop.write("id,id_empleado,fecha,id_justificacion,estado\n")
                cop.write(nueva_fila)
        
        # Reemplazar archivo original con el temporal
        if os.path.exists(archivo):
            os.remove(archivo)
        os.rename(copia, archivo)
        
        return True
        
    except OSError as e:
        print(ROJO + f"Error al registrar la entidad: {e}" + RESET)
        # Limpiar archivo temporal si existe
        if os.path.exists(copia):
            try:
                os.remove(copia)
            except:
                pass
        return False
    except Exception as e:
        print(ROJO + f"Error inesperado: {e}" + RESET)
        # Limpiar archivo temporal si existe
        if os.path.exists(copia):
            try:
                os.remove(copia)
            except:
                pass
        return False