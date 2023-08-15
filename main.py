class Baraja:
    def __init__(self):
        # Oros, Copas, Espadas, Bastos
        NUMEROS = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
        # Numeros por palo
        PALOS = ["o", "c", "e", "b"]
        # # Naipe, mezclar ambos palos con numeros
        self.naipes = [(numero + palo) for numero in NUMEROS for palo in PALOS]
        # self.baraja_inicial = self.crearBaraja()

    def crearBaraja(self):
        # Convierto en set ya que son desordenados
        self.naipes = set(self.naipes)
        # Vuelvo a convertir en lista para luego poder manipular los elementos
        self.naipes = list(self.naipes)

        return self.naipes

    def mezclar(self):
        n = len(self.naipes)
        mitad = n // 2  # Divido a la mitad la cantidad de cartas en el baraja

        primera_mitad = self.naipes[:mitad]  # ":" Operador de corte
        segunda_mitad = self.naipes[mitad:]

        self.naipes.clear()  # Limpio la lista para dejarla en 0

        for i in range(mitad):
            self.naipes.append(
                segunda_mitad[i]
            )  # Agrego de forma intercalada los elementos de la primer mitad con los de la segunda mitad
            self.naipes.append(primera_mitad[i])

        if n % 2 != 0:
            self.naipes.append(
                segunda_mitad[-1]
            )  # Si la baraja tiene un número impar de cartas, la última carta de la segunda mitad se agrega al final

        return self.naipes

    def barajar(
        self, veces=3
    ):  # Establezco un numero predeterminado de veces que quiero que se mezcle la baraja
        for _ in range(veces):
            self.mezclar()

    def repartir(
        self, jugadores=2, mano=3
    ):  # Establezco como predeterminado que participan 2 jugadores y se reparten 3 cartas para cada uno.
        # Mano: cantidad de cartas que se reparten por jugador
        manos = []
        for _ in range(jugadores):
            mano_jugador = []
            for _ in range(mano):
                mano_jugador.append(
                    self.naipes.pop()
                )  # .pop metodo para entregar los elementos de la posicion que uno desee, en este caso de los ultimos y lo elimina de self.naipes
            manos.append(mano_jugador)
        return manos
