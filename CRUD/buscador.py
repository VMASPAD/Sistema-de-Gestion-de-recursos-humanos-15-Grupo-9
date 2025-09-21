
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from impresion import Imprimir_Encabezados, Reemplazo_Id_Valor
from dataset import usuarios, empleados
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

def Id_Empleado(empleados, empleado):
    emp = empleado.lower()
    id = bool([empleado[0] for empleado in empleados if emp in empleado[1].lower()])
    while not id:
        print(ROJO + "Empleado no encontrado, intente nuevamente" + RESET)
        emp = input(MAGENTA + "Ingrese el nombre o apellido del empleado: " + RESET).lower()
        id = bool([empleado[0] for empleado in empleados if emp in empleado[1].lower()])
    id = [empleado[0] for empleado in empleados if emp in empleado[1].lower()][0]
    return id

def Encontrar_diccionario(busqueda, usuarios, clave, encabezado=None):
    if not usuarios:
        print(ROJO + "No hay datos para buscar" + RESET)
        return

    # Resolver nombre de la clave si se pasó un índice
    if isinstance(clave, int):
        keys = list(usuarios[0].keys())
        if clave < 0 or clave >= len(keys):
            print(ROJO + "Clave de búsqueda inválida" + RESET)
            return
        key = keys[clave]
    else:
        key = clave

    # Normalizar búsqueda y seleccionar por igualdad o substring
    resultado = []
    try:
        # si busqueda es numérica o un entero, comparar por igualdad
        if isinstance(busqueda, int) or (isinstance(busqueda, str) and busqueda.isdigit()):
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
    except Exception:
        print(ROJO + "Error durante la búsqueda" + RESET)
        return

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
if __name__ == "__main__":
    Encontrar(0, empleados, 0, 0)