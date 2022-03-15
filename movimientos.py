from tablero import Tablero

inicial,final = "Tc3 a8".split()

tablero = Tablero()

letras = ["a", "b", "c", "d", "e", "f", "g", "h"]

estado_inicial = inicial[1]+inicial[2]
estado_final = final

aliado = "B"



lista_mov_posibles = []
def mov_validos_horiz(aliado,estado_inicial,tablero,lista_mov_posibles):  
    enemigo = "B" if aliado == "N" else "N"

    columna_inicial = estado_inicial[0]

    fila_inicial = estado_inicial[1]

    indice_columna_inicial = letras.index(columna_inicial)

    letras_derecha = letras[indice_columna_inicial+1:]
    letras_izquierda = letras[:indice_columna_inicial]
    for i in range(indice_columna_inicial + 1,7):
        posicion_comprobando = letras[i+indice_columna_inicial]+ fila_inicial

        if tablero.tablero[posicion_comprobando] == None:
            lista_mov_posibles.append(posicion_comprobando)
        elif tablero.tablero[posicion_comprobando][-1] == enemigo:
            lista_mov_posibles.append(posicion_comprobando)
            break
        else: #Si no es enemiga o vacia es aliada
            break
    
    for i in range(indice_columna_inicial-1,0,-1):
        posicion_comprobando = letras[i+indice_columna_inicial]+ fila_inicial
        if tablero.tablero[posicion_comprobando] == None:
            lista_mov_posibles.append(posicion_comprobando)
        elif tablero.tablero[posicion_comprobando][-1] == enemigo:
            lista_mov_posibles.append(posicion_comprobando)
            break
        else:
            break

mov_validos_horiz(aliado,estado_inicial,tablero,lista_mov_posibles)
tablero.imprimir_tablero()  
print(lista_mov_posibles)
