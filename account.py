
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from dataset import usuarios

#Funciones
def userLog(usuarios):
    usuarios_activos = {usuarios[i]["username"] for i in range(len(usuarios)) if usuarios[i]["estado"]=="Activo"}
    user = input(MAGENTA + "Ingrese su usuario: " + RESET).strip()
    password = input(MAGENTA + "Ingrese su contraseña: " + RESET).strip()
    nivel_acceso = None
    for i in range(len(usuarios)):
        if user == usuarios[i]['username'] and user in usuarios_activos:
            if password == usuarios [i]['password']:
                nivel_acceso=usuarios[i]['nivel_acceso']
            else: print(ROJO + "El usuario no coincide con la contraseña" + RESET)        
    if not nivel_acceso:
        print (ROJO + "No se encontró el usuario." + RESET)
        return 0    

    if nivel_acceso=="admin": #user: juanp, pass: jp1234, DNI:40123456
        print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
        print()
        print(AZUL + "MENU PRINCIPAL" + RESET)
        print(AZUL + "="*26 + RESET)
        print(CIAN + '| Seleccione operacion   | ' + RESET)
        print(CIAN + '| 1. Registrar Elemento  | ' + RESET)
        print(CIAN + '| 2. Buscador Elementos  | ' + RESET)
        print(CIAN + '| 3. Editar Elementos    | ' + RESET)
        print(CIAN + '| 4. Eliminar Elementos  | ' + RESET)
        print(CIAN + '| 5. Salir               | ' + RESET)
        print(AZUL + "="*26 + RESET)
        return 2
    elif nivel_acceso=="user": #user: maria.g, pass: mg2024, DNI:38987456
        print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
        print()
        print(AZUL + "MENU PRINCIPAL" + RESET)
        print(AZUL + "="*26 + RESET)
        print(CIAN + '| Seleccione operacion   | ' + RESET)
        print(CIAN + '| 1. Registrar Empleado  | ' + RESET)
        print(CIAN + '| 2. Buscador Elementos  | ' + RESET)
        print(CIAN + '| 3. Editar Elementos    | ' + RESET)
        print(CIAN + '| 4. Eliminar Empleado  | ' + RESET)
        print(CIAN + '| 5. Salir               | ' + RESET)
        print(AZUL + "="*26 + RESET)
        return 1
    elif nivel_acceso == "guest": #user: lucasf, pass: lfpass, DNI:42111444
        print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
        print()
        print(AZUL + "MENU PRINCIPAL" + RESET)
        print(AZUL + "="*26 + RESET)
        print(CIAN + '| Seleccione operacion   | ' + RESET)
        print(CIAN + '| 1. Buscador Elementos  | ' + RESET)
        print(CIAN + '| 2. Salir               | ' + RESET)
        print(AZUL + "="*26 + RESET)
        return 0