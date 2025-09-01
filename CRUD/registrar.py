from idGenerator import generar_id
from dataset import areas, empleados

def Registrar(tipo):
    if tipo == 2:
        RegistrarEmpleado(empleados)
    elif tipo == 1:
        RegistrarArea(areas)
    elif tipo == 3:
        return 0
    else:
        print("Tipo no valido")
        print()
        return 0

def RegistrarEmpleado(empleados):
    empleado = []
    nombre_empleado = input("Ingrese el nombre del empleado: ").lower()
    apellido_empleado = input("Ingrese el apellido del empleado: ").lower()
    telefono_empleado = int(input("Ingrese el telefono del empleado: "))
    posicion_empleado = input("Ingrese la posicion del empleado: ")
    num_area_empleado = int(input("Ingrese el número area del empleado: "))
    fecha_ingreso_empleado = input("Ingrese la fecha de ingreso del empleado: ")
    fecha_nacimiento_empleado = input("Ingrese la fecha de nacimiento del empleado: ")
    A = [generar_id(),nombre_empleado + " " + apellido_empleado, telefono_empleado, posicion_empleado,num_area_empleado,"Activo",fecha_ingreso_empleado,fecha_nacimiento_empleado]
    empleado.extend(A)
    empleados.append(empleado)
    return empleados

def RegistrarArea(areas):
    nueva_area = []
    nombre_area = input("Ingrese el nombre del área: ")
    A = [generar_id(), nombre_area, 0]
    nueva_area.extend(A)
    areas.append(nueva_area)
    return areas

def RegistrarLicencia(licencias):
    nueva_licencia = []
    id_empleado = int(input("Ingrese el id del empleado: "))
    fecha = input("Ingrese la fecha de la licencia (AAAA-MM-DD): ")
    motivo = input("Ingrese el motivo de la licencia: ")
    A = [generar_id(), id_empleado, fecha, motivo, "Activo"]
    nueva_licencia.extend(A)
    licencias.append(nueva_licencia)
    return licencias