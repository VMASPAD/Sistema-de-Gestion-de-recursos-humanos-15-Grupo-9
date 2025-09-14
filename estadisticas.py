
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


def cantidad_empleados(parametro):
    if parametro == "total":
        total = len(empleados)
        print(CIAN + f"La cantidad total de empleados es: {total}" + RESET)
        return total
    elif parametro == "activo":
        activos = lambda emp: emp[5] == "Activo"
        cantidad_activos = len(list(filter(activos, empleados)))
        print(VERDE + f"La cantidad de empleados activos es: {cantidad_activos}" + RESET)
        return cantidad_activos
    elif parametro == "inactivo":
        inactivos = lambda emp: emp[5] == "Inactivo"
        cantidad_inactivos = len(list(filter(inactivos, empleados)))
        print(AMARILLO + f"La cantidad de empleados inactivos es: {cantidad_inactivos}" + RESET)
        return cantidad_inactivos
    else:
        print(ROJO + "Parámetro inválido. Use 'total', 'activo' o 'inactivo'." + RESET)
        return 0

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
    
def porcentaje_empleados_activos(empleados):
    total=len(empleados)
    if total == 0:
        print(AMARILLO + "No hay empleados registrados." + RESET)
        return 0
    activos = len([emp for emp in empleados if emp[5] == "Activo"])
    inactivos = total - activos
    porcentaje_activos = (activos / total) * 100
    porcentaje_inactivos = (inactivos / total) * 100
    print(VERDE + f"Porcentaje de empleados activos: {porcentaje_activos:.2f}%" + RESET)
    print(AMARILLO + f"Porcentaje de empleados inactivos: {porcentaje_inactivos:.2f}%" + RESET)
    return 0

def cantidad_empleados_area(empleados, areas):
    area_dict = {area[0]: area[1] for area in areas}
    area_count = {}
    for emp in empleados:
        if emp[5] == "Activo":
            area_id = emp[4]
            if area_id in area_count:
                area_count[area_id] += 1
            else:
                area_count[area_id] = 1
    print(AZUL + "Cantidad de empleados activos por área:" + RESET)
    for area_id, count in area_count.items():
        area_name = area_dict.get(area_id, "Área desconocida")
        print(CIAN + f"{area_name}: {count}" + RESET)
    return 0


if __name__ == "__main__":
    porcentaje_empleados_activos(empleados)