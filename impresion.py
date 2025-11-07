
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

import re
import json
from dataset import archivos, justificaciones

# Funciones auxiliares para leer archivos

# def leer_justificaciones_csv():
#     """Lee el archivo justificaciones.csv y retorna una lista de listas."""
#     justificaciones = []
#     try:
#         with open(CSV_JUSTIFICACIONES, "r", encoding="utf-8") as f:
#             next(f, None)  # Saltar header
#             for line in f:
#                 line = line.strip()
#                 if not line:
#                     continue
#                 datos = line.split(",")
#                 datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
#                 justificaciones.append(datos)
#     except FileNotFoundError:
#         pass
#     return justificaciones

def leer_usuarios_json():
    """Lee el archivo usuarios.json y retorna la lista de usuarios."""
    try:
        with open(r'dataset/usuarios.json', "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

#Funciones 
# def Imprimir_Opciones(matriz, columna):
#     print()
#     print(AZUL + "Opciones: " + RESET)
#     for i in range(len(matriz)):
#         print(CIAN + f"{i} - {matriz[i][columna]}" + RESET)

def Imprimir_Encabezados(fila):
    encabezados = [
        ["id",	"N/A", "Telefono", "Posición", "id_Area", "Estado", "F_ingreso", "F_nacimiento"], # Empleados 
        ["Id", "Nombre", "Cantidad", "Estado"], # Areas
        ["Id", "Empleado", "Fecha","Justificacion", "Estado"], # Licencias
        ["Id", "Justificación", "Tipo"], # Justificaciones
        ["Operacion", "Entidad Afectada", "Fecha"] # Historial de Operaciones
    ]
    for i in range(len(encabezados)):
        if i < 2:
            encabezados[i] = list(map(lambda x: x.ljust(21), encabezados[i]))
        else:
            encabezados[i] = list(map(lambda x: x.ljust(23), encabezados[i]))
    for i in encabezados[fila]:
        print(i, end= "\t")
    print()
    return

def Rellenar(nombre):
    nombre = str(nombre)
    nombre = nombre.ljust(8)
    return nombre

def Formato(nombre):
    nombre = str(nombre)
    if len(nombre) > 7:
        nombre = nombre.split()
        cort = []
        cort.append(nombre[0])
        if len(nombre) < 3:
            for n in nombre[1:]:
                if len(n) > 3:
                    n = n[:3] + ".."
                cort.append(n)
            cort = " ".join(cort)
            nombre = cort
        else:
            cort.append(nombre[1][:3] + "..")
            nombre = " ".join(cort)

    elif len(str(nombre)) < 8:
       nombre = Rellenar(nombre)

    nombre = nombre.ljust(20)
    return nombre

# def Imprimir_Matriz_Ordenada(matriz, encabezado, llave):
#     filas = len(matriz)
#     columnas = len(matriz[0])

#     matriz.sort(key=llave)
#     print(AZUL + "="*180 + RESET)
#     Imprimir_Encabezados(encabezado)
#     print(AZUL + "-"*180 + RESET)
#     for i in range(filas):
#         if "Inactivo" not in matriz[i]:
#             for j in range(columnas):
#                 impresion = matriz[i][j]
#                 impresion = Reemplazo_Id_Valor(impresion, j)
#                 if encabezado == 0:
#                     impresion = Formato(impresion)
#                 else:
#                     impresion = str(impresion).ljust(24)
#                 print(impresion, end="\t")
#             print()
#             print(AZUL + "-"*180 + RESET)
#     print(AZUL + "="*180 + RESET)
#     print()
#     return
        
    
def Buscar_id_archivo(archivo, id):
    try: 
        with open(archivo, 'r', encoding='UTF-8') as arch:
            encontrado = False
            skip = True
            lineas = arch.readline().strip()
            while lineas:
                if skip:
                    skip = False
                    lineas = arch.readline().strip()
                    continue
                columnas = lineas.strip().split(",")
                if int(columnas[0]) == id:
                    impresion = columnas[1]
                    encontrado = True
                lineas = arch.readline().strip()
            if encontrado:
                return impresion
            else:
                return str(id)
    except OSError as error:
        print("No se pudo imprimir el archivo:", error)


def Reemplazo_Id_Valor(id, reemplazar):
    id = str(id)
    if id.isnumeric():
        id = int(id)
        columna = reemplazar
        match columna:
            case 1:
                valor = Buscar_id_archivo(archivos[0], id)
            case 3:
                valor = justificaciones[id][1]
            case 4:
                valor = Buscar_id_archivo(archivos[1], id)
            case _:
                valor = id

        return valor
    else:
        return id

def Imprimir_Diccionario_Ordenada(clave):
    usuarios = leer_usuarios_json()
    if not usuarios:
        print(AMARILLO + "No hay usuarios para mostrar" + RESET)
        return
    usuarios.sort(key=lambda x: x[clave])
    print(AZUL + "="*170 + RESET)
    for i in usuarios[0].keys():
        print (i.ljust(23),end="\t")
    print()
    print(AZUL + "-"*170 + RESET)
    for i in range(len(usuarios)):
        if "Inactivo" not in usuarios[i].values():
            for j in usuarios[i].keys():
                impresion = str(usuarios[i][j])
                print(impresion.ljust(23), end="\t")
            print()
            print(AZUL + "-"*170 + RESET)
    print(AZUL + "="*170 + RESET)
    print()
    return 

def formato_dni(dni):
    patron= re.compile (dni)
    impresion_dni=patron.sub(dni[:-6]+'.'+dni[-6:-3]+'.'+ dni[-3: ],dni)
    return impresion_dni

def Mostrar_historial_operaciones(historial):
    print(AZUL + "="*170 + RESET)
    print(AZUL + "HISTORIAL DE OPERACIONES".ljust(60) + RESET)
    print(AZUL + "="*170 + RESET)
    Imprimir_Encabezados(4)
    print(AZUL + "-"*170 + RESET)
    for op in historial:
        for dato in op:
            dato = str(dato)
            print(dato.ljust(24), end="\t")
        print()
        print(AZUL + "-"*170 + RESET)

def impresion_recursiva_formateada(columnas, encabezado, i=0):
    if len(columnas) > 0:
        impresion = Reemplazo_Id_Valor(columnas[0], i)
        if encabezado == 0 or encabezado == 1:
            impresion = Formato(impresion)
        print(str(impresion).ljust(23), end="\t")
        impresion_recursiva_formateada(columnas[1:], encabezado, i + 1)

def imprimir_archivo(archivo, encabezado):
    try:
        skip = True
        with open(archivo, 'r', encoding='UTF-8') as datos:
            lineas = datos.readline().strip()
            print(AZUL + "="*185 + RESET)
            Imprimir_Encabezados(encabezado)
            print(AZUL + "-"*185 + RESET)
            while lineas:
                if skip:
                    skip = False
                    lineas = datos.readline().strip()
                    continue
                columnas = lineas.strip().split(",")
                # for col in range(len(columnas)):
                #     impresion = Reemplazo_Id_Valor(columnas[col], col)
                #     if encabezado == 0:
                #         impresion = Formato(impresion)
                #     print(str(impresion).ljust(23), end="\t")
                impresion_recursiva_formateada(columnas, encabezado)

                print()
                print(AZUL + "-"*185 + RESET)
                lineas = datos.readline().strip()
    except OSError:
        print("No se encontró el archivo")

    return

if __name__ == "__main__":
    # Ejemplo: imprimir archivo de empleados
    imprimir_archivo(archivos[0], 0)