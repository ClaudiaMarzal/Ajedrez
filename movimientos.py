estado_inicial = ""
letras = ["a","b","c","d","e","f","g","h"]
tablero = {}
aliados = tablero[estado_inicial][-1]
enemigo = "B" if aliados == "N" else "N"
columna_inicial = estado_inicial[0]
fila_inicial = estado_inicial[1]
indice_columna_inicial = letras.index(columna_inicial)

def mov_validos_horiz():  
    for i in range(indice_columna_inicial,7,1):
        posicion_comprobando = letras[i+indice_columna_inicial]
        if tablero[posicion_comprobando][-1] == 

    for i in range(0,indice_columna_inicial,-1):

