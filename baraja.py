import random

palos = ['Oro', 'Copa', 'Espada', 'Basto']
cartas = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']


def crearBaraja():
    baraja = []
    for palo in palos:
        for carta in cartas:
            baraja.append(f'{carta} de {palo}')
    return baraja


def eligeCarta(i, longitud):
    return random.randint(longitud-1)


def barajar(baraja):
    for i in range(len(baraja)):
        aux = baraja[i]
        numRandom = eligeCarta(i, len(baraja))
        baraja[i] = baraja[numRandom]
        baraja[numRandom] = aux
    return baraja
