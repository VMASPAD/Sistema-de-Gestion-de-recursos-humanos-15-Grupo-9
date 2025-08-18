# return nivel de acceso
def userLog(user, password):
    if user == "admin" and password == "admin":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print("="*26)
        print('| 1. Registrar empleado  | ')
        print('| 2. Obtener empleados   | ')
        print('| 3. Editar empleado     | ')
        print('| 4. Eliminar empleado   | ')
        print('| 5. Salir               | ')
        print("="*26)
        return 2
    elif user == "empleado" and password == "empleado":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print("="*26)
        print('| 1. Registrar empleado  | ')
        print('| 2. Obtener empleados   | ')
        print('| 3. Editar empleado     | ')
        print('| 4. Salir               | ')
        print("="*26)
        return 1
    elif user == "pasante" and password == "pasante":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print("="*26)
        print('| 1. Obtener empleados   | ')
        print('| 2. Salir               | ')
        print("="*26)
        return 0
    