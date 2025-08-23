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
            print('1. Nombre')
            print('2. Apellido')
            print('3. Telefono')
            print('4. Area')
            print('5. Estado')
            print('6. Fecha de ingreso')
            print('7. Fecha de nacimiento')
            campo = int(input("Seleccione el campo a editar (1-7): "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            empleado[campo] = nuevo_valor
            print("Empleado actualizado:", empleado)
        else:
            print("Empleado no encontrado.")
    return
