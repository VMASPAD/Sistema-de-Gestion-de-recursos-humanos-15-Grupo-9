
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada, Imprimir_Opciones
from estadisticas import cantidad_empleados, porcentaje_empleados_activos, cantidad_empleados_area
from CRUD.registrar import Ingresar_Fecha, verificar_telefono, Ingresar_Numero, agregar_entidad_archivo, obtener_ultimo_codigo
from CRUD.buscador import Encontrar
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import empleados, areas, licencias
#Funciones 

#Registrar empleado
def RegistrarEmpleado(archivo):
    id = int(obtener_ultimo_codigo(archivo))
    id = id + 1 if id != 0 else 0
    nombre_empleado = input("Ingrese el nombre del empleado: ").strip().capitalize()
    apellido_empleado = input("Ingrese el apellido del empleado: ").strip().capitalize()
    telefono_empleado = verificar_telefono()
    posicion_empleado = input("Ingrese la posicion del empleado: ").strip().capitalize()
    num_area_empleado = Ingresar_Numero("Ingrese el numero del area del empleado: " )
    fecha_ingreso_empleado = Ingresar_Fecha("el ingreso del empleado")
    fecha_nacimiento_empleado = Ingresar_Fecha("la fecha de nacimiento del empleado")
    fila = [id, nombre_empleado + " " + apellido_empleado, telefono_empleado, posicion_empleado, num_area_empleado, "Activo", fecha_ingreso_empleado, fecha_nacimiento_empleado]
    ok = agregar_entidad_archivo(archivo, fila)
    if ok:
        print(f"Se agrego el empleado {nombre_empleado + " " + apellido_empleado} exitosamente!")
    else:
        print("No se pudo registrar al empleado")

#Buscar empleado
def BuscarEmpleado(empleados):
    print(AZUL + "MENU PRINCIPAL -> EMPLEADOS -> BUSCADOR" + RESET)
    print(AZUL + "="*34 + RESET)
    print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
    print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
    print(CIAN + "| 2 - Nombre/Apellido".ljust(33) + "|" + RESET)
    print(CIAN + "| 3 - Area".ljust(33) + "|" + RESET)
    print(CIAN + "| 4 - Mostrar empleados".ljust(33) + "|" + RESET)
    print(CIAN + "| 5 - Volver".ljust(33) + "|" + RESET)
    print(AZUL + "="*34 + RESET)
    opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
    print()
    match opcion: 
        case 1:
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
            Encontrar(busqueda, empleados, 0, 0)
        case 2:
            busqueda = input(MAGENTA + "Ingrese el nombre o apellido a buscar: " + RESET)
            busqueda = busqueda.lower()
            Encontrar(busqueda, empleados, 1, 0)
        case 3: 
            Imprimir_Opciones(areas, 1)
            busqueda = Ingresar_Numero(MAGENTA + "Ingrese el numero de area a buscar: " + RESET)
            Encontrar(busqueda, empleados, 4, 0)
        case 4:
            print(CIAN + "="*34 + RESET)
            print(CIAN + "| Opciones ascendentemente:".ljust(33) + "|" + RESET)
            print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
            print(CIAN + "| 2 - Area".ljust(33) + "|" + RESET)
            print(CIAN + "| 3 - Apellido".ljust(33) + "|" + RESET)
            print(CIAN + "| 4 - Volver".ljust(33) + "|" + RESET)
            print(CIAN + "="*34 + RESET)
            opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de ordenado: " + RESET)
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

def EstadisticasEmpleados():
    print("="*43)
    print("MENU PRINCIPAL -> EMPLEADOS -> ESTADISTICAS")
    print("="*43)
    print("| Opciones:".ljust(42) +"|")
    print("| 1. Ver cantidad de empleados totales".ljust(42) +"|")
    print("| 2. Ver estado actual de empleados".ljust(42) +"|")
    print("| 3. Ver cantidad de empleados por area".ljust(42) +"|")
    print("| 0. Volver".ljust(42) +"|")
    print("="*43)
    opcion = Ingresar_Numero("Seleccione una opcion: ")
    match opcion:
        case 1: 
            cantidad_empleados("total")
        case 2:
            cantidad_empleados("activo")
            porcentaje_empleados_activos(empleados)
        case 3:
            cantidad_empleados("inactivo")
            cantidad_empleados_area(empleados, areas)
        case 0:
            print("Volviendo al menu principal...")
        case _:
            print("Opcion no valida")
        
    return 0
#Editar empleado
def EditarEmpleado():
    print("="*26)
    index = Ingresar_Numero("Escriba el id del empleado a editar:  ")
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
        campo = Ingresar_Numero("Seleccione el campo a editar (1-7): ")
        match campo:
            case 1:
                nuevo_valor = input("Ingrese el nuevo nombre: ").strip().capitalize()
            case 2:
                nuevo_valor = input("Ingrese el nuevo apellido: ").strip().capitalize()
            case 3:
                nuevo_valor = verificar_telefono()
            case 4:
                nuevo_valor = input("Ingrese la nueva area: ").strip().capitalize()
            case 5:
                nuevo_valor = input("Ingrese el nuevo estado: ").strip().capitalize()
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

             
def obtener_ultimo_codigo(archivo):
    ultimo_codigo = "0"
    try:
        with open(archivo, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = linea.strip().split(";")
                ultimo_codigo = datos[0]
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos desde cero
    return ultimo_codigo

if __name__ == "__main__":
    EstadisticasEmpleados()