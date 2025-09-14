from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada, Imprimir_Opciones
from CRUD.registrar import Ingresar_Fecha, verificar_telefono
from CRUD.buscador import Encontrar
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import empleados, areas, licencias
#Funciones 

#Registrar empleado
def RegistrarEmpleado(empleados):
    empleado = []
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    telefono_empleado = verificar_telefono()
    posicion_empleado = input("Ingrese la posicion del empleado: ")
    Imprimir_Opciones(areas, 1)
    num_area_empleado = int(input("Ingrese el número area del empleado: "))
    fecha_ingreso_empleado = Ingresar_Fecha("el ingreso del empleado")
    fecha_nacimiento_empleado = Ingresar_Fecha("la fecha de nacimiento del empleado")
    A = [generar_id(empleados),nombre_empleado + " " + apellido_empleado, telefono_empleado, posicion_empleado,num_area_empleado,"Activo",fecha_ingreso_empleado,fecha_nacimiento_empleado]
    empleado.extend(A)
    empleados.append(empleado)
    areas[num_area_empleado][2] += 1
    return empleados

#Buscar empleado
def BuscarEmpleado(empleados):
    print("MENU PRINCIPAL -> EMPLEADOS -> BUSCADOR")
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

#Editar empleado
def EditarEmpleado():
    print("="*26)
    index = int(input("Escriba el id del empleado a editar:  "))
    if index < len(empleados) and index >= 0:
        empleado = empleados[index]
        print(f"Empleado encontrado: {empleado}")
        print("Que campo quiere editar?")
        print('1. Nombre')
        print('2. Apellido')
        print('3. Telefono')
        print('4. Area')
        print('5. Estado')
        print('6. Fecha de ingreso')
        print('7. Fecha de nacimiento')
        campo = int(input("Seleccione el campo a editar (1-7): "))
        match campo:
            case 1:
                nuevo_valor = input("Ingrese el nuevo nombre: ")
            case 2:
                nuevo_valor = input("Ingrese el nuevo apellido: ")
            case 3:
                nuevo_valor = verificar_telefono()
            case 4:
                nuevo_valor = input("Ingrese la nueva area: ")
            case 5:
                nuevo_valor = input("Ingrese el nuevo estado: ")
            case 6:
                nuevo_valor = Ingresar_Fecha("fecha de ingreso")
            case 7:
                nuevo_valor = Ingresar_Fecha("fecha de nacimiento")
        if campo == 1 or campo == 2:
            nombre_actual = empleado[1].split(" ")
            if campo == 1:
                nombre_actual[0] = nuevo_valor
            else:
                nombre_actual[1] = nuevo_valor
            nuevo_valor = " ".join(nombre_actual)
        empleados[index][campo - 1 if campo > 1 else campo] = nuevo_valor
        print("Empleado actualizado:", empleados[index])
    else:
        print("Empleado no encontrado.")
    
#Eliminar empleado
def EliminarEmpleado():
    print("="*26)
    empleadoEliminar = input("Escriba el nombre y apellido del empleado o escriba \"Lista\" para obtener la planilla: ").lower()
    if empleadoEliminar == "lista":
        print("Lista de empleados:")
        Imprimir_Matriz_Ordenada(empleados, lambda fila: fila[0])
    elif empleadoEliminar in [empleado[1].lower() for empleado in empleados]:
        posicion_empleados = empleados[[empleado[1].lower() for empleado in empleados].index(empleadoEliminar)]
        # print(posicion_empleados)
        empleados[posicion_empleados[0]][5] = "Inactivo"
        Eliminar_ClaveForanea(posicion_empleados[0], licencias, 1)
        print(f"Empleado {empleadoEliminar} eliminado.")
        areas[posicion_empleados[4]][2] -= 1
    else:
        print(f"Empleado {empleadoEliminar} no encontrado.")


if __name__ == "__main__":
    EditarEmpleado()