import random
opciones = ('piedra', 'papel', 'tijera')
partidas_maximas = 3
partidas_ganadas = 2

maquina = random.choice(opciones)

eleccion_jugador = input(
    'para poder jugar debes escoger uno de las siguientes opciones: Piedra , Papel , Tijera  : ')


for i in range(0, len(opciones), 1):
    if (opciones[i] != eleccion_jugador):
        eleccion_jugador = input(
            'para poder jugar debes escoger uno de las siguientes opciones: piedra , papel , tijera  : ')
