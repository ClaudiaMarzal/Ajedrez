class Tablero:
    tablero = {}
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for j in range(8, 0, -1):
        for letra in letras:
            tablero[letra + str(j)] = None

    orden_piezas = ["T", "C", "A", "D", "R", "A", "C", "T"]
    blancas = 0
    negras = 0
    for key in tablero:
        if key[1] == "8":
            tablero[key] = orden_piezas[negras] + "-N"
            negras += 1
        elif key[1] == "1":
            tablero[key] = orden_piezas[blancas] + "-B"
            blancas += 1
        elif key[1] == "7":
            tablero[key] = "P-N"
        elif key[1] == "2":
            tablero[key] = "P-B"
    
    def imprimir_tablero(self):
        for i in range(8, 0, -1):
            fila = "|"
            for key in self.tablero:
                if key[1] == str(i):
                    elemento = self.tablero[key]
                    if elemento == None:
                        elemento = "   "
                    fila += elemento + "|"
            print(fila)


tablero = Tablero()
print(tablero.imprimir_tablero())