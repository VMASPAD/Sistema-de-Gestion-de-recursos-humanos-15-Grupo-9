from dataset import areas
#Funciones 
def Registrar_Areas(A, ID):
    cantidad = int(input("Ingrese la cantidad de areas a ingresar: "))

    for _ in range(cantidad):
        A.append([]) 
        A[ID].append(ID + 1)
        area = input("Ingrese el Nombre del area: ")
        A[ID].append(area)
        ID += 1
        #Poner mas tarde para calcular la cantidad por sector
    return A, ID



def Imprimir_Areas(A, encabezados):
    filas = len(A)
    columnas = len(A[0])

    print()
    print("="*26)
    for encabezado in encabezados:
        print(encabezado, end="\t")
    print()
    for i in range(filas):
        for j in range(columnas):
            print(A[i][j], end="\t")
        print()
    print("="*26)
    print()



if __name__ == "__main__":

    encabezados_Areas = ["Id", "Nombre de Area"]
    id = len(areas)
    print(id)
    areas, id = Registrar_Areas(areas, id)
    Imprimir_Areas(areas, encabezados_Areas)