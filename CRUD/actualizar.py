import os 
from dataset import archivos
from CRUD.eliminar import Modificar_cantidad_area
#Funciones 
def editar_entidad_archivo(archivo, entidad, columna,columna_id, edicion):
    copia = r'matrices/copia.txt'
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
        arch = open(archivo, 'rt', encoding='UTF-8') 
        cop = open(copia, 'wt', encoding='UTF-8') 

        for linea in arch:
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
    finally:
        try:
            arch.close()
            cop.close()
        except:
            print("Error al cierre del archivo")
    if encontrado:
        try:
            os.remove(archivo)
            os.rename(copia, archivo)
        except OSError:
            print("Error al eliminar archivo")
    else:
        try:
            os.remove(copia)
            print(f"No se encontro {ent} con id:", entidad)
        except OSError:
            print("Error al eliminar el archivo")
    return encontrado
#Programa principal  
if __name__ == '__main__':
    editar_entidad_archivo('matrices/empleados.txt', 15, 1, 'Juan Lopez')