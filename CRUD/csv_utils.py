"""
Utilidades comunes para manejo de archivos CSV.
Proporciona funciones genéricas para leer, escribir y modificar archivos CSV
sin duplicar código en los diferentes módulos.
"""

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


def leer_csv(archivo, skip_header=True, convertir_numeros=None):
    """
    Lee un archivo CSV y retorna una lista de listas.
    
    Args:
        archivo: Ruta del archivo CSV
        skip_header: Si True, salta la primera línea (encabezado)
        convertir_numeros: Lista de índices de columnas a convertir a int (None = no convertir)
    
    Returns:
        list: Lista de listas con los datos del CSV
    """
    datos = []
    try:
        with open(archivo, 'r', encoding='UTF-8') as f:
            if skip_header:
                next(f, None)  # Saltar header
            
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                
                cols = linea.split(",")
                
                # Convertir columnas numéricas si se especifica
                if convertir_numeros:
                    for idx in convertir_numeros:
                        if idx < len(cols) and cols[idx].isdigit():
                            cols[idx] = int(cols[idx])
                
                datos.append(cols)
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {archivo} no existe." + RESET)
    except Exception as e:
        print(ROJO + f"Error al leer {archivo}: {e}" + RESET)
    
    return datos


def escribir_csv(archivo, lineas):
    """
    Escribe líneas en un archivo CSV.
    
    Args:
        archivo: Ruta del archivo CSV
        lineas: Lista de líneas (strings) a escribir
    
    Returns:
        bool: True si fue exitoso, False en caso contrario
    """
    try:
        with open(archivo, 'w', encoding='UTF-8') as f:
            f.writelines(lineas)
        return True
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al escribir en {archivo}: {e}" + RESET)
        return False


def modificar_entidad_csv(archivo, id_buscar, columna_id, columna_modificar, nuevo_valor, condicion=None):
    """
    Modifica una entidad específica en un archivo CSV.
    Lee el archivo completo, modifica en memoria y reescribe.
    
    Args:
        archivo: Ruta del archivo CSV
        id_buscar: ID de la entidad a modificar
        columna_id: Índice de la columna que contiene el ID
        columna_modificar: Índice de la columna a modificar
        nuevo_valor: Nuevo valor a asignar
        condicion: Función opcional que recibe datos y retorna True si se puede modificar
    
    Returns:
        tuple: (bool encontrado, list datos_modificados o None)
    """
    encontrado = False
    datos_modificados = None
    
    try:
        # Leer todo el archivo
        with open(archivo, 'r', encoding='UTF-8') as f:
            lineas = f.readlines()
        
        # Modificar en memoria
        for i in range(1, len(lineas)):  # Saltar header
            datos = lineas[i].strip().split(",")
            if len(datos) > max(columna_id, columna_modificar):
                id_actual = int(datos[columna_id]) if datos[columna_id].isdigit() else datos[columna_id]
                
                if id_actual == id_buscar:
                    # Verificar condición si existe
                    if condicion and not condicion(datos):
                        return False, None
                    
                    datos[columna_modificar] = str(nuevo_valor)
                    lineas[i] = ",".join(map(str, datos)) + "\n"
                    encontrado = True
                    datos_modificados = datos
                    break
        
        # Reescribir el archivo si se encontró
        if encontrado:
            with open(archivo, 'w', encoding='UTF-8') as f:
                f.writelines(lineas)
        
        return encontrado, datos_modificados
        
    except FileNotFoundError:
        print(ROJO + f"Error: Archivo {archivo} no encontrado" + RESET)
        return False, None
    except Exception as e:
        print(ROJO + f"Error al modificar {archivo}: {e}" + RESET)
        return False, None


def modificar_multiple_csv(archivo, condicion, modificacion):
    """
    Modifica múltiples entidades en un archivo CSV basándose en una condición.
    
    Args:
        archivo: Ruta del archivo CSV
        condicion: Función que recibe datos y retorna True si debe modificarse
        modificacion: Función que recibe datos y retorna datos modificados
    
    Returns:
        int: Cantidad de registros modificados
    """
    modificados = 0
    
    try:
        # Leer todo el archivo
        with open(archivo, 'r', encoding='UTF-8') as f:
            lineas = f.readlines()
        
        # Modificar en memoria
        for i in range(1, len(lineas)):  # Saltar header
            datos = lineas[i].strip().split(",")
            
            if condicion(datos):
                datos_nuevos = modificacion(datos)
                lineas[i] = ",".join(map(str, datos_nuevos)) + "\n"
                modificados += 1
        
        # Reescribir el archivo
        if modificados > 0:
            with open(archivo, 'w', encoding='UTF-8') as f:
                f.writelines(lineas)
        
        return modificados
        
    except FileNotFoundError:
        print(ROJO + f"Error: Archivo {archivo} no encontrado" + RESET)
        return 0
    except Exception as e:
        print(ROJO + f"Error al modificar {archivo}: {e}" + RESET)
        return 0


def obtener_ultimo_id(archivo):
    """
    Obtiene el último ID del archivo CSV.
    
    Args:
        archivo: Ruta del archivo CSV
    
    Returns:
        int: Último ID encontrado (0 si no existe el archivo o está vacío)
    """
    ultimo_id = 0
    try:
        with open(archivo, 'r', encoding='UTF-8') as f:
            next(f, None)  # Saltar header
            for linea in f:
                datos = linea.strip().split(",")
                if datos and datos[0].isdigit():
                    ultimo_id = int(datos[0])
    except FileNotFoundError:
        pass
    except Exception as e:
        print(ROJO + f"Error al leer último ID de {archivo}: {e}" + RESET)
    
    return ultimo_id


def agregar_linea_csv(archivo, columnas):
    """
    Agrega una nueva línea al final de un archivo CSV.
    
    Args:
        archivo: Ruta del archivo CSV
        columnas: Lista con los valores de cada columna
    
    Returns:
        bool: True si fue exitoso, False en caso contrario
    """
    try:
        # Leer contenido existente
        lineas = []
        try:
            with open(archivo, 'r', encoding='UTF-8') as f:
                lineas = f.readlines()
        except FileNotFoundError:
            lineas = []
        
        # Construir nueva línea
        nueva_linea = ",".join(map(str, columnas)) + "\n"
        
        # Escribir todo de vuelta
        with open(archivo, 'w', encoding='UTF-8') as f:
            f.writelines(lineas)
            f.write(nueva_linea)
        
        return True
    except Exception as e:
        print(ROJO + f"Error al agregar línea a {archivo}: {e}" + RESET)
        return False
