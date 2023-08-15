from main import Baraja

# Ejemplo de uso

prueba = Baraja()  # Armo el naipe
print(prueba.naipes)

print(prueba.crearBaraja())  # Creo la Baraja
print(
    prueba.repartir()
)  # Reparto las ultimas cartas de la lista, serian las de arriba o primeras del mazo.
print(prueba.naipes)  # Imprimo naipe para ver cartas restantes

prueba.barajar()  # Barajo las veces por defecto (3) el naipe
print(prueba.naipes)  # Imprimo naipe para corroborar que se haya barajado correctamente
