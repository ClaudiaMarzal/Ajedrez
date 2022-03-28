class Tablero:
    tablero = {}
    def __init__(self, tablero = {}):
        if tablero != {}:
            self.tablero = tablero
        else:
            letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
            for j in range(8, 0, -1):
                for letra in letras:
                    self.tablero[letra + str(j)] = None
            orden_piezas = ["T", "C", "A", "D", "R", "A", "C", "T"]
            blancas = 0
            negras = 0
            for key in self.tablero:
                if key[1] == "8":
                    self.tablero[key] = orden_piezas[negras] + "-N"
                    negras += 1
                elif key[1] == "1":
                    self.tablero[key] = orden_piezas[blancas] + "-B"
                    blancas += 1
                elif key[1] == "7":
                    self.tablero[key] = "P-N"
                elif key[1] == "2":
                    self.tablero[key] = "P-B"
    def mover(self, inicial, final):
        pieza = self.tablero[inicial]
        self.tablero[inicial] = None
        self.tablero[final] = pieza

    def imprimir_tablero(self):
        for i in range(8, 0, -1):
            fila = "|"
            for key in self.tablero:
                if key[1] == str(i):
                    elemento = self.tablero[key]
                    if elemento == None:
                        elemento = "   "
                    fila += elemento + "|"
            print(" ---" * 8)
            print(fila)
        print(" ---" * 8)

        