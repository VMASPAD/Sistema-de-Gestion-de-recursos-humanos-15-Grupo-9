#id, nombre, cantidad
areas = []
#id, id_empleado, fecha, id_justificacion
licencias = []
#id, justificacion
justificaciones = []
#id, nombre y apellido, telefono, area, estado, fecha de ingreso, fecha de nacimiento
empleados = []

# region FACU
def Registrar(emp):
    empleado = []
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    telefono_empleado = int(input("Ingrese el telefono del empleado: "))
    num_area_empleado = int(input("Ingrese el número area del empleado: "))
    estado_empleado = int(input("Ingrese el estado del empleado: "))
    fecha_ingreso_empleado = int(input("Ingrese la fecha de ingreso del empleado: "))
    fecha_nacimiento_empleado = int(input("Ingrese la fecha de nacimiento del empleado: "))
    empleado.extend(nombre_empleado,apellido_empleado,telefono_empleado,num_area_empleado,estado_empleado,fecha_ingreso_empleado,fecha_nacimiento_empleado)
    emp.append(empleado)
    return emp

def Buscador():

    return

def Editar():
    
    return

def Eliminar():
    print("="*26)
    empleadoEliminar = int(input("Escriba el id del empleado o escriba \"Lista\" para obtener la planilla"))
    if empleadoEliminar == "Lista":
        print("Lista de empleados:")
    else:
        del empleados[empleadoEliminar]
    return ''

def Menu():
    print("="*26)
    print('| 1. Registrar empleado  | ')
    print('| 2. Obtener empleados   | ')
    print('| 3. Editar empleado     | ')
    print('| 4. Eliminar empleado   | ')
    print('| 5. Salir               | ')
    print("="*26)

#Programa principal
#if __name__ == "__main__":
empleados=Registrar(empleados)
print(empleados)
    # Menu()