#id, nombre, cantidad
areas = []
#id, id_empleado, fecha, id_justificacion
licencias = []
#id, justificacion
justificaciones = []
#id, nombre y apellido, telefono, area, estado, fecha de ingreso, fecha de nacimiento
empleados = []

def Registrar():

    return

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
if __name__ == "__main__":

    Menu()