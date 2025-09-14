from dataset import empleados, licencias

#Funciones 

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