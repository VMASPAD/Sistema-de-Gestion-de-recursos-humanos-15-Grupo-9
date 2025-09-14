from dataset import empleados, licencias

#Funciones 

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




if __name__ == "__main__":
    promedio_licencias_por_empleado(licencias, empleados)