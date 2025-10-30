
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from dataset import empleados, licencias, areas

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
        with open(r'matrices/empleados.txt', 'r', encoding='UTF-8') as arch:
            for lineas in arch:
                linea = lineas.strip().split(";")
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
        with open(r'matrices/areas.txt', 'r', encoding="UTF-8") as arch:
            for lineas in arch:
                linea = lineas.strip().split(";")
                nomArea = linea[1]
                cantidad = linea[2]
                print(f'{nomArea}: {cantidad}')
    except FileNotFoundError:
        print("No se encontro el archivo")
    return 0


if __name__ == "__main__":
    porcentaje_empleados_activos(empleados)