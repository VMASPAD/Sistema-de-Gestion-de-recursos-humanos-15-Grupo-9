from idGenerator import generar_id
from dataset import justificaciones

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