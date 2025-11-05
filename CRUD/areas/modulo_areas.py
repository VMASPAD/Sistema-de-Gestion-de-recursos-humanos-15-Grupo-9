
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada
from estadisticas import promedio_empleados_por_area
from CRUD.registrar import Ingresar_Numero, verificar_area
from CRUD.buscador import Encontrar
from CRUD.eliminar import Eliminar_ClaveForanea
from main import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS

def obtener_ultimo_id_csv(archivo_csv):
    """
    Obtiene el último ID del archivo CSV sin cargar todo en memoria.
    Lee línea por línea y retorna el ID máximo encontrado.
    """
    max_id = -1
    try:
        with open(archivo_csv, "r", encoding="utf-8") as f:
            next(f, None)  # Saltar header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                id_str = line.split(",")[0]
                if id_str.isdigit():
                    max_id = max(max_id, int(id_str))
    except FileNotFoundError:
        return -1
    except (PermissionError, IOError, OSError):
        return -1
    return max_id


def buscar_en_csv_linea_por_linea(archivo_csv, valor_busqueda, columna_index, skip_header=True):
    """
    Busca un valor en el CSV procesando línea por línea sin cargar todo.
    Retorna la línea completa si la encuentra, None si no.
    """
    try:
        with open(archivo_csv, "r", encoding="utf-8") as f:
            if skip_header:
                next(f, None)
            
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                if len(datos) > columna_index:
                    # Convertir a int si es numérico
                    valor_col = int(datos[columna_index]) if datos[columna_index].isdigit() else datos[columna_index]
                    if valor_col == valor_busqueda or str(valor_col).lower() == str(valor_busqueda).lower():
                        # Convertir campos numéricos antes de retornar
                        datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                        if len(datos) > 2:
                            datos[2] = int(datos[2]) if datos[2].isdigit() else datos[2]
                        return datos
    except (FileNotFoundError, PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al buscar en {archivo_csv}: {e}" + RESET)
    return None


def leer_areas_csv(skip_header=True):
    """
    Lee el archivo areas.csv y retorna una lista de listas con los datos.
    Incluye manejo de 3 excepciones típicas.
    
    Args:
        skip_header: Si True, omite la primera línea (encabezado)
    
    Returns:
        Lista de listas con los datos de áreas
    
    Raises:
        FileNotFoundError: Si el archivo no existe
        PermissionError: Si no hay permisos de lectura
        IOError: Para otros errores de I/O
    """
    areas = []
    try:
        with open(CSV_AREAS, "r", encoding="utf-8") as f:
            lines = f.readlines()
            start_index = 1 if skip_header and len(lines) > 0 else 0
            
            for line in lines[start_index:]:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir campos numéricos
                datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                datos[2] = int(datos[2]) if datos[2].isdigit() else datos[2]
                areas.append(datos)
                
    except FileNotFoundError:
        print(ROJO + f"Error: El archivo {CSV_AREAS} no existe." + RESET)
        raise
    except PermissionError:
        print(ROJO + f"Error: No hay permisos para leer {CSV_AREAS}." + RESET)
        raise
    except (IOError, OSError) as e:
        print(ROJO + f"Error de I/O al leer {CSV_AREAS}: {e}" + RESET)
        raise
    
    return areas


def escribir_areas_csv(areas, incluir_header=True):
    """
    Escribe la lista completa de áreas al archivo CSV.
    Incluye manejo de 3 excepciones típicas.
    
    Args:
        areas: Lista de listas con los datos de áreas
        incluir_header: Si True, escribe el encabezado en la primera línea
    
    Raises:
        PermissionError: Si no hay permisos de escritura
        IOError: Para otros errores de I/O
        OSError: Para errores del sistema operativo
    """
    try:
        with open(CSV_AREAS, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("id,nombre,cantidad,estado\n")
            
            for area in areas:
                f.write(f"{area[0]},{area[1]},{area[2]},{area[3]}\n")
                
    except PermissionError:
        print(ROJO + f"Error: No hay permisos para escribir en {CSV_AREAS}." + RESET)
        raise
    except (IOError, OSError) as e:
        print(ROJO + f"Error de I/O al escribir en {CSV_AREAS}: {e}" + RESET)
        raise


def leer_empleados_csv(skip_header=True):
    """Lee el archivo empleados.csv y retorna una lista con los datos."""
    empleados_data = []
    try:
        with open(CSV_EMPLEADOS, "r", encoding="utf-8") as f:
            lines = f.readlines()
            start_index = 1 if skip_header and len(lines) > 0 else 0
            
            for line in lines[start_index:]:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir campos numéricos (id, area)
                if len(datos) >= 6:
                    datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                    datos[4] = int(datos[4]) if datos[4].isdigit() else datos[4]
                empleados_data.append(datos)
                
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {CSV_EMPLEADOS} no existe." + RESET)
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al leer {CSV_EMPLEADOS}: {e}" + RESET)
    
    return empleados_data


def escribir_empleados_csv(empleados_data, incluir_header=True):
    """Escribe la lista completa de empleados al archivo CSV."""
    try:
        with open(CSV_EMPLEADOS, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("id,nombre,telefono,posicion,area,estado,fecha_ingreso,fecha_nacimiento\n")
            
            for emp in empleados_data:
                f.write(",".join(map(str, emp)) + "\n")
                
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al escribir en {CSV_EMPLEADOS}: {e}" + RESET)
        raise


def leer_licencias_csv(skip_header=True):
    """Lee el archivo licencias.csv y retorna una lista con los datos."""
    licencias_data = []
    try:
        with open(CSV_LICENCIAS, "r", encoding="utf-8") as f:
            lines = f.readlines()
            start_index = 1 if skip_header and len(lines) > 0 else 0
            
            for line in lines[start_index:]:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                # Convertir campos numéricos
                if len(datos) >= 5:
                    datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                    datos[1] = int(datos[1]) if datos[1].isdigit() else datos[1]
                    datos[3] = int(datos[3]) if datos[3].isdigit() else datos[3]
                licencias_data.append(datos)
                
    except FileNotFoundError:
        print(AMARILLO + f"Advertencia: {CSV_LICENCIAS} no existe." + RESET)
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al leer {CSV_LICENCIAS}: {e}" + RESET)
    
    return licencias_data


def escribir_licencias_csv(licencias_data, incluir_header=True):
    """Escribe la lista completa de licencias al archivo CSV."""
    try:
        with open(CSV_LICENCIAS, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("id,id_empleado,fecha,id_justificacion,estado\n")
            
            for lic in licencias_data:
                f.write(",".join(map(str, lic)) + "\n")
                
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al escribir en {CSV_LICENCIAS}: {e}" + RESET)
        raise


#Registrar Area
def RegistrarArea():
    """
    Registra una nueva área en el archivo CSV usando archivo temporal.
    Lee línea por línea, copia todo y agrega la nueva área al final.
    Usa solo modos 'r' y 'w' como se requiere.
    """
    import os
    try:
        # Obtener datos de la nueva área
        nombre_area = verificar_area()
        cantidad_empleados = 0
        
        # Generar ID obteniendo el último ID sin cargar todo el archivo
        ultimo_id = obtener_ultimo_id_csv(CSV_AREAS)
        nuevo_id = ultimo_id + 1
        
        # Crear nueva área
        nueva_area = [nuevo_id, nombre_area, cantidad_empleados, "Activo"]
        
        # Usar archivo temporal
        copia = "matrices/copia_area.csv"
        
        try:
            # Copiar archivo existente línea por línea y agregar nueva área
            with open(CSV_AREAS, "r", encoding="utf-8") as f, \
                 open(copia, "w", encoding="utf-8") as cop:
                # Copiar todo el contenido existente
                for linea in f:
                    cop.write(linea)
                # Agregar la nueva área
                cop.write(f"{nueva_area[0]},{nueva_area[1]},{nueva_area[2]},{nueva_area[3]}\n")
        except FileNotFoundError:
            # Si no existe, crear con header
            with open(copia, "w", encoding="utf-8") as cop:
                cop.write("id,nombre,cantidad,estado\n")
                cop.write(f"{nueva_area[0]},{nueva_area[1]},{nueva_area[2]},{nueva_area[3]}\n")
        
        # Reemplazar archivo original con el temporal
        if os.path.exists(CSV_AREAS):
            os.remove(CSV_AREAS)
        os.rename(copia, CSV_AREAS)
        
        print(VERDE + f"Area {nombre_area} registrada con exito!" + RESET)
        return nueva_area
        
    except (PermissionError, IOError, OSError) as e:
        print(ROJO + f"Error al registrar área: {e}" + RESET)
        # Limpiar archivo temporal si existe
        if os.path.exists("matrices/copia_area.csv"):
            try:
                os.remove("matrices/copia_area.csv")
            except:
                pass
        return None

def EstadisticasAreas():
    """Muestra estadísticas de áreas leyendo desde CSV."""
    try:
        areas = leer_areas_csv(skip_header=True)
        empleados = leer_empleados_csv(skip_header=True)
        
        print(AZUL + "="*43 + RESET)
        print(AZUL + "MENU PRINCIPAL -> AREAS -> ESTADISTICAS" + RESET)
        print(AZUL + "="*43 + RESET)
        print(CIAN + "| Opciones:".ljust(42) + "|" + RESET)
        print(CIAN + "| 1 - Ver promedio de empleados por area".ljust(42) + "|" + RESET)
        print(CIAN + "| 0 - Volver".ljust(42) + "|" + RESET)
        print(AZUL + "="*43 + RESET)
        opcion = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
        match opcion:
            case 1:
                promedio_empleados_por_area(empleados, areas)
            case 0:
                return
            case _:
                print(AMARILLO + "Opcion no valida." + RESET)
                print(AZUL + "="*130 + RESET)
                print()
                print(VERDE + "ESTADISTICAS FINALIZADAS" + RESET)
                print(AZUL + "="*130 + RESET)
    except Exception as e:
        print(ROJO + f"Error al obtener estadísticas: {e}" + RESET)
    
#Buscar Area
def BuscarArea():
    """Busca áreas en el archivo CSV por diferentes criterios."""
    try:
        print(AZUL + "MENU PRINCIPAL -> AREAS -> BUSCADOR" + RESET)
        print(AZUL + "="*34 + RESET)
        print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
        print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
        print(CIAN + "| 2 - Nombre".ljust(33) + "|" + RESET)
        print(CIAN + "| 3 - Mostrar areas".ljust(33) + "|" + RESET)
        print(CIAN + "| 4 - Volver".ljust(33) + "|" + RESET)
        print(AZUL + "="*34 + RESET)
        opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
        print()
        match opcion:
            case 1:
                # Búsqueda optimizada línea por línea (sin cargar todo)
                busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
                resultado = buscar_en_csv_linea_por_linea(CSV_AREAS, busqueda, 0, skip_header=True)
                if resultado:
                    print(VERDE + f"Área encontrada: ID={resultado[0]}, Nombre={resultado[1]}, Cantidad={resultado[2]}, Estado={resultado[3]}" + RESET)
                else:
                    print(AMARILLO + "Área no encontrada." + RESET)
            case 2:
                # Búsqueda optimizada línea por línea (sin cargar todo)
                busqueda = input(MAGENTA + "Ingrese el nombre a buscar: " + RESET)
                busqueda = busqueda.lower()
                resultado = buscar_en_csv_linea_por_linea(CSV_AREAS, busqueda, 1, skip_header=True)
                if resultado:
                    print(VERDE + f"Área encontrada: ID={resultado[0]}, Nombre={resultado[1]}, Cantidad={resultado[2]}, Estado={resultado[3]}" + RESET)
                else:
                    print(AMARILLO + "Área no encontrada." + RESET)
            case 3:
                # Para mostrar todas, necesitamos cargar en memoria (para ordenar)
                areas = leer_areas_csv(skip_header=True)
                key = lambda fila : fila[0]
                Imprimir_Matriz_Ordenada(areas, 1, key)
            case 4:
                return
    except Exception as e:
        print(ROJO + f"Error al buscar área: {e}" + RESET) 
        
#Editar Area
def EditarArea():
    """Edita un área existente en el archivo CSV."""
    try:
        # Leer áreas desde CSV
        areas = leer_areas_csv(skip_header=True)
        
        print(AZUL + "="*26 + RESET)
        id_area = Ingresar_Numero(MAGENTA + 'Escriba el id de la area a editar: ' + RESET)
        
        # Buscar el área por ID
        area_encontrada = None
        indice_area = -1
        for i, area in enumerate(areas):
            if area[0] == id_area:
                area_encontrada = area
                indice_area = i
                break
        
        if area_encontrada is None:
            print(ROJO + "El id ingresado no es valido" + RESET)
            return
        
        print(CIAN + f"Area encontrada: {area_encontrada}" + RESET)
        print(AZUL + "Que campo quiere editar?" + RESET)
        print(CIAN + '1. Nombre' + RESET)
        print(CIAN + '2. Cantidad' + RESET)
        valueTochange = Ingresar_Numero(MAGENTA + 'Seleccione una opcion: ' + RESET)
        
        if valueTochange == 1:
            newName = input(MAGENTA + 'Ingrese el nuevo nombre: ' + RESET)
            areas[indice_area][1] = newName
            print(VERDE + f"Area actualizada: {areas[indice_area]}" + RESET)
        elif valueTochange == 2:
            newCantidad = Ingresar_Numero(MAGENTA + 'Ingrese la nueva cantidad: ' + RESET)
            areas[indice_area][2] = newCantidad
            print(VERDE + f"Area actualizada: {areas[indice_area]}" + RESET)
        else:
            print(ROJO + "Opción no válida" + RESET)
            return
        
        # Escribir los cambios de vuelta al CSV
        escribir_areas_csv(areas, incluir_header=True)
        print(VERDE + "Cambios guardados exitosamente." + RESET)
        
    except Exception as e:
        print(ROJO + f"Error al editar área: {e}" + RESET)
    
#Eliminar Area
def EliminarArea():
    """Elimina (marca como Inactivo) un área en el archivo CSV y actualiza dependencias."""
    try:
        # Leer áreas desde CSV
        areas = leer_areas_csv(skip_header=True)
        
        print(AZUL + "="*26 + RESET)
        areaEliminar = str(input(MAGENTA + "Escriba el nombre del area o escriba \"Lista\" para obtener la planilla: " + RESET)).lower()
        
        if areaEliminar == "lista":
            print(AZUL + "Lista de areas:" + RESET)
            Imprimir_Matriz_Ordenada(areas, 1, lambda fila: fila[0])
            return
        
        # Buscar área por nombre
        area_encontrada = None
        indice_area = -1
        for i, area in enumerate(areas):
            if area[1].lower() == areaEliminar:
                area_encontrada = area
                indice_area = i
                break
        
        if area_encontrada is None:
            print(ROJO + f"Area {areaEliminar} no encontrada." + RESET)
            return
        
        # Marcar área como Inactivo
        id_area = area_encontrada[0]
        areas[indice_area][3] = "Inactivo"
        
        # Escribir cambios en áreas
        escribir_areas_csv(areas, incluir_header=True)
        
        # Leer empleados y marcar como Inactivos los del área eliminada
        empleados_data = leer_empleados_csv(skip_header=True)
        id_empleados_afectados = []
        for i, emp in enumerate(empleados_data):
            if emp[4] == id_area:
                empleados_data[i][5] = "Inactivo"
                id_empleados_afectados.append(emp[0])
        
        # Escribir cambios en empleados
        if id_empleados_afectados:
            escribir_empleados_csv(empleados_data, incluir_header=True)
        
        # Leer licencias y marcar como Inactivas las de empleados afectados
        licencias_data = leer_licencias_csv(skip_header=True)
        for i, lic in enumerate(licencias_data):
            if lic[1] in id_empleados_afectados:
                licencias_data[i][4] = "Inactivo"
        
        # Escribir cambios en licencias
        if id_empleados_afectados:
            escribir_licencias_csv(licencias_data, incluir_header=True)
        
        print(VERDE + f"Area '{area_encontrada[1]}' eliminada (marcada como Inactivo)." + RESET)
        if id_empleados_afectados:
            print(VERDE + f"{len(id_empleados_afectados)} empleados y sus licencias marcados como Inactivos." + RESET)
        
    except Exception as e:
        print(ROJO + f"Error al eliminar área: {e}" + RESET)
    

if __name__ == "__main__":
    print(AZUL + "Modulo de Areas - Sistema CRUD basado en archivos CSV" + RESET)
    print(AZUL + "="*55 + RESET)
   