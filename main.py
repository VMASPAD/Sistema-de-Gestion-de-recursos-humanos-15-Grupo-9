from account import userLog
from dataset import empleados, areas, licencias, usuarios, historial_operaciones
from sign_up import crear_usuario
from impresion import Mostrar_historial_operaciones
import modulo_areas
import modulo_empleados
import modulo_licencias
import modulo_usuarios
#region Menu
def Menu():
    while True:
        print("="*34)
        print("Opciones de ingreso:")
        print("="*34)
        print("| 1 - Crear Usuario".ljust(33) + "|")
        print("| 2 - Iniciar Sesion".ljust(33) + "|")
        print("| 3 - Salir".ljust(33) + "|")
        print("="*34)
        opcion = int(input("Seleccione una opcion: "))
        match opcion:
            case 1:
                crear_usuario(usuarios)
            case 2:
                nivel_acceso = userLog(usuarios)
                opcion = -1
                if nivel_acceso == 0:
                    opcion = 5
                    print()
                else:
                    print()
                    print("Ingreso exitoso")
                    print()
                while opcion != 5:
                    print()
                    print("="*34)
                    print("MENU PRINCIPAL")
                    print("="*34)
                    print("| Opciones:".ljust(33) + "|")
                    print("| 1 - Areas".ljust(33) + "|")
                    print("| 2 - Empleados".ljust(33) + "|")
                    print("| 3 - Licencias".ljust(33) + "|")
                    print("| 4 - Usuarios".ljust(33) + "|")
                    print("| 5 - Historial de Operaciones".ljust(33) + "|")
                    print("| 6 - Cerrar Sesion".ljust(33) + "|")
                    print("| 0 - Salir".ljust(33) + "|")
                    print("="*34)
                    opcion = int(input("Seleccione una opcion: "))
                    match opcion:
                        case 1:
                            print()
                            print("="*34)
                            print("MENU PRINCIPAL -> AREAS")
                            print("="*34)
                            print("| Opciones:".ljust(33) + "|")
                            print("| 1 - Buscar Area".ljust(33) + "|")
                            if nivel_acceso > 1:
                                print("| 2 - Ver estadisticas".ljust(33) + "|")
                            if nivel_acceso == 2:
                                print("| 3 - Registrar Area".ljust(33) + "|")
                                print("| 4 - Editar Area".ljust(33) + "|")
                                print("| 5 - Eliminar Area".ljust(33) + "|")
                            print("| 0 - Volver".ljust(33) + "|")
                            print("="*34)
                            tipo = int(input("Seleccione una opcion: "))
                            match tipo:
                                case 1:
                                    modulo_areas.BuscarArea(areas)
                                case 2:
                                    if nivel_acceso > 1:
                                        modulo_areas.EstadisticasAreas(areas)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_areas.RegistrarArea(areas)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_areas.EditarArea()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_areas.EliminarArea()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 0:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no existente")
                        case 2:
                            print()
                            print("="*34)
                            print("MENU PRINCIPAL -> EMPLEADOS")
                            print("="*34)
                            print("| Opciones:".ljust(33) + "|")
                            print("| 1 - Buscar Empleado".ljust(33) + "|")
                            if nivel_acceso > 1:
                                print("| 2 - Ver estadisticas".ljust(33) + "|")
                            if nivel_acceso == 2:
                                print("| 3 - Registrar Empleado".ljust(33) + "|")
                                print("| 4 - Editar Empleado".ljust(33) + "|")
                                print("| 5 - Eliminar Empleado".ljust(33) + "|")
                            print("| 0 - Volver".ljust(33) + "|")
                            print("="*34)
                            tipo = int(input("Seleccione una opcion: "))
                            match tipo:
                                case 1:
                                    modulo_empleados.BuscarEmpleado(empleados)
                                case 2:
                                    if nivel_acceso > 1:
                                        modulo_empleados.EstadisticasEmpleados()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_empleados.RegistrarEmpleado(empleados)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_empleados.EditarEmpleado()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_empleados.EliminarEmpleado()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 0:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no existente")
                        case 3:
                            print()
                            print("="*34)
                            print("MENU PRINCIPAL -> LICENCIAS")
                            print("="*34)
                            print("| Opciones:".ljust(33) + "|")
                            print("| 1 - Buscar Licencia".ljust(33) + "|")
                            if nivel_acceso > 1:
                                print("| 2 - Ver estadisticas".ljust(33) + "|")
                            if nivel_acceso == 2:
                                print("| 3 - Registrar Licencia".ljust(33) + "|")
                                print("| 4 - Editar Licencia".ljust(33) + "|")
                                print("| 5 - Eliminar Licencia".ljust(33) + "|")
                            print("| 0 - Volver".ljust(33) + "|")
                            print("="*34)
                            tipo = int(input("Seleccione una opcion: "))
                            match tipo:
                                case 1:
                                    modulo_licencias.BuscarLicencia(licencias, empleados)
                                case 2:
                                    if nivel_acceso > 1:
                                        modulo_licencias.EstadisticasLicencias(licencias)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_licencias.RegistrarLicencia(licencias)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_licencias.EditarLicencia()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 5:
                                    if nivel_acceso == 2:
                                        modulo_licencias.EliminarLicencia()
                                    else: print("No tiene permisos para realizar esta accion")
                                case 0:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no existente")
                        case 4:
                            print("MENU PRINCIPAL -> USUARIOS")
                            print("="*34)
                            print("| Opciones:".ljust(33) + "|")
                            print("| 1 - Buscar Usuario".ljust(33) + "|")
                            if nivel_acceso == 2:
                                print("| 2 - Crear Usuario".ljust(33) + "|")
                                print("| 3 - Eliminar Usuario".ljust(33) + "|")
                                print("| 4 - Editar Usuario".ljust(33) + "|")
                            print("| 0 - Volver".ljust(33) + "|")
                            print("="*34)
                            tipo = int(input("Seleccione una opcion: "))
                            match tipo:
                                case 1:
                                    modulo_usuarios.buscar_usuarios(usuarios)
                                case 2:
                                    if nivel_acceso == 2:
                                        crear_usuario(usuarios)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 3:
                                    if nivel_acceso == 2:
                                        modulo_usuarios.eliminar_usuario(usuarios)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 4:
                                    if nivel_acceso == 2:
                                        modulo_usuarios.editar_usuario(usuarios)
                                    else: print("No tiene permisos para realizar esta accion")
                                case 0:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no existente")
                                    print("="*130)
                        case 5:
                            print()
                            print("="*34)
                            print("MENU PRINCIPAL -> HISTORIAL DE OPERACIONES")
                            print("="*34)
                            print("| Opciones:".ljust(33) + "|")
                            print("| 1 - Historial de Operaciones".ljust(33) + "|")
                            print("| 0 - Volver".ljust(33) + "|")
                            print("="*34)
                            tipo = int(input("Seleccione una opcion: "))
                            match tipo:
                                case 1:
                                    Mostrar_historial_operaciones(historial_operaciones)
                                case 0:
                                    print("Volviendo al menu principal...")
                                case _:
                                    print("Opcion no existente")
                            
                        case 6:
                            print("Cerrando sesion...")
                        case 0:
                            print()
                            print("Gracias por usar el sistema de gestion de recursos humanos.")
                            print("Saliendo del programa...")
                            print()
                            return
                        case _:
                            print("Opcion no existente")
            case 3:
                print()
                print("Gracias por usar el sistema de gestion de recursos humanos.")
                print("Saliendo del programa...")
                print()
                return


if __name__ == "__main__":
    Menu()

