from movimientos_horiz import mov_validos_horiz
from tablero import Tablero

inicial,final = "Tc3 a8".split()

tablero = Tablero()

letras = ["a", "b", "c", "d", "e", "f", "g", "h"]

estado_inicial = inicial[1]+inicial[2]
estado_final = final

aliado = "B"

enemigo = "B" if aliado == "N" else "N"

lista_mov_posibles = []

def movimientos_validos_general(tablero,pieza,posicion_inicial):
    if pieza == "T":
        mov_validos_horiz(enemigo, estado_inicial, tablero, lista_mov_posibles,letras)
        print(lista_mov_posibles)
        #movimientos vertical
    elif pieza == "A":
        #movimientos diagonales
        print("aaa")
    elif pieza == "D":
        mov_validos_horiz()
        #movimientos vertical
        #movimientos diagonales

movimientos_validos_general(tablero, "T", "c3")