from dataset import usuarios

def userLog(user, password, usuarios):
    for i in range(len(usuarios)):
        if user == usuarios[i][1]:
            if password == usuarios [i][2]:
                nivel_acceso=usuarios[i][4]
            else: print("El usuario no coincide con la contraseña")        
    if not nivel_acceso:
        print ("No se encontró el usuario.")
        return 0    

    if nivel_acceso=="admin":
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
    elif nivel_acceso=="user":
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
    elif nivel_acceso == "guest":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print()
        print("MENU PRINCIPAL")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Buscador Elementos  | ')
        print('| 2. Salir               | ')
        print("="*26)
        return 0