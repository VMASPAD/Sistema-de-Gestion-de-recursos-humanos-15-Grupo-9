from idGenerator import generar_id
from dataset import areas, empleados

def Registrar(tipo):
    if tipo == 1:
        RegistrarEmpleado(empleados)
    elif tipo == 2:
        RegistrarArea(areas)
    else:
        print("Tipo no valido")
    return 0

def RegistrarEmpleado():
    empleado = []
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    telefono_empleado = int(input("Ingrese el telefono del empleado: "))
    num_area_empleado = int(input("Ingrese el número area del empleado: "))
    estado_empleado = int(input("Ingrese el estado del empleado: "))
    fecha_ingreso_empleado = int(input("Ingrese la fecha de ingreso del empleado: "))
    fecha_nacimiento_empleado = int(input("Ingrese la fecha de nacimiento del empleado: "))
    empleado.extend(generar_id(),nombre_empleado,apellido_empleado,telefono_empleado,num_area_empleado,estado_empleado,fecha_ingreso_empleado,fecha_nacimiento_empleado)
    empleados.append(empleado)
    return empleados

def RegistrarArea():
    nueva_area = []
    nombre_area = input("Ingrese el nombre del área: ")
    cantidad_empleados = int(input("Ingrese la cantidad de empleados en el área: "))
    nueva_area.extend(generar_id(), nombre_area, cantidad_empleados)
    areas.append(nueva_area)
    return areas