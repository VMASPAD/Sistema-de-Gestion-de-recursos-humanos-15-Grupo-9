from dataset import empleados, areas, licencias

def Eliminar():
    print("="*26)
    empleadoEliminar = int(input("Escriba el id del empleado o escriba \"Lista\" para obtener la planilla"))
    if empleadoEliminar == "Lista":
        print("Lista de empleados:")
    else:
        del empleados[empleadoEliminar]
        print(f"Empleado con id {empleadoEliminar} eliminado.")

def EliminarArea():
    print("="*26)
    areaEliminar = int(input("Escriba el id del area o escriba \"Lista\" para obtener la planilla"))
    if areaEliminar == "Lista":
        print("Lista de areas:")
    else:
        del areas[areaEliminar]
        print(f"Area con id {areaEliminar} eliminada.")

def EliminarLicencia():
    print("="*26)
    licenciaEliminar = int(input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla"))
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
    else:
        del licencias[licenciaEliminar]
        print(f"Licencia con id {licenciaEliminar} eliminada.")
