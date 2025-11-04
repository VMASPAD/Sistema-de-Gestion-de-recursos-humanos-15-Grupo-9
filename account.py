
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'
import json

#Funciones
def userLog(user=None, password=None):
    try:
        with open("dataset/usuarios.json", "r", encoding="UTF-8") as usu:
                usuarios=json.load(usu)
        usuarios_activos = {usuarios[i]["username"] for i in range(len(usuarios)) if usuarios[i]["estado"]=="Activo"}
        if not user:
            user = input(MAGENTA + "Ingrese su usuario: " + RESET).strip()
        if not password:
            password = input(MAGENTA + "Ingrese su contraseña: " + RESET).strip()
        nivel_acceso = None
        for i in range(len(usuarios)):
            if user == usuarios[i]['username'] and user in usuarios_activos:
                if password == usuarios [i]['password']:
                    nivel_acceso=usuarios[i]['nivel_acceso']
                else: print(ROJO + "El usuario no coincide con la contraseña" + RESET)     
        if not nivel_acceso:
            print (ROJO + "No se encontró el usuario." + RESET)
            return -1  

        if nivel_acceso=="admin": #user: juanp, pass: jp1234, DNI:40123456
            print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
            print()
            
            return 2
        elif nivel_acceso=="user": #user: maria.g, pass: mg2024, DNI:38987456
            print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
            print()
            
            return 1
        elif nivel_acceso == "guest": #user: lucasf, pass: lfpass, DNI:42111444
            print(VERDE + "Bienvenido al sistema de gestion de recursos humanos" + RESET)
            print()
            return 0
        

    except (OSError, FileNotFoundError) as error :
        print("error", error)