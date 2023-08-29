from main import Baraja

# Ejemplo de uso


juego = Baraja()  # Armo el naipe
print(Baraja())
print("PASO 1------------------------------------")

print(juego.naipes)
print("PASO 2------------------------------------")

print(juego.crearBaraja())  # Creo la Baraja
print("PASO 3------------------------------------")

print(
    juego.repartir()
)  # Reparto las ultimas cartas de la lista, serian las de arriba o primeras del mazo.
print("PASO 4------------------------------------")

print(juego.naipes)  # Imprimo naipe para ver cartas restantes
print("PASO 5------------------------------------")

juego.barajar()  # Barajo las veces por defecto (3) el naipe
print("PASO 6------------------------------------")

print(juego.naipes)  # Imprimo naipe para corroborar que se haya barajado correctamente
print("PASO 7------------------------------------")
print(juego.repartir())
