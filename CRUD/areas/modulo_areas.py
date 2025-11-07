
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'

from estadisticas import promedio_empleados_por_area, cantidad_entidad
from CRUD.actualizar import editar_entidad_archivo
from CRUD.registrar import Ingresar_Numero, obtener_ultimo_codigo, agregar_entidad_archivo
from CRUD.eliminar import eliminar_entidad_archivo
from CRUD.buscador import encontrar_elemento
from impresion import imprimir_archivo
from dataset import archivos

#Registrar Area
def RegistrarArea():
    """
    Registra una nueva área en el archivo CSV usando archivo temporal.
    Lee línea por línea, copia todo y agrega la nueva área al final.
    Usa solo modos 'r' y 'w' como se requiere.
    """
    # Obtener datos de la nueva área
    nombre_area = input("Ingrese el nombre del area a registrar: ").title()
    cantidad_empleados = 0
    
    # Generar ID obteniendo el último ID sin cargar todo el archivo
    id = int(obtener_ultimo_codigo(archivos[1]))                    
    id = id + 1 if id != 0 else 0
    
    # Crear nueva área
    nueva_area = [id, nombre_area, cantidad_empleados, "Activo"]
    
    ok = agregar_entidad_archivo(archivos[1], nueva_area)
    if ok:
        print(f"Se agrego el area {nombre_area} exitosamente!")
    else:
        print("No se pudo registrar al area")

def EstadisticasAreas():
    """Muestra estadísticas de áreas leyendo desde CSV."""
    try:
        areas, areas_inactivas = cantidad_entidad(1, -1)
        empleados, empleados_inactivos = cantidad_entidad(0, 5)
        
        print(AZUL + "="*43 + RESET)
        print(AZUL + "MENU PRINCIPAL -> AREAS -> ESTADISTICAS" + RESET)
        print(AZUL + "="*43 + RESET)
        print(CIAN + "| Opciones:".ljust(42) + "|" + RESET)
        print(CIAN + "| 1 - Ver promedio de empleados por area".ljust(42) + "|" + RESET)
        print(CIAN + "| 0 - Volver".ljust(42) + "|" + RESET)
        print(AZUL + "="*43 + RESET)
        opcion = Ingresar_Numero(MAGENTA + "Seleccione una opcion: " + RESET)
        match opcion:
            case 1:
                promedio_empleados_por_area(empleados, areas)
            case 0:
                return
            case _:
                print(AMARILLO + "Opcion no valida." + RESET)
                print(AZUL + "="*130 + RESET)
                print()
                print(VERDE + "ESTADISTICAS FINALIZADAS" + RESET)
                print(AZUL + "="*130 + RESET)
    except Exception as e:
        print(ROJO + f"Error al obtener estadísticas: {e}" + RESET)
    
#Buscar Area
def BuscarArea():
    """Busca áreas en el archivo CSV por diferentes criterios."""
    try:
        print(AZUL + "MENU PRINCIPAL -> AREAS -> BUSCADOR" + RESET)
        print(AZUL + "="*34 + RESET)
        print(CIAN + "| Opciones:".ljust(33) + "|" + RESET)
        print(CIAN + "| 1 - Id".ljust(33) + "|" + RESET)
        print(CIAN + "| 2 - Nombre".ljust(33) + "|" + RESET)
        print(CIAN + "| 3 - Mostrar areas".ljust(33) + "|" + RESET)
        print(CIAN + "| 4 - Volver".ljust(33) + "|" + RESET)
        print(AZUL + "="*34 + RESET)
        opcion = Ingresar_Numero(MAGENTA + "Ingrese la opcion de busqueda: " + RESET)
        print()
        match opcion:
            case 1:
                # Búsqueda optimizada línea por línea (sin cargar todo)
                busqueda = Ingresar_Numero(MAGENTA + "Ingrese el Id a buscar: " + RESET)
                encontrar_elemento(busqueda, archivos[1], 0, 1)
            case 2:
                # Búsqueda optimizada línea por línea (sin cargar todo)
                busqueda = input(MAGENTA + "Ingrese el nombre a buscar: " + RESET)
                busqueda = busqueda.lower()
                encontrar_elemento(busqueda, archivos[1], 1, 1)
            case 3:
                imprimir_archivo(archivos[1], 1)
            case 4:
                return
    except Exception as e:
        print(ROJO + f"Error al buscar área: {e}" + RESET) 
        
#Editar Area
def EditarArea():
    """Edita un área existente en el archivo CSV."""

    print(AZUL + "="*26 + RESET)
    id_area = Ingresar_Numero(MAGENTA + 'Escriba el id de la area a editar: ' + RESET)
    print(AZUL + "Que campo quiere editar?" + RESET)
    print(CIAN + '1. Nombre' + RESET)
    print(CIAN + '2. Alta Lógica' + RESET)
    valueTochange = Ingresar_Numero(MAGENTA + 'Seleccione una opcion: ' + RESET)
    
    if valueTochange == 1:
        newName = input(MAGENTA + 'Ingrese el nuevo nombre: ' + RESET).title()
        editar_entidad_archivo(archivos[1], id_area, valueTochange, 0, newName)
    elif valueTochange == 2:
        editar_entidad_archivo(archivos[1], id_area, -1, 0, "Activo")
    else:
        print(ROJO + "Opción no válida" + RESET)
        return
    
#Eliminar Area
def EliminarArea():
    """Elimina (marca como Inactivo) un área en el archivo CSV y actualiza dependencias."""
    print(AZUL + "="*26 + RESET)
    areaEliminar = str(input(MAGENTA + "Escriba el id del area o escriba \"Lista\" para obtener la planilla: " + RESET)).lower()
    if areaEliminar == "lista":
        print(AZUL + "Lista de areas:" + RESET)
        imprimir_archivo(archivos[1], 1)
        return
    elif areaEliminar.isnumeric():
        areaEliminar = int(areaEliminar)
        ok = eliminar_entidad_archivo(archivos[1], areaEliminar, 0, 3)
        if ok:
            eliminar_entidad_archivo(archivos[0], areaEliminar, 4, 5)
    else:
        print(AZUL + "Opción no valida" + RESET)
        print()


if __name__ == "__main__":
    print(AZUL + "Modulo de Areas - Sistema CRUD basado en archivos CSV" + RESET)
    print(AZUL + "="*55 + RESET)
   