from validez_casilla import comprueba_validez_casilla


def mov_validos_vertical(enemigo,estado_inicial,tablero,lista_mov_posibles):  

    columna_inicial = estado_inicial[0]
    fila_inicial = estado_inicial[1]

    indice_fila_inicial = int(fila_inicial)

    numeros_arriba = [i for i in range(1, indice_fila_inicial)]
    numeros_abajo = [i for i in range(indice_fila_inicial+1,9)]
    listas_numeros = [numeros_abajo, numeros_arriba]
    
    for lista in listas_numeros:
        for numero in lista:
            posicion_comprobando = f"{columna_inicial}{numero}"
            resultado = comprueba_validez_casilla(tablero, enemigo, posicion_comprobando)
            if resultado[0]:
                lista_mov_posibles.append(posicion_comprobando)
                if not resultado[1]:
                    break  
            else:
                break

