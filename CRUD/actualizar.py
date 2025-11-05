import os 
from CRUD.eliminar import Modificar_cantidad_area
from config import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS
from CRUD.csv_utils import modificar_entidad_csv

#Funciones 
def editar_entidad_archivo(archivo, entidad, columna, columna_id, edicion):
    """
    Edita una entidad en el archivo CSV.
    Usa csv_utils para reducir duplicación.
    
    Args:
        archivo: Ruta del archivo CSV a editar
        entidad: ID de la entidad a buscar
        columna: Índice de la columna a editar
        columna_id: Índice de la columna que contiene el ID
        edicion: Nuevo valor para la columna
    
    Returns:
        bool: True si se encontró y editó la entidad, False en caso contrario
    """
    if archivo == CSV_EMPLEADOS:
        ent = "empleado"
    elif archivo == CSV_AREAS:
        ent = "area"
    elif archivo == CSV_LICENCIAS:
        ent = "licencia"
    else:
        ent = "entidad"
    
    # Condición especial para reactivar empleados
    def condicion(datos):
        if archivo == CSV_EMPLEADOS and columna == 5:
            if datos[columna] != "Inactivo":
                print(f"{ent} ya se encuentra activo")
                return False
            # Actualizar cantidad de área al reactivar
            Modificar_cantidad_area(operacion=True, area=int(datos[4]))
        return True
    
    encontrado, datos_modificados = modificar_entidad_csv(
        archivo, entidad, columna_id, columna, edicion, condicion
    )
    
    if encontrado:
        print(f"Se editó {ent} {datos_modificados[1]}")
    else:
        print(f"No se encontro {ent} con id:", entidad)
    
    return encontrado
#Programa principal  
if __name__ == '__main__':
    editar_entidad_archivo('matrices/empleados.txt', 15, 1, 'Juan Lopez')