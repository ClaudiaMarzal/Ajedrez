def comprueba_validez_casilla(tablero, enemigo, posicion_comprobando):
    if tablero.tablero[posicion_comprobando] == None:
        return True, True
    elif tablero.tablero[posicion_comprobando][-1] == enemigo:
        return True, False
    else:
        return False, False