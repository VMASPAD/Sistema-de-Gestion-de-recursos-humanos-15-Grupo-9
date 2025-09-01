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
                impresion = Formato(matriz[i][j]) 
                print(impresion, end="\t")
            print()
            print("-"*130)
    print("="*130)
    print()
    return

def Encontrar(valor, matriz, columna, encabezado):
    existe = False
    print("="*130)
    Imprimir_Encabezados(encabezado)
    print("-"*130)
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
            for j in matriz[i]:
                print(str(j).ljust(15), end= "\t")
            existe = True
            print()
            print("-"*130)
    if not existe: print("No se encontro"), print("-"*130)
    print("="*130)

def Buscador(empleados, areas):
    print()
    print("MENU PRINCIPAL -> BUSCADOR")
    print("="*34)
    print("| Opciones:".ljust(33) + "|")
    print("| 1 - Areas".ljust(33) + "|")
    print("| 2 - Empleados".ljust(33) + "|")
    print("| 3 - Licencias".ljust(33) + "|")
    print("| 4 - Volver".ljust(33) + "|")
    print("="*34)
    matriz = int(input("Ingrese la opcion de busqueda: "))
    print()
    match matriz:
        case 1:
            print("MENU PRINCIPAL -> BUSCADOR -> AREAS")
            print("="*34)
            print("| Opciones:".ljust(33) + "|")
            print("| 1 - Id".ljust(33) + "|")
            print("| 2 - Nombre".ljust(33) + "|")
            print("| 3 - Mostrar areas".ljust(33) + "|")
            print("| 4 - Volver".ljust(33) + "|")
            print("="*34)
            opcion = int(input("Ingrese la opcion de busqueda: "))
            print()
            match opcion:
                case 1:
                    busqueda = int(input("Ingrese el Id a buscar: "))
                    Encontrar(busqueda, areas, 0, 1)
                case 2:
                    busqueda = input("Ingrese el nombre a buscar: ")
                    busqueda = busqueda.lower()
                    Encontrar(busqueda, areas, 1, 1)
                case 3:
                    key = lambda fila : fila[0]
                    Imprimir_Matriz_Ordenada(areas, 1, key)
                case 4:
                    return

        case 2:
            print("MENU PRINCIPAL -> BUSCADOR -> EMPLEADOS")
            print("="*34)
            print("| Opciones:".ljust(33) + "|")
            print("| 1 - Id".ljust(33) + "|")
            print("| 2 - Nombre/Apellido".ljust(33) + "|")
            print("| 3 - Area".ljust(33) + "|")
            print("| 4 - Mostrar empleados".ljust(33) + "|")
            print("| 5 - Volver".ljust(33) + "|")
            print("="*34)
            opcion = int(input("Ingrese la opcion de busqueda: "))
            print()
            match opcion: 
                case 1:
                    busqueda = int(input("Ingrese el Id a buscar: "))
                    Encontrar(busqueda, empleados, 0, 0)
                case 2:
                    busqueda = input("Ingrese el nombre o apellido a buscar: ")
                    busqueda = busqueda.lower()
                    Encontrar(busqueda, empleados, 1, 0)
                case 3: 
                    Imprimir_Opciones(areas, 1)
                    busqueda = int(input("Ingrese el numero de area a buscar: "))
                    Encontrar(busqueda, empleados, 4, 0)
                case 4:
                    print("="*34)
                    print("| Opciones ascendentemente:".ljust(33) + "|")
                    print("| 1 - Id".ljust(33) + "|")
                    print("| 2 - Area".ljust(33) + "|")
                    print("| 3 - Apellido".ljust(33) + "|")
                    print("| 4 - Volver".ljust(33) + "|")
                    print("="*34)   
                    opcion = int(input("Ingrese la opcion de ordenado: "))
                    print()
                    match opcion :
                        case 1:
                            key = lambda fila : fila[0]
                            Imprimir_Matriz_Ordenada(empleados, 0,  key)
                        case 2:
                            key = lambda fila : fila[4]
                            Imprimir_Matriz_Ordenada(empleados, 0,  key)
                        case 3: 
                            key = lambda fila: fila[1].rsplit(" ", 1)[-1]
                            Imprimir_Matriz_Ordenada(empleados, 0,  key)

    return



if __name__ == "__main__":
    Buscador(empleados, areas)
