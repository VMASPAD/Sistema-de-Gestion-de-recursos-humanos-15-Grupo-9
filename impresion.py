
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

import re
from dataset import empleados, areas, justificaciones, licencias, historial_operaciones, usuarios
#Funciones 
def Imprimir_Opciones(matriz, columna):
    print()
    print(AZUL + "Opciones: " + RESET)
    for i in range(len(matriz)):
        print(CIAN + f"{i} - {matriz[i][columna]}" + RESET)

def Imprimir_Encabezados(fila):
    encabezados = [
        ["id",	"N/A", "Telefono", "Posición", "id_Area", "Estado", "F_ingreso", "F_nacimiento"], # Empleados 
        ["Id", "Nombre", "Cantidad", "Estado"], # Areas
        ["Id", "Empleado", "Fecha","Justificacion", "Estado"], # Licencias
        ["Id", "Justificación", "Tipo"], # Justificaciones
        ["Operacion", "Entidad Afectada", "Fecha"] # Historial de Operaciones
    ]
    for i in encabezados[fila]:
        if fila == 0:
            i = i.ljust(21)
        else:
            i = i.ljust(24)
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

def Imprimir_Matriz_Ordenada(matriz, encabezado, llave):
    filas = len(matriz)
    columnas = len(matriz[0])

    matriz.sort(key=llave)
    print(AZUL + "="*180 + RESET)
    Imprimir_Encabezados(encabezado)
    print(AZUL + "-"*180 + RESET)
    for i in range(filas):
        if "Inactivo" not in matriz[i]:
            for j in range(columnas):
                impresion = matriz[i][j]
                impresion = Reemplazo_Id_Valor(impresion, j)
                if encabezado == 0:
                    impresion = Formato(impresion)
                else:
                    impresion = str(impresion).ljust(24)
                print(impresion, end="\t")
            print()
            print(AZUL + "-"*180 + RESET)
    print(AZUL + "="*180 + RESET)
    print()
    return

def Encontrar_Id_Empleado(empleados, empleado):
    id = list(filter(lambda x: empleado in x[1].lower(), empleados))    
    if id:
        return id[0][0]
    else:
        print(ROJO + "Empleado no encontrado" + RESET) 
        return False

def Reemplazo_Id_Valor(id, reemplazar):
    id = str(id)
    if id.isnumeric():
        id = int(id)
        columna = reemplazar
        match columna:
            case 1:
                valor = empleados[id][1]
            case 3:
                valor = justificaciones[id][1]
            case 4:
                valor = areas[id][1]
            case _:
                valor = id

        return valor
    else:
        return id

def Imprimir_Diccionario_Ordenada(usuarios, clave):
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

def imprimir_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='UTF-8') as datos:
            lineas = datos.readline().strip()
            while lineas:
                columnas = lineas.strip().split(";")
                for col in range(len(columnas)):
                    print(str(columnas[col]).ljust(20), end="\t")
                print()
                lineas = datos.readline().strip()
    except OSError:
        print("No se encontró el archivo")

    return

if __name__ == "__main__":
    Imprimir_Matriz_Ordenada(empleados, 0, lambda fila: fila[0])