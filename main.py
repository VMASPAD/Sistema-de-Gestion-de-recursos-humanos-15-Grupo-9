from dataset import empleados, areas, justificaciones, licencias
from account import userLog
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

#region TOMI
def Editar():
    print("="*26)
    index = int(input("Escriba el id del empleado a editar o ejecute \"Ver\" para obtener toda la lista"))
    if index == "Ver":
        print("Lista de empleados:")
    else:
        if index < len(empleados):
            empleado = empleados[index]
            print(f"Empleado encontrado: {empleado}")
            print("Que campo quiere editar?")
            print('1. Nombre y apellido')
            print('2. Telefono')
            print('3. Area')
            print('4. Estado')
            print('5. Fecha de ingreso')
            print('6. Fecha de nacimiento')
            campo = int(input("Seleccione el campo a editar (1-6): "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            empleado[campo] = nuevo_valor
            print("Empleado actualizado:", empleado)
        else:
            print("Empleado no encontrado.")
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
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    nivel_acceso = userLog(user, password)
    match nivel_acceso:
        case 2:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                Registrar()
            if opcion == 2:
                Buscador()
            if opcion == 3:
                Editar()
            if opcion == 4:
                Eliminar()
            if opcion == 5:
                print("-"*26)
                return 0
            pass
        case 1:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                Registrar()
            if opcion == 2:
                Buscador()
            if opcion == 3:
                Editar()
            if opcion == 4:
                print("-"*26)
                return 0
            pass
        case 0:
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                Buscador()
            if opcion == 2:
                print("-"*26)
                return 0
            pass
#Programa principal
if __name__ == "__main__":

    Menu()