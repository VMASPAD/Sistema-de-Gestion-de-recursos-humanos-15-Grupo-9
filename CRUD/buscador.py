from impresion import Imprimir_Encabezados, Reemplazo_Id_Valor
#Funciones 

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
            for j in range(len(matriz[i])):
                impresion = Reemplazo_Id_Valor(matriz[i][j], j)
                print(str(impresion).ljust(15), end= "\t")
            existe = True
            print()
            print("-"*130)
    if not existe: print("No se encontro"), print("-"*130)
    print("="*130)

def Id_Empleado(empleados, empleado):
    emp = empleado.lower()
    id = bool(empleado[0] for empleado in empleados if emp in empleado[1].lower())
    while not id:
        print("Empleado no encontrado, intente nuevamente")
        emp = input("Ingrese el nombre o apellido del empleado: ").lower()
        id = bool([empleado[0] for empleado in empleados if emp in empleado[1].lower()])
    id = [empleado[0] for empleado in empleados if emp in empleado[1].lower()][0]
    return id