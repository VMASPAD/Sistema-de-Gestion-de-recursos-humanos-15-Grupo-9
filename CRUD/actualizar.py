import os 
from CRUD.eliminar import Modificar_cantidad_area
from dataset import archivos 

#Funciones 
def editar_entidad_archivo(archivo, entidad, columna, columna_id, edicion):
    """
    Edita una entidad en el archivo CSV procesando línea por línea sin cargar en memoria.
    Lee el archivo original, modifica la línea correspondiente y escribe en archivo temporal.
    Luego reemplaza el original con el temporal.
    
    Args:
        archivo: Ruta del archivo CSV a editar
        entidad: ID de la entidad a buscar
        columna: Índice de la columna a editar
        columna_id: Índice de la columna que contiene el ID
        edicion: Nuevo valor para la columna
    
    Returns:
        bool: True si se encontró y editó la entidad, False en caso contrario
    """
    copia = r'matrices/copia.csv'
    encontrado = False
    cantidad = False
    if archivo == archivos[0]:
        ent = "empleado"
        cantidad = True
    elif archivo == archivos[1]:
        ent = "area"
    elif archivo == archivos[2]:
        ent = "licencia"
    try:
        arch = open(archivo, 'r', encoding='UTF-8') 
        cop = open(copia, 'w', encoding='UTF-8') 
        skip = True
        for linea in arch:
            if skip:
                skip = False
                cop.write(linea)
                continue
            datos = linea.strip().split(",")
            id = int(datos[columna_id])

            if entidad == id:
                if cantidad and columna == 5:
                    assert datos[columna] == "Inactivo"
                    Modificar_cantidad_area(operacion=True, area=int(datos[4]))
                datos[columna] = edicion
                encontrado = True
                nueva_linea = str(datos[0])
                for dato in datos[1:]:
                    nueva_linea += "," + str(dato)
                nueva_linea += "\n"
                cop.write(nueva_linea)
                print(f"Se editó {ent} {datos[1]}")
            else:
                cop.write(linea)
    except FileNotFoundError:
        print("No se encontró el archivo")
    except OSError as error:
        print(f"No se pudo editar {ent}:", error) 
    except AssertionError:
        print(f"{ent} ya se encuentra activo")
    except IndexError:
        print("Archivo vacío")
    except:
        print("Error!")
    finally:
        try:
            arch.close()
            cop.close()
        except:
            print("Error al cierre del archivo")
    
    # Reemplazar archivo original con el temporal
    if encontrado:
        try:
            os.remove(archivo)
            os.rename(copia, archivo)
        except OSError as e:
            print(f"Error al reemplazar archivo: {e}")
    else:
        print(f"No se encontro {ent} con id:", entidad)
        # Eliminar archivo temporal si no se encontró nada
        if os.path.exists(copia):
            os.remove(copia)
    
    return encontrado
#Programa principal  
if __name__ == '__main__':
    editar_entidad_archivo('matrices/empleados.txt', 15, 1, 'Juan Lopez')