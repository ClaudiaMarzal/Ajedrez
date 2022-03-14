from tablero import Tablero

inicial,final = "Ta2 a8".split()

tablero = Tablero()

letras = tablero.letras

estado_inicial = inicial[1]+inicial[2]
estado_final = final

aliado = tablero.tablero[estado_inicial][-1]

enemigo = "B" if aliado == "N" else "N"

columna_inicial = estado_inicial[0]

fila_inicial = estado_inicial[1]

indice_columna_inicial = letras.index(columna_inicial)

lista_mov_posibles = []
def mov_validos_horiz(aliado,enemigo,columna_inicial,fila_inicial_indice_columan_inicial):  
    for i in range(indice_columna_inicial,7,1):
        posicion_comprobando = letras[i+indice_columna_inicial]
        if tablero.tablero[posicion_comprobando][-1] == aliado:
            break
        else:
            lista_mov_posibles.append(posicion_comprobando)
    
    for i in range(0,indice_columna_inicial,-1):
        posicion_comprobando = letras[i+indice_columna_inicial]
        if tablero.tablero[posicion_comprobando][-1] == aliado:
            break
        else:
            lista_mov_posibles.append(posicion_comprobando)
print(tablero)    
mov_validos_horiz(aliado,enemigo,columna_inicial,fila_inicial,indice_columna_inicial)
print(lista_mov_posibles)
