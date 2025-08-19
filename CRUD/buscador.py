from dataset import empleados, areas

#Funciones 
def Imprimir_Opciones(matriz, columna):
    print()
    print("Opciones: ")
    for i in range(len(matriz)):
        print(f"{i + 1} - {matriz[i][columna]}")

def Imprimir_Encabezados(fila):
    encabezados = [
        ["id",	"Nombre", "Apellido", "Telefono", "Posición", "id_Area", "Estado", "Fecha_ingreso", "Fecha_nacimiento"], # Empleados 
        ["Id", "Nombre", "Cantidad"], # Areas
        ["Id", "Id_Empleado", "Fecha","ID_Justificacion"], # Licencias
        ["Id", "Justificación", "Tipo"] # Justificaciones 
        ]
    for i in encabezados[fila]:
        print(i, end= "    ")
    print()
    return

def Imprimir_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="\t")
        print()
    print("="*26)
    print()
    return

def Encontrar(valor, matriz, columna, encabezado):
    existe = False
    Imprimir_Encabezados(encabezado)
    for i in range(len(matriz)):
        if matriz[i][columna] == valor:
            #mejorar impresion 
            for j in matriz[i]:
                print(j, end= "\t")
            existe = True
            print() 
    if not existe: print("No se encontro")

def Buscador(empleados, areas):
    for i in range(len(empleados)):
        for j in range(1, 3):
            empleados[i][j] =  empleados[i][j].lower()
    
    print("Opciones: ")
    print("1 - Id")
    print("2 - Nombre")
    print("3 - Apellido")
    print("4 - Area")
    print("5 - xxx")
    opcion = int(input("Ingrese la opcion de busqueda: "))
    match opcion: 
        case 1:
            busqueda = int(input("Ingrese el Id a buscar: "))
            Encontrar(busqueda, empleados, 0, 0)
        case 2:
            busqueda = input("Ingrese el nombre a buscar: ")
            busqueda = busqueda.lower()
            Encontrar(busqueda, empleados, 1, 0)
        case 3:
            busqueda = input("Ingrese el apellido a buscar: ")
            busqueda = busqueda.lower()
            Encontrar(busqueda, empleados, 2, 0)
        case 4: 
            Imprimir_Opciones(areas, 1)
            busqueda = int(input("Ingrese el Area a buscar: "))
            Encontrar(busqueda, empleados, 5, 0)

    return



if __name__ == "__main__":
    Buscador(empleados, areas)