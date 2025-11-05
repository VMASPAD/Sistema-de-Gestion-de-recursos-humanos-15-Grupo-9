import os
from main import CSV_AREAS, CSV_EMPLEADOS, CSV_LICENCIAS

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


#Funciones 
def Eliminar_ClaveForanea(id_area):
    """
    Elimina en cascada todas las dependencias de un área.
    Marca como Inactivo: área, empleados del área, y licencias de esos empleados.
    Utiliza archivos temporales para cada operación sin cargar en memoria.
    
    Args:
        id_area: ID del área a eliminar en cascada
    
    Returns:
        tuple: (empleados_afectados, licencias_afectadas)
    """
    empleados_afectados = []
    
    # 1. Marcar empleados del área como Inactivo
    copia_emp = 'matrices/copia_empleados_temp.csv'
    try:
        with open(CSV_EMPLEADOS, 'r', encoding='UTF-8') as arch, \
             open(copia_emp, 'w', encoding='UTF-8') as copia:
            
            # Copiar header
            header = arch.readline()
            copia.write(header)
            
            # Procesar cada empleado
            for linea in arch:
                datos = linea.strip().split(",")
                if len(datos) >= 6:
                    emp_area = int(datos[4]) if datos[4].isdigit() else datos[4]
                    if emp_area == id_area and datos[5] == "Activo":
                        # Marcar como Inactivo y guardar ID
                        datos[5] = "Inactivo"
                        empleados_afectados.append(int(datos[0]) if datos[0].isdigit() else datos[0])
                
                # Escribir línea (modificada o no)
                copia.write(",".join(map(str, datos)) + "\n")
        
        # Reemplazar archivo original
        os.remove(CSV_EMPLEADOS)
        os.rename(copia_emp, CSV_EMPLEADOS)
        
    except (FileNotFoundError, OSError) as e:
        print(ROJO + f"Error al eliminar empleados: {e}" + RESET)
        if os.path.exists(copia_emp):
            os.remove(copia_emp)
    
    # 2. Marcar licencias de empleados afectados como Inactivo
    licencias_afectadas = 0
    if empleados_afectados:
        copia_lic = 'matrices/copia_licencias_temp.csv'
        try:
            with open(CSV_LICENCIAS, 'r', encoding='UTF-8') as arch, \
                 open(copia_lic, 'w', encoding='UTF-8') as copia:
                
                # Copiar header
                header = arch.readline()
                copia.write(header)
                
                # Procesar cada licencia
                for linea in arch:
                    datos = linea.strip().split(",")
                    if len(datos) >= 5:
                        id_emp = int(datos[1]) if datos[1].isdigit() else datos[1]
                        if id_emp in empleados_afectados and datos[4] == "Activo":
                            datos[4] = "Inactivo"
                            licencias_afectadas += 1
                    
                    # Escribir línea (modificada o no)
                    copia.write(",".join(map(str, datos)) + "\n")
            
            # Reemplazar archivo original
            os.remove(CSV_LICENCIAS)
            os.rename(copia_lic, CSV_LICENCIAS)
            
        except (FileNotFoundError, OSError) as e:
            print(ROJO + f"Error al eliminar licencias: {e}" + RESET)
            if os.path.exists(copia_lic):
                os.remove(copia_lic)
    
    return (len(empleados_afectados), licencias_afectadas)

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
    copia = 'matrices/copia.csv'
    encontrado = False
    cantidad = False
    if archivo == CSV_EMPLEADOS:
        ent = "empleado"
        cantidad = True
    elif archivo == CSV_AREAS:
        ent = "area"
    elif archivo == CSV_LICENCIAS:
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

            if empleado == id:
                assert datos[columna] == "Activo"
                encontrado = True
                datos[columna] = "Inactivo"
                if cantidad:
                    Modificar_cantidad_area(operacion= False, area=int(datos[4]))
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
        with open(CSV_AREAS, 'r', encoding='UTF-8') as arch, open(r'matrices/copia2.csv', 'w', encoding='UTF-8') as copia:
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
        os.remove(CSV_AREAS)
        os.rename(r'matrices/copia2.csv', CSV_AREAS)
    except OSError as e:
        print(ROJO + f"Error al reemplazar archivo de áreas: {e}" + RESET)
                    

if __name__ == "__main__":
    # Ejemplo de uso: eliminar_entidad_archivo(CSV_EMPLEADOS, 15, 0, 5)
    pass