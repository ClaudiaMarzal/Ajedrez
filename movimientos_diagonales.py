from validez_casilla import comprueba_validez_casilla

def mov_validos_vertical(enemigo,estado_inicial,tablero,lista_mov_posibles, letras):  

    columna_inicial = estado_inicial[0]

    fila_inicial = estado_inicial[1]

    indice_columna_inicial = letras.index(columna_inicial)
    indice_fila_inicial =  int(fila_inicial)

    letras_derecha = letras[indice_columna_inicial+1:]
    letras_izquierda = letras[:indice_columna_inicial]
    listas_letras = [letras_izquierda, letras_derecha]

    numeros_arriba = [i for i in range(1, indice_fila_inicial)]
    numeros_abajo = [i for i in range(indice_fila_inicial+1,9)]
    listas_numeros = [numeros_abajo, numeros_arriba]

    lista_rangos = [min(len(letras_izquierda), len(numeros_abajo)), min(len(letras_derecha), len(numeros_arriba))]

    for i in range(len(lista_rangos)):
        for j in range(lista_rangos[i]):
            posicion_comprobando = f"{listas_letras[i][j] + 1}{listas_numeros[i][j] + 1}"
            
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

