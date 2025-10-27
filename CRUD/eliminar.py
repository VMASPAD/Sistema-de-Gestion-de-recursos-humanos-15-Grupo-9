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
def Eliminar_ClaveForanea():
    return

def eliminar_entidad_archivo(archivo, empleado, columna_id, columna):
    copia = r'matrices/copia.txt'
    encontrado = False
    if archivo == archivos[0]:
        ent = "empleado"
    elif archivo == archivos[1]:
        ent = "area"
    elif archivo == archivos[2]:
        ent = "licencia"
    try:
        arch = open(archivo, 'rt', encoding='UTF-8') 
        cop = open(copia, 'wt', encoding='UTF-8') 

        for linea in arch:
            datos = linea.strip().split(";")
            id = int(datos[columna_id])

            if empleado == id:
                encontrado = True
                datos[columna] = "Inactivo"
                nueva_linea = str(datos[0])
                for dato in range(len(datos)):
                    if dato == 0:
                        continue
                    else:
                        nueva_linea += ";" + str(datos[dato])
                nueva_linea += "\n"
                cop.write(nueva_linea)
                print(f"Se elimino {ent} con id: {datos[0]}")
            else:
                cop.write(linea)
    except FileNotFoundError:
        print("No se encontró el archivo")
    except OSError as error:
        print("No se pudo editar al empleado:", error) 
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
            print("No se encontro al empleado con id:", empleado)
        except OSError:
            print("Error al eliminar el archivo")
    return encontrado

if __name__ == "__main__":
    eliminar_entidad_archivo(archivos[2], 11, 0, 4)