class Baraja:
    def __init__(self):
        # Oros, Copas, Espadas, Bastos
        numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
        # Numeros por palo
        palos = ["o", "c", "e", "b"]
        # # Naipe, mezclar ambos palos con numeros
        self.naipes = [(numero + palo) for numero in numeros for palo in palos]

    def crearBaraja(self):
        # Convierto en set ya que son desordenados
        self.naipes = set(self.naipes)
        # Vuelvo a convertir en lista para luego poder manipular los elementos
        self.naipes = list(self.naipes)

        return self.naipes

    def barajar(
        self, veces=3
    ):  # Establezco un numero predeterminado de veces que quiero que se mezcle la baraja
        for v in range(veces):
            n = len(self.naipes)
            mitad = n // 2  # Divido a la mitad la cantidad de cartas en el baraja

            # ":" Operador de corte , aca seria desde el inicio hasta :
            primera_mitad = self.naipes[:mitad]
            segunda_mitad = self.naipes[mitad:]

            self.naipes.clear()  # Limpio la lista para dejarla en 0

            for i in range(mitad):
                self.naipes.append(
                    segunda_mitad[i]
                )  # Agrego de forma intercalada los elementos de la primer mitad con los de la segunda mitad
                self.naipes.append(primera_mitad[i])

            return self.naipes

    def repartir(
        self, jugadores=2, mano=3
    ):  # Establezco como predeterminado que participan 2 jugadores y se reparten 3 cartas para cada uno.
        # Mano: cantidad de cartas que se reparten por jugador
        manos = []
        for j in range(jugadores):
            mano_jugador = []
            for m in range(mano):
                mano_jugador.append(
                    self.naipes.pop()
                )  # .pop metodo para entregar los elementos de la posicion que uno desee, en este caso de los ultimos y lo elimina de self.naipes
            manos.append(mano_jugador)
        return manos

    def __str__(self):
        return f"Es hora de jugar!!!"
