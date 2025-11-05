
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

import json
from impresion import Imprimir_Encabezados, Reemplazo_Id_Valor

# Funciones auxiliares locales

def leer_usuarios_json():
    """Lee el archivo usuarios.json y retorna la lista de usuarios."""
    try:
        with open("dataset/usuarios.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(AMARILLO + "Advertencia: dataset/usuarios.json no existe." + RESET)
        return []

def leer_empleados_csv():
    """Lee el archivo empleados.csv y retorna una lista de listas."""
    empleados = []
    try:
        with open("Matrices/empleados.csv", "r", encoding="utf-8") as f:
            next(f, None)  # Saltar header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                datos = line.split(",")
                if len(datos) >= 6:
                    datos[0] = int(datos[0]) if datos[0].isdigit() else datos[0]
                    datos[4] = int(datos[4]) if datos[4].isdigit() else datos[4]
                empleados.append(datos)
    except FileNotFoundError:
        print(AMARILLO + "Advertencia: Matrices/empleados.csv no existe." + RESET)
    return empleados
#Funciones 

def Encontrar(valor, matriz, columna, encabezado):
    existe = False
    print(AZUL + "="*185 + RESET)
    Imprimir_Encabezados(encabezado)
    print(AZUL + "-"*185 + RESET)
    for i in range(len(matriz)):
        valor = str(valor).lower()
        busqueda = matriz[i][columna]
        if valor.isnumeric():
            valor = int(valor)
            busqueda = [matriz[i][columna]]
        else:
            busqueda = busqueda.lower()
        if valor in busqueda:
            
            #mejorar impresion
            for j in range(len(matriz[i])):
                impresion = Reemplazo_Id_Valor(matriz[i][j], j)
                print(str(impresion).ljust(21), end= "\t")
            existe = True
            print()
            print(AZUL + "-"*185 + RESET)
    if not existe: print(ROJO + "No se encontro" + RESET), print(AZUL + "-"*185 + RESET)
    print(AZUL + "="*185 + RESET)

def Id_Empleado(empleado):
    empleados = leer_empleados_csv()
    emp = empleado.lower()
    id = bool([empleado[0] for empleado in empleados if emp in empleado[1].lower()])
    while not id:
        print(ROJO + "Empleado no encontrado, intente nuevamente" + RESET)
        emp = input(MAGENTA + "Ingrese el nombre o apellido del empleado: " + RESET).lower()
        id = bool([empleado[0] for empleado in empleados if emp in empleado[1].lower()])
    id = [empleado[0] for empleado in empleados if emp in empleado[1].lower()][0]
    return id

def Encontrar_diccionario(busqueda, clave, encabezado=None):
    usuarios = leer_usuarios_json()
    if not usuarios:
        print(ROJO + "No hay datos para buscar" + RESET)
        return

    # Resolver nombre de la clave si se pasó un índice
    clave = str(clave)
    if clave.isnumeric():
        clave = int(clave)
        keys = list(usuarios[0].keys())
        if clave < 0 or clave >= len(keys):
            print(ROJO + "Clave de búsqueda inválida" + RESET)
            return
        key = keys[clave]
    else:
        key = clave

    # Normalizar búsqueda y seleccionar por igualdad o substring
    resultado = []
    
    # si busqueda es numérica o un entero, comparar por igualdad
    bstr = str(busqueda)
    if bstr.isnumeric():
        bstr = str(busqueda)
        for item in usuarios:
            if str(item.get(key)) == bstr:
                resultado.append(item)
    else:
        b = str(busqueda).lower()
        for item in usuarios:
            val = item.get(key)
            if val is None:
                continue
            if b in str(val).lower():
                resultado.append(item)
    

    # Imprimir resultados formateados
    print(AZUL + "="*170 + RESET)
    for i in usuarios[0].keys():
        print (i.ljust(23),end="\t")
    print()
    print(AZUL + "="*170 + RESET)
    print(AZUL + "-"*170 + RESET)
    for res in resultado:
        for j in res.keys():
            print(str(res[j]).ljust(23), end="\t")
        print()
        print(AZUL + "-"*170 + RESET)
        print()
    if len(resultado) == 0:
        print(ROJO + "No se encontro" + RESET)
    print(AZUL + "="*170 + RESET)
    print(VERDE + "BUSQUEDA FINALIZADA" + RESET)
    print(AZUL + "="*170 + RESET)
    print()

def impresion_recursiva(lista, i):
    if len(lista)>0:
        impresion = Reemplazo_Id_Valor(lista[0], i)
        print(str(impresion).ljust(23), end="\t")
        impresion_recursiva(lista[1:], i + 1)


def encontrar_elemento(valor, archivo, columna, encabezado):
    try:
        with open(archivo, 'r', encoding='UTF-8') as datos:
            skip = True
            lineas = datos.readline().strip()
            encontrado = False
            print(AZUL + "="*185 + RESET)
            Imprimir_Encabezados(encabezado)
            print(AZUL + "-"*185 + RESET)
            while lineas:
                if skip:
                    skip = False
                    lineas = datos.readline().strip()
                    continue
                columnas = lineas.strip().split(",")
                valor = str(valor)
                busqueda = str(columnas[columna]).lower()
                if valor.isnumeric():
                    busqueda = [busqueda]
                if valor in busqueda:
                    encontrado = True
                    # for col in range(len(columnas)):
                    #     impresion = Reemplazo_Id_Valor(columnas[col], col)
                    #     print(str(impresion).ljust(23), end="\t")
                    impresion_recursiva(columnas, 0)
                    print()
                lineas = datos.readline().strip()
            if not encontrado:
                print("No se encontro el usuario")
            print(AZUL + "-"*185 + RESET)
    except OSError:
        print("No se encontró el archivo")

    return


if __name__ == "__main__":
    encontrar_elemento(12, r'./matrices/empleados.txt', 0, 0)