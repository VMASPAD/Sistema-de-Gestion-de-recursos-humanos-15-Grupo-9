from dataset import empleados

def Eliminar():
    print("="*26)
    empleadoEliminar = int(input("Escriba el id del empleado o escriba \"Lista\" para obtener la planilla"))
    if empleadoEliminar == "Lista":
        print("Lista de empleados:")
    else:
        del empleados[empleadoEliminar]
        print(f"Empleado con id {empleadoEliminar} eliminado.")