class Tablero:
    tablero = []
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for j in range(8, 0, -1):
        fila = []
        for letra in letras:
            fila.append(letra + str(j))
        tablero.append(fila)



tablero = Tablero()
for i in range(8):
    print(tablero.tablero[i])