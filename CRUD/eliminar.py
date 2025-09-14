

VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIAN = '\033[96m'
RESET = '\033[0m'


#Funciones 
def Eliminar_ClaveForanea(id, matriz, columna):
    for i in range(len(matriz)):
        if id == matriz[i][columna]:
            posicion = matriz[i].index("Activo")
            matriz[i][posicion] = "Inactivo"
    return matriz

if __name__ == "__main__":
    print(AMARILLO + "Este archivo no se ejecuta de forma independiente" + RESET)