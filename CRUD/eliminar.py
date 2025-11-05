import os
from config import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS
from CRUD.csv_utils import modificar_multiple_csv

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


#Funciones 
def Eliminar_ClaveForanea(entidad_tipo, entidad_id):
    """
    Elimina claves foráneas en cascada cuando se elimina una entidad principal.
    Marca como "Inactivo" todas las entidades relacionadas.
    Usa csv_utils para evitar duplicación de código.
    
    Args:
        entidad_tipo: Tipo de entidad principal ("area", "empleado")
        entidad_id: ID de la entidad principal eliminada
    
    Returns:
        dict: Diccionario con contadores de entidades afectadas por tipo
    """
    afectados = {"empleados": 0, "licencias": 0}
    empleados_a_inactivar = []
    
    try:
        if entidad_tipo == "area":
            # Marcar empleados del área como Inactivos
            def condicion_empleado(datos):
                if len(datos) >= 6:
                    area_empleado = int(datos[4]) if datos[4].isdigit() else datos[4]
                    return area_empleado == entidad_id and datos[5] == "Activo"
                return False
            
            def modificacion_empleado(datos):
                id_empleado = int(datos[0]) if datos[0].isdigit() else datos[0]
                empleados_a_inactivar.append(id_empleado)
                datos[5] = "Inactivo"
                return datos
            
            afectados["empleados"] = modificar_multiple_csv(CSV_EMPLEADOS, condicion_empleado, modificacion_empleado)
            
            # Marcar licencias de empleados afectados como Inactivas
            if empleados_a_inactivar:
                def condicion_licencia(datos):
                    if len(datos) >= 5:
                        id_emp_lic = int(datos[1]) if datos[1].isdigit() else datos[1]
                        return id_emp_lic in empleados_a_inactivar and datos[4] == "Activo"
                    return False
                
                def modificacion_licencia(datos):
                    datos[4] = "Inactivo"
                    return datos
                
                afectados["licencias"] = modificar_multiple_csv(CSV_LICENCIAS, condicion_licencia, modificacion_licencia)
        
        elif entidad_tipo == "empleado":
            # Marcar licencias del empleado como Inactivas
            def condicion_licencia(datos):
                if len(datos) >= 5:
                    id_emp_lic = int(datos[1]) if datos[1].isdigit() else datos[1]
                    return id_emp_lic == entidad_id and datos[4] == "Activo"
                return False
            
            def modificacion_licencia(datos):
                datos[4] = "Inactivo"
                return datos
            
            afectados["licencias"] = modificar_multiple_csv(CSV_LICENCIAS, condicion_licencia, modificacion_licencia)
        
        return afectados
        
    except Exception as e:
        print(ROJO + f"Error al eliminar claves foráneas: {e}" + RESET)
        return afectados

def eliminar_entidad_archivo(archivo, empleado, columna_id, columna):
    """
    Marca una entidad como "Inactivo" en el archivo CSV.
    Usa csv_utils para reducir duplicación.
    
    Args:
        archivo: Ruta del archivo CSV
        empleado: ID de la entidad a eliminar (marcar como Inactivo)
        columna_id: Índice de la columna que contiene el ID
        columna: Índice de la columna de estado (Activo/Inactivo)
    
    Returns:
        bool: True si se encontró y eliminó la entidad, False en caso contrario
    """
    from CRUD.csv_utils import modificar_entidad_csv
    
    if archivo == CSV_EMPLEADOS:
        ent = "empleado"
    elif archivo == CSV_AREAS:
        ent = "area"
    elif archivo == CSV_LICENCIAS:
        ent = "licencia"
    else:
        ent = "entidad"
    
    # Condición: debe estar Activo
    def condicion(datos):
        if datos[columna] != "Activo":
            print(f"{ent} ya se encontraba Inactivo")
            return False
        return True
    
    encontrado, datos_modificados = modificar_entidad_csv(
        archivo, empleado, columna_id, columna, "Inactivo", condicion
    )
    
    if encontrado:
        print(f"Se elimino {ent} con id: {datos_modificados[0]}")
        # Si es empleado, actualizar cantidad de área
        if archivo == CSV_EMPLEADOS and len(datos_modificados) > 4:
            Modificar_cantidad_area(operacion=False, area=int(datos_modificados[4]))
    else:
        print(f"No se encontro {ent} con id:", empleado)
    
    return encontrado

def formateado_recursivo(lista, nl):
    """
    Formatea recursivamente una lista en una cadena CSV.
    Concatena elementos de la lista con comas.
    
    Args:
        lista: Lista de valores a formatear
        nl: String acumulador con el formato actual
    
    Returns:
        str: String formateado en formato CSV
    """ 
    if len(lista) > 0:
        nl += "," + str(lista[0])
        nl = formateado_recursivo(lista[1:], nl)
        return nl
    else:
        return nl
def Modificar_cantidad_area(operacion, area):
    """
    Modifica la cantidad de empleados en un área específica.
    Usa csv_utils para reducir duplicación.
    
    Args:
        operacion: True para sumar, False para restar
        area: ID del área a modificar
    """ 
    from CRUD.csv_utils import modificar_entidad_csv
    
    try:
        # Leer valor actual
        with open(CSV_AREAS, 'r', encoding='UTF-8') as f:
            lineas = f.readlines()
        
        for i in range(1, len(lineas)):
            datos = lineas[i].strip().split(",")
            if len(datos) >= 3:
                id_area = int(datos[0]) if datos[0].isdigit() else datos[0]
                if id_area == area:
                    cantidad_actual = int(datos[2])
                    nuevo_valor = cantidad_actual + 1 if operacion else cantidad_actual - 1
                    modificar_entidad_csv(CSV_AREAS, area, 0, 2, nuevo_valor)
                    break
    except Exception as e:
        print(ROJO + f"Error al modificar cantidad de área: {e}" + RESET)
                    

if __name__ == "__main__":
    # Ejemplo de uso: eliminar_entidad_archivo(CSV_EMPLEADOS, 15, 0, 5)
    pass