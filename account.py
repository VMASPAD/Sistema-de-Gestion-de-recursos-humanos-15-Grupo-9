def userLog(user, password):
    if user == "admin" and password == "admin":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print()
        print("MENU PRINCIPAL")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Registrar Elemento  | ')
        print('| 2. Buscador Elementos  | ')
        print('| 3. Editar Elementos    | ')
        print('| 4. Eliminar Elementos  | ')
        print('| 5. Salir               | ')
        print("="*26)
        return 2
    elif user == "user" and password == "user":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print()
        print("MENU PRINCIPAL")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Registrar Empleado  | ')
        print('| 2. Buscador Elementos  | ')
        print('| 3. Editar Elementos    | ')
        print('| 4. Eliminar Empleado  | ')
        print('| 5. Salir               | ')
        print("="*26)
        return 1
    elif user == "guest" and password == "guest":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print()
        print("MENU PRINCIPAL")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Buscador Elementos  | ')
        print('| 2. Salir               | ')
        print("="*26)
        return 0