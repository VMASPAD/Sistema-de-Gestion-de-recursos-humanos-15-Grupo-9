
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from account import userLog
from dataset import empleados, areas, licencias, usuarios, historial_operaciones
from sign_up import crear_usuario
from impresion import Mostrar_historial_operaciones
from CRUD.registrar import Ingresar_Numero
from CRUD.areas import modulo_areas
from CRUD.licencias import modulo_licencias
from CRUD.usuarios import modulo_usuarios
from CRUD.empleados import modulo_empleados
#region Menu
def Menu():
    while True:
        print(AZUL + "="*34 + RESET)
        print(AZUL + "Opciones de ingreso:" + RESET)
        print(AZUL + "="*34 + RESET)
        print(CIAN + "| 1 - Crear Usuario".ljust(33) + "|" + RESET)
        print(CIAN + "| 2 - Iniciar Sesion".ljust(33) + "|" + RESET)
        print(CIAN + "| 3 - Salir".ljust(33) + "|" + RESET)
        print(AZUL + "="*34 + RESET)
        try:
            opcion = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
        except ValueError:
            print(AMARILLO + "Por favor ingrese un numero valido." + RESET)
            continue
        match opcion:
            case 1:
                crear_usuario(usuarios)
            case 2:
                nivel_acceso = userLog(usuarios)
                opcion = -1
                if nivel_acceso == -1:
                    opcion = 6
                    print()
                else:
                    print()
                    print(VERDE + "Ingreso exitoso" + RESET)
                    print()
                while opcion != 6:
                    print()
                    print(AZUL + "="*34 + RESET)
                    print(AZUL + "MENU PRINCIPAL" + RESET)
                    print(AZUL + "="*34 + RESET)
                    print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                    print(CIAN + "| 1 - Areas".ljust(33) + "|" + RESET)
                    print(CIAN + "| 2 - Empleados".ljust(33) + "|" + RESET)
                    print(CIAN + "| 3 - Licencias".ljust(33) + "|" + RESET)
                    print(CIAN + "| 4 - Usuarios".ljust(33) + "|" + RESET)
                    print(CIAN + "| 5 - Historial de Operaciones".ljust(33) + "|" + RESET)
                    print(CIAN + "| 6 - Cerrar Sesion".ljust(33) + "|" + RESET)
                    print(CIAN + "| 0 - Salir".ljust(33) + "|" + RESET)
                    print(AZUL + "="*34 + RESET)
                    opcion = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                    match opcion:
                        case 1:
                            print()
                            print(AZUL + "="*34 + RESET)
                            print(AZUL + "MENU PRINCIPAL -> AREAS" + RESET)
                            print(AZUL + "="*34 + RESET)
                            print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                            print(CIAN + "| 1 - Buscar Area".ljust(33) + "|" + RESET)
                            if nivel_acceso >= 1:
                                print(CIAN + "| 2 - Ver estadisticas".ljust(33) + "|" + RESET)
                            if nivel_acceso == 2:
                                print(CIAN + "| 3 - Registrar Area".ljust(33) + "|" + RESET)
                                print(CIAN + "| 4 - Editar Area".ljust(33) + "|" + RESET)
                                print(CIAN + "| 5 - Eliminar Area".ljust(33) + "|" + RESET)
                            print(CIAN + "| 0 - Volver".ljust(33) + "|" + RESET)
                            print(AZUL + "="*34 + RESET)
                            tipo = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                            match tipo:
                                case 1:
                                    modulo_areas.BuscarArea(areas)
                                case 2:
                                    if nivel_acceso >= 1:
                                        modulo_areas.EstadisticasAreas(areas)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_areas.RegistrarArea(areas)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_areas.EditarArea()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_areas.EliminarArea()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 0:
                                    print(CIAN + "Volviendo al menu principal..." + RESET)
                                case _:
                                    print(AMARILLO + "Opcion no existente" + RESET)
                        case 2:
                            print()
                            print(AZUL + "="*34 + RESET)
                            print(AZUL + "MENU PRINCIPAL -> EMPLEADOS" + RESET)
                            print(AZUL + "="*34 + RESET)
                            print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                            print(CIAN + "| 1 - Buscar Empleado".ljust(33) + "|" + RESET)
                            if nivel_acceso >= 1:
                                print(CIAN + "| 2 - Ver estadisticas".ljust(33) + "|" + RESET)
                            if nivel_acceso == 2:
                                print(CIAN + "| 3 - Registrar Empleado".ljust(33) + "|" + RESET)
                                print(CIAN + "| 4 - Editar Empleado".ljust(33) + "|" + RESET)
                                print(CIAN + "| 5 - Eliminar Empleado".ljust(33) + "|" + RESET)
                            print(CIAN + "| 0 - Volver".ljust(33) + "|" + RESET)
                            print(AZUL + "="*34 + RESET)
                            tipo = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                            match tipo:
                                case 1:
                                    modulo_empleados.BuscarEmpleado(empleados)
                                case 2:
                                    if nivel_acceso >= 1:
                                        modulo_empleados.EstadisticasEmpleados()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_empleados.RegistrarEmpleado(r"matrices/empleados.txt")
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_empleados.EditarEmpleado()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_empleados.EliminarEmpleado()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 0:
                                    print(CIAN + "Volviendo al menu principal..." + RESET)
                                case _:
                                    print(AMARILLO + "Opcion no existente" + RESET)
                        case 3:
                            print()
                            print(AZUL + "="*34 + RESET)
                            print(AZUL + "MENU PRINCIPAL -> LICENCIAS" + RESET)
                            print(AZUL + "="*34 + RESET)
                            print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                            print(CIAN + "| 1 - Buscar Licencia".ljust(33) + "|" + RESET)
                            if nivel_acceso >= 1:
                                print(CIAN + "| 2 - Ver estadisticas".ljust(33) + "|" + RESET)
                            if nivel_acceso == 2:
                                print(CIAN + "| 3 - Registrar Licencia".ljust(33) + "|" + RESET)
                                print(CIAN + "| 4 - Editar Licencia".ljust(33) + "|" + RESET)
                                print(CIAN + "| 5 - Eliminar Licencia".ljust(33) + "|" + RESET)
                            print(CIAN + "| 0 - Volver".ljust(33) + "|" + RESET)
                            print(AZUL + "="*34 + RESET)
                            tipo = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                            match tipo:
                                case 1:
                                    modulo_licencias.BuscarLicencia(licencias, empleados)
                                case 2:
                                    if nivel_acceso >= 1:
                                        modulo_licencias.EstadisticasLicencias(licencias)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_licencias.RegistrarLicencia(licencias)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_licencias.EditarLicencia()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_licencias.EliminarLicencia()
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 0:
                                    print(CIAN + "Volviendo al menu principal..." + RESET)
                                case _:
                                    print(AMARILLO + "Opcion no existente" + RESET)
                        case 4:
                            print(AZUL + "MENU PRINCIPAL -> USUARIOS" + RESET)
                            print(AZUL + "="*34 + RESET)
                            print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                            print(CIAN + "| 1 - Buscar Usuario".ljust(33) + "|" + RESET)
                            if nivel_acceso == 2:
                                print(CIAN + "| 2 - Crear Usuario".ljust(33) + "|" + RESET)
                                print(CIAN + "| 3 - Eliminar Usuario".ljust(33) + "|" + RESET)
                                print(CIAN + "| 4 - Editar Usuario".ljust(33) + "|" + RESET)
                            print(CIAN + "| 0 - Volver".ljust(33) + "|" + RESET)
                            print(AZUL + "="*34 + RESET)
                            tipo = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                            match tipo:
                                case 1:
                                    modulo_usuarios.buscar_usuarios(usuarios)
                                case 2:
                                    if nivel_acceso == 2:
                                        crear_usuario(usuarios)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_usuarios.eliminar_usuario(usuarios)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_usuarios.editar_usuario(usuarios)
                                    else: print(ROJO + "No tiene permisos para realizar esta accion" + RESET)
                                case 0:
                                    print(CIAN + "Volviendo al menu principal..." + RESET)
                                case _:
                                    print(AMARILLO + "Opcion no existente" + RESET)
                                    print(AZUL + "="*130 + RESET)
                        case 5:
                            print()
                            print(AZUL + "="*34 + RESET)
                            print(AZUL + "MENU PRINCIPAL -> HISTORIAL DE OPERACIONES" + RESET)
                            print(AZUL + "="*34 + RESET)
                            print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
                            print(CIAN + "| 1 - Historial de Operaciones".ljust(33) + "|" + RESET)
                            print(CIAN + "| 0 - Volver".ljust(33) + "|" + RESET)
                            print(AZUL + "="*34 + RESET)
                            tipo = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
                            match tipo:
                                case 1:
                                    Mostrar_historial_operaciones(historial_operaciones)
                                case 0:
                                    print(CIAN + "Volviendo al menu principal..." + RESET)
                                case _:
                                    print(AMARILLO + "Opcion no existente" + RESET)
                            
                        case 6:
                            print(VERDE + "Cerrando sesion..." + RESET)
                        case 0:
                            print()
                            print(VERDE + "Gracias por usar el sistema de gestion de recursos humanos." + RESET)
                            print(VERDE + "Saliendo del programa..." + RESET)
                            print()
                            return
                        case _:
                            print(AMARILLO + "Opcion no existente" + RESET)
            case 3:
                print()
                print(VERDE + "Gracias por usar el sistema de gestion de recursos humanos." + RESET)
                print(VERDE + "Saliendo del programa..." + RESET)
                print()
                return


if __name__ == "__main__":
    Menu()

