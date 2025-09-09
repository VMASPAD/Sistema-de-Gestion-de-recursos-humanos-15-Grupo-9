

#Funciones 
def Eliminar_ClaveForanea(id, matriz, columna):
    for i in range(len(matriz)):
        if id == matriz[i][columna]:
            posicion = matriz[i].index("Activo")
            matriz[i][posicion] = "Inactivo"
    return matriz

if __name__ == "__main__":
    print("Este archivo no se ejecuta de forma independiente")