from dataset import empleados
def Editar():
    print("="*26)
    index = int(input("Escriba el id del empleado a editar o ejecute \"Ver\" para obtener toda la lista"))
    if index == "Ver":
        print("Lista de empleados:")
    else:
        if index < len(empleados):
            empleado = empleados[index]
            print(f"Empleado encontrado: {empleado}")
            print("Que campo quiere editar?")
            print('1. Nombre y apellido')
            print('2. Telefono')
            print('3. Area')
            print('4. Estado')
            print('5. Fecha de ingreso')
            print('6. Fecha de nacimiento')
            campo = int(input("Seleccione el campo a editar (1-6): "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            empleado[campo] = nuevo_valor
            print("Empleado actualizado:", empleado)
        else:
            print("Empleado no encontrado.")
    return
