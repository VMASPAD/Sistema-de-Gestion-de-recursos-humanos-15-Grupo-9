from idGenerator import generar_id
from dataset import justificaciones, empleados, areas
import re 

#Funciones
def Eleccion_Justificacion():
    print("Seleccione una justificacion:")
    for justificacion in justificaciones:
        print(f"{justificacion[0]} - {justificacion[1]}")
    opcion = int(input("Ingrese la opcion: "))
    return opcion

def Ingresar_Fecha(asunto):
    dia = int(input(f"Ingrese el dia (DD) de {asunto}: "))
    mes = int(input(f"Ingrese el mes (MM) de {asunto}: "))
    año = int(input(f"Ingrese el año (AAAA) de {asunto}: "))
    return f"{año}-{mes}-{dia}"

def Calcular_cantidad_empleados(empleados, area_id):
    cantidad = 0
    for empleado in empleados:
        if empleado[4] == area_id and empleado[5] == "Activo":
            cantidad += 1
    return cantidad

def verificar_area():
    nombres_areas = {areas[i][1].lower() for i in range(len(areas))}
    nombre_area = input("Ingrese el nombre del área: ").strip().lower()
    while nombre_area in nombres_areas or nombre_area == "":
        if nombre_area in nombres_areas:
            print("El nombre del área ya existe, por favor ingrese otro.")
        else:
            print("El nombre del área no puede estar vacío.")
        nombre_area = input("Ingrese el nombre del área: ").strip().lower()
    return nombre_area.capitalize()


def verificar_telefono():
    codigo_area = input("Ingrese el codigo de area (sin +54): ")
    telefono = input("Ingrese el telefono (los ultimos 8 digitos): ")
    patron = re.compile('[0-9]{8}')
    while not patron.match(telefono):
        print("Telefono invalido")
        telefono = input("Ingrese el telefono (los ultimos 8 digitos): ")
    telefono = "+54" + codigo_area + telefono
    telefonos_en_sistema = {empleados[i][2] for i in range(len(empleados))}
    while telefono in telefonos_en_sistema:
        print("El telefono ya existe en el sistema, por favor ingrese otro.")
        codigo_area = input("Ingrese el codigo de area (sin +54): ")
        telefono = input("Ingrese el telefono (los ultimos 8 digitos): ")
        while not patron.match(telefono):
            print("Telefono invalido")
            telefono = input("Ingrese el telefono (los ultimos 8 digitos): ")
        telefono = "+54" + codigo_area + telefono
    return telefono