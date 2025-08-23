from idGenerator import generar_id
def Registrar(emp):
    empleado = []
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    telefono_empleado = int(input("Ingrese el telefono del empleado: "))
    num_area_empleado = int(input("Ingrese el número area del empleado: "))
    estado_empleado = int(input("Ingrese el estado del empleado: "))
    fecha_ingreso_empleado = int(input("Ingrese la fecha de ingreso del empleado: "))
    fecha_nacimiento_empleado = int(input("Ingrese la fecha de nacimiento del empleado: "))
    empleado.extend(generar_id(),nombre_empleado,apellido_empleado,telefono_empleado,num_area_empleado,estado_empleado,fecha_ingreso_empleado,fecha_nacimiento_empleado)
    emp.append(empleado)
    return emp

def RegistrarArea(area):
    nueva_area = []
    nombre_area = input("Ingrese el nombre del área: ")
    cantidad_empleados = int(input("Ingrese la cantidad de empleados en el área: "))
    nueva_area.extend(generar_id(), nombre_area, cantidad_empleados)
    area.append(nueva_area)
    return area