from dataset import usuarios

#Funciones
def userLog(usuarios):
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    nivel_acceso = None
    for i in range(len(usuarios)):
        if user == usuarios[i]['username'] and usuarios[i]['estado']=="activo":
            if password == usuarios [i]['password']:
                nivel_acceso=usuarios[i]['nivel_acceso']
            else: print("El usuario no coincide con la contraseña")        
    if not nivel_acceso:
        print ("No se encontró el usuario.")
        return 0    

    if nivel_acceso=="admin": #user: juanp, pass: jp1234, DNI:40123456
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
    elif nivel_acceso=="user": #user: maria.g, pass: mg2024, DNI:38987456
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
    elif nivel_acceso == "guest": #user: lucasf, pass: lfpass, DNI:42111444
        print("Bienvenido al sistema de gestion de recursos humanos")
        print()
        print("MENU PRINCIPAL")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Buscador Elementos  | ')
        print('| 2. Salir               | ')
        print("="*26)
        return 0