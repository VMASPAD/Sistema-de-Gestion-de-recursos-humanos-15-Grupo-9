import re
from dataset import empleados, areas, justificaciones, licencias
#Funciones 
def Imprimir_Opciones(matriz, columna):
    print()
    print("Opciones: ")
    for i in range(len(matriz)):
        print(f"{i} - {matriz[i][columna]}")

def Imprimir_Encabezados(fila):
    encabezados = [
        ["id",	"Nombre y Ape..", "Telefono", "Posición", "id_Area", "Estado", "Fecha_ingreso", "Fecha_nacimiento"], # Empleados 
        ["Id", "Nombre", "Cantidad", "Estado"], # Areas
        ["Id", "Empleado", "Fecha","Justificacion", "Estado"], # Licencias
        ["Id", "Justificación", "Tipo"] # Justificaciones 
        ]
    for i in encabezados[fila]:
        i = i.ljust(15)
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

    nombre = nombre.ljust(15)
    return nombre

def Imprimir_Matriz_Ordenada(matriz, encabezado, llave):
    filas = len(matriz)
    columnas = len(matriz[0])

    matriz.sort(key=llave)
    print("="*130)
    Imprimir_Encabezados(encabezado)
    print("-"*130)
    for i in range(filas):
        if "Inactivo" not in matriz[i]:
            for j in range(columnas):
                impresion = matriz[i][j]
                impresion = Reemplazo_Id_Valor(impresion, j)
                impresion = Formato(impresion)
                print(impresion, end="\t")
            print()
            print("-"*130)
    print("="*130)
    print()
    return

def Encontrar_Id_Empleado(empleados, empleado):
    id = list(filter(lambda x: empleado in x[1].lower(), empleados))    
    if id:
        return id[0][0]
    else:
        print("Empleado no encontrado") 
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
    print("="*198)
    for i in usuarios[0].keys():
        print (i.ljust(25),end="\t")
    print()
    print("-"*198)
    for i in range(len(usuarios)):
        if "Inactivo" not in usuarios[i].values():
            for j in usuarios[i].keys():
                impresion = str(usuarios[i][j])
                print(impresion.ljust(25), end="\t")
            print()
            print("-"*198)
    print("="*198)
    print()
    return 

def formato_dni(dni):
    patron= re.compile (dni)
    impresion_dni=patron.sub(dni[:-6]+'.'+dni[-6:-3]+'.'+ dni[-3: ],dni)
    return impresion_dni