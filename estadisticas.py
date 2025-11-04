
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from dataset import archivos
from datetime import datetime
from functools import reduce

#Funciones 

def promedio_empleados_por_area(empleados, areas):
    empleados_activos = len([emp for emp in empleados if emp[5] == "Activo"])
    areas_activas = len([area for area in areas if area[3] == "Activo"])
    if areas_activas == 0 or empleados_activos == 0:
        if areas_activas == 0:
            print(AMARILLO + "No hay áreas activas." + RESET)
        if empleados_activos == 0:
            print(AMARILLO + "No hay empleados activos." + RESET)
        return 0
    else:
        promedio = empleados_activos / areas_activas
        print(CIAN + f"El promedio de empleados por área activa es: {promedio:.2f}" + RESET)
        return 0


def cantidad_empleados():
    activos = 0
    inactivos = 0
    try:
        with open(r'matrices/empleados.csv', 'r', encoding='UTF-8') as arch:
            skip = True
            for lineas in arch:
                if skip:
                    skip = False
                    continue
                linea = lineas.strip().split(",")
                estado = linea[5]
                match estado:
                    case "Activo":
                        activos += 1
                    case "Inactivo":
                        inactivos += 1
                    case _:
                        raise OSError
    except (OSError, FileNotFoundError):
        print("Error!")
    return activos, inactivos
    
def promedio_licencias_por_empleado(licencias, empleados):
    empleados_activos = [emp for emp in empleados if emp[5] == "Activo"]
    licencias_activas = [lic for lic in licencias if lic[4] == "Activo"]
    if len(empleados_activos) == 0:
        print(AMARILLO + "No hay empleados activos." + RESET)
        return 0
    else:
        promedio = len(licencias_activas) / len(empleados_activos)
        print(CIAN + f"El promedio de licencias por empleado activo es: {promedio:.2f}" + RESET)
        return 0

def porcentaje_empleados_activos(activos, inactivos):
    total= activos + inactivos
    if total == 0:
        print(AMARILLO + "No hay empleados registrados." + RESET)
        return 0
    porcentaje_activos = (activos / total) * 100
    porcentaje_inactivos = (inactivos / total) * 100
    print(VERDE + f"Porcentaje de empleados activos: {porcentaje_activos:.2f}%" + RESET)
    print(AMARILLO + f"Porcentaje de empleados inactivos: {porcentaje_inactivos:.2f}%" + RESET)
    return 0

def cantidad_empleados_area():
    try:
        with open(r'matrices/areas.csv', 'r', encoding="UTF-8") as arch:
            skip = True
            for lineas in arch:
                if skip:
                    skip = False
                    continue
                linea = lineas.strip().split(",")
                nomArea = linea[1]
                cantidad = linea[2]
                print(f'{nomArea}: {cantidad}')
    except FileNotFoundError:
        print("No se encontro el archivo")
    return 0

def calcular_edad(fecha, hoy):
    fecha_nacimiento = datetime.strptime(fecha, r"%Y-%m-%d").date()
    edad = hoy.year - fecha_nacimiento.year- ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad


def promedio_de_edad():
    fechas = []
    try:
        with open(archivos[0], 'r', encoding='UTF-8') as arch:
            skip = True
            for lineas in arch:
                if skip:
                    skip = False
                    continue
                linea = lineas.strip().split(",")
                fechas.append(linea[-1])


    except (FileNotFoundError, OSError):
        print("Error!")
    
    hoy = datetime.today()
    edades = list(map(lambda x: calcular_edad(x, hoy), fechas))

    if edades:
        suma = reduce(lambda x, y: x + y, edades)
        promedio = suma / len(edades) 
        print(f"El promedio de edad es de: {promedio:.2f}")
    else:
        print("No se puede hacer promedio por falta de empleados")

if __name__ == "__main__":
    promedio_de_edad()