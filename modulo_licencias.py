from idGenerator import generar_id
from impresion import Imprimir_Matriz_Ordenada, Encontrar_Id_Empleado
from CRUD.registrar import Eleccion_Justificacion, Ingresar_Fecha
from CRUD.buscador import Encontrar, Id_Empleado
from CRUD.eliminar import Eliminar_ClaveForanea
from dataset import empleados, licencias
#Funciones 

#Registrar Licencia
def RegistrarLicencia(licencias):
    nueva_licencia = []
    id_empleado = Id_Empleado(empleados, input("Ingrese el nombre y apellido del empleado: "))
    fecha_licencia = Ingresar_Fecha("la licencia")
    justificacion_licencia = Eleccion_Justificacion()
    A = [generar_id(licencias), id_empleado, fecha_licencia, justificacion_licencia, "Activo"]
    nueva_licencia.extend(A)
    licencias.append(nueva_licencia)
    return licencias

#Buscar Licencia
def BuscarLicencia(licencias, empleados):
    print("MENU PRINCIPAL -> LICENCIAS -> BUSCADOR")
    print("="*34)
    print("| Opciones:".ljust(33) + "|")
    print("| 1 - Id".ljust(33) + "|")
    print("| 2 - Empleado".ljust(33) + "|")
    print("| 3 - Fecha".ljust(33) + "|")
    print("| 4 - Mostrar licencias".ljust(33) + "|")
    print("| 5 - Volver".ljust(33) + "|")
    print("="*34)
    opcion = int(input("Ingrese la opcion de busqueda: "))
    print()
    match opcion:
        case 1:
            busqueda = int(input("Ingrese el Id a buscar: "))
            Encontrar(busqueda, licencias, 0, 2)
        case 2:
            busqueda = input("Ingrese el nombre y apellido del empleado a buscar: ")
            busqueda = busqueda.lower()
            busqueda = Encontrar_Id_Empleado(empleados, busqueda)
            if busqueda:
                Encontrar(busqueda, licencias, 1, 2)
        case 3:
            busqueda = input("Ingrese la fecha a buscar (AAAA-MM-DD): ")
            Encontrar(busqueda, licencias, 2, 2)
        case 4:
            key = lambda fila : fila[0]
            Imprimir_Matriz_Ordenada(licencias, 2, key)
        case 5:
            return

#Editar Licencia
def EditarLicencia():
    print("="*26)
    index = int(input('Escriba el id de la licencia a editar: '))
    if index < len(licencias) and index >= 0:
        print("Que campo quiere editar?")
        print('1. Fecha')
        print('2. Empleado')
        valueTochange = int(input('Seleccione una opcion: '))
        if licencias[index][0] == index:
            print(f"Licencia encontrada: {licencias[index]}")
        if valueTochange == 1:
            newFecha = Ingresar_Fecha("la licencia")
            licencias[index][2] = newFecha
            print(f"Licencia actualizada: {licencias[index]}")
        elif valueTochange == 2:
            newEmpleado = input(f'Ingrese el nombre y apellido del empleado a reemplazar: {licencias[index][1]}: ')
            licencias[index][1] = Id_Empleado(empleados, newEmpleado)
            print(f"Licencia actualizada: {licencias[index]}")
    else:
        print('Licencia no encontrada')
    return licencias

#Eliminar Licencia
def EliminarLicencia():
    print("="*26)
    licenciaEliminar = input("Escriba el id de la licencia a eliminar del empleado o escriba \"Lista\" para obtener la planilla: ")
    if licenciaEliminar == "Lista":
        print("Lista de licencias:")
        Imprimir_Matriz_Ordenada(licencias, 2, lambda fila: fila[0])
    elif licenciaEliminar in [str(licencia[0]) for licencia in licencias]:
        posicion_licencia = licencias[[str(licencia[0]) for licencia in licencias].index(licenciaEliminar)]
        licencias[posicion_licencia[0]][4] = "Inactivo"
        print(f"Licencia con id {licenciaEliminar} de la persona {empleados[posicion_licencia[1]][1]} eliminada.")
    else:
        print(f"Licencia con id {licenciaEliminar} no encontrada.")