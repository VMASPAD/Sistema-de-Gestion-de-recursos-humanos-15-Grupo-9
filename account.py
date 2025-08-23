# return nivel de acceso
def userOptionAcces(level):
    if level == 2:
        return 2
    elif level == 1:
        return 1
    elif level == 0:
        return 0

def userLog(user, password):
    if user == "admin" and password == "admin":
        print("Bienvenido al sistema de gestion de recursos humanos")
        print("="*26)
        print('| Seleccione operacion   | ')
        print('| 1. Gestionar Area      | ')
        print('| 2. Gestionar Licencias | ')
        print('| 3. Gestionar Empleados | ')
        print('| 4. Salir               | ')
        print("="*26)
        return 2

    