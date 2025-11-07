import os
from dataset import archivos 

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


#Funciones 
def eliminar_entidad_archivo(archivo, empleado, columna_id, columna):
    """
    Marca una entidad como "Inactivo" en el archivo CSV sin cargar todo en memoria.
    Procesa el archivo línea por línea, escribe en temporal y reemplaza el original.
    
    Args:
        archivo: Ruta del archivo CSV
        empleado: ID de la entidad a eliminar (marcar como Inactivo)
        columna_id: Índice de la columna que contiene el ID
        columna: Índice de la columna de estado (Activo/Inactivo)
    
    Returns:
        bool: True si se encontró y eliminó la entidad, False en caso contrario
    """
    encontrado = False
    cantidad = False
    if archivo == archivos[0]:
        ent = "empleado"
        cantidad = True
    elif archivo == archivos[1]:
        ent = "area"
    elif archivo == archivos[2]:
        ent = "licencia"
    copia = f'matrices/copia{ent}.csv'
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

            if empleado == id:
                assert datos[columna] == "Activo"
                encontrado = True
                datos[columna] = "Inactivo"
                if cantidad:
                    Modificar_cantidad_area(operacion= False, area=int(datos[4]))
                    eliminar_entidad_archivo(archivos[2], empleado, 1, 4)
                nueva_linea = str(datos[0])
                for dato in range(len(datos)):
                    if dato == 0:
                        continue
                    else:
                        nueva_linea += "," + str(datos[dato])
                nueva_linea += "\n"
                cop.write(nueva_linea)
                print(f"Se elimino {ent} con id: {datos[0]}")
            else:
                cop.write(linea)
    except FileNotFoundError:
        print("No se encontró el archivo")
    except OSError as error:
        print("No se pudo editar al empleado:", error)
    except AssertionError:
        print(f"{ent} ya se encontraba Inactivo")
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
            print(ROJO + f"Error al reemplazar archivo: {e}" + RESET)
    else:
        print("No se encontro al empleado con id:", empleado)
        # Eliminar archivo temporal si no se encontró nada
        if os.path.exists(copia):
            os.remove(copia)
    
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
    Modifica la cantidad de empleados en un área específica sin cargar archivo en memoria.
    Procesa el archivo línea por línea y actualiza el contador.
    
    Args:
        operacion: True para sumar, False para restar
        area: ID del área a modificar
    """ 
    #True : Sumar // False : Restar
    try: 
        with open(archivos[1], 'r', encoding='UTF-8') as arch, open(r'matrices/copia2.csv', 'w', encoding='UTF-8') as copia:
            skip = True
            for linea in arch:
                if skip:
                    skip = False
                    copia.write(linea)
                    continue
                datos = linea.strip().split(",")
                id_area = int(datos[0])
                if id_area == area:
                    if operacion:
                        datos[2] = int(datos[2]) + 1
                    else:
                        datos[2] = int(datos[2]) - 1
                    nueva_linea = str(datos[0])
                    # for i in range(len(datos)):
                    #     if i == 0:
                    #         continue
                    #     else:
                    #         nueva_linea += "," + str(datos[i])
                    nueva_linea = formateado_recursivo(datos[1:], nueva_linea)
                    nueva_linea += "\n"
                    copia.write(nueva_linea)
                else:
                    copia.write(linea)
    except FileNotFoundError:
        print("No se encontró el archivo")
    except OSError as error:
        print("Ocurrió un error: ", error)
    except IndexError:
        print("Archivo vacío")
    except:
        print("Error!")
    
    # Reemplazar archivo original con el temporal
    try:
        os.remove(archivos[1])
        os.rename(r'matrices/copia2.csv', archivos[1])
    except OSError as e:
        print(ROJO + f"Error al reemplazar archivo de áreas: {e}" + RESET)
                    

if __name__ == "__main__":
    # Ejemplo de uso: eliminar_entidad_archivo(archivos[0], 15, 0, 5)
    pass