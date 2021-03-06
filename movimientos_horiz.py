from validez_casilla import comprueba_validez_casilla

def mov_validos_horiz(enemigo,estado_inicial,tablero,lista_mov_posibles, letras):  

    columna_inicial = estado_inicial[0]

    fila_inicial = estado_inicial[1]

    indice_columna_inicial = letras.index(columna_inicial)

    letras_derecha = letras[indice_columna_inicial+1:]
    letras_izquierda = letras[:indice_columna_inicial]
    listas_letras = [letras_izquierda, letras_derecha]
    for lista in listas_letras:
        for letra in lista:
            posicion_comprobando = f"{letra}{fila_inicial}"
            resultado = comprueba_validez_casilla(tablero, enemigo, posicion_comprobando)
            if resultado[0]:
                lista_mov_posibles.append(posicion_comprobando)
                if not resultado[1]:
                    break  
            else:
                break

