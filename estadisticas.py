from dataset import empleados, licencias, areas

#Funciones 

def promedio_empleados_por_area(empleados, areas):
    empleados_activos = len([emp for emp in empleados if emp[5] == "Activo"])
    areas_activas = len([area for area in areas if area[3] == "Activo"])
    if areas_activas == 0 or empleados_activos == 0:
        if areas_activas == 0:
            print("No hay áreas activas.")
        if empleados_activos == 0:
            print("No hay empleados activos.")
        return 0
    else:
        promedio = empleados_activos / areas_activas
        print(f"El promedio de empleados por área activa es: {promedio:.2f}")
        return 0


def cantidad_empleados(parametro):
    if parametro == "total":
        total = len(empleados)
        print(f"La cantidad total de empleados es: {total}")
        return total
    elif parametro == "activo":
        activos = lambda emp: emp[5] == "Activo"
        cantidad_activos = len(list(filter(activos, empleados)))
        print(f"La cantidad de empleados activos es: {cantidad_activos}")
        return cantidad_activos
    elif parametro == "inactivo":
        inactivos = lambda emp: emp[5] == "Inactivo"
        cantidad_inactivos = len(list(filter(inactivos, empleados)))
        print(f"La cantidad de empleados inactivos es: {cantidad_inactivos}")
        return cantidad_inactivos
    else:
        print("Parámetro inválido. Use 'total', 'activo' o 'inactivo'.")
        return 0

def promedio_licencias_por_empleado(licencias, empleados):
    empleados_activos = [emp for emp in empleados if emp[5] == "Activo"]
    licencias_activas = [lic for lic in licencias if lic[4] == "Activo"]
    if len(empleados_activos) == 0:
        print("No hay empleados activos.")
        return 0
    else:
        promedio = len(licencias_activas) / len(empleados_activos)
        print(f"El promedio de licencias por empleado activo es: {promedio:.2f}")
        return 0
    
def porcentaje_empleados_activos(empleados):
    total=len(empleados)
    if total == 0:
        print("No hay empleados registrados.")
        return 0
    activos = len([emp for emp in empleados if emp[5] == "Activo"])
    inactivos = total - activos
    porcentaje_activos = (activos / total) * 100
    porcentaje_inactivos = (inactivos / total) * 100
    print(f"Porcentaje de empleados activos: {porcentaje_activos:.2f}%")
    print(f"Porcentaje de empleados inactivos: {porcentaje_inactivos:.2f}%")
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
    print("Cantidad de empleados activos por área:")
    for area_id, count in area_count.items():
        area_name = area_dict.get(area_id, "Área desconocida")
        print(f"{area_name}: {count}")
    return 0


if __name__ == "__main__":
    porcentaje_empleados_activos(empleados)