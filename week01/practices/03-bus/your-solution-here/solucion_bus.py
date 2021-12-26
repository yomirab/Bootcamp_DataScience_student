import statistics

stops = [(10, 0), (4, 1), (3, 5), (3, 4),
         (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
flujoPasajeros = 0
cantidadPasajeros = []
maximo = 0
print('numeros de paradas seran:', len(stops))

for i in range(0, len(stops), 1):
    for j in range(0, len(stops[i]), 1):
        # print(stops[i][j])
        if (j == 0):
            # print("La cantidad de personas que entran es: ", stops[i][j])
            flujoPasajeros += stops[i][j]
        else:
            # print("La cantidad de personas que salen es: ", stops[i][j])
            flujoPasajeros -= stops[i][j]

    cantidadPasajeros.append(flujoPasajeros)
    if (flujoPasajeros > maximo):
        maximo = flujoPasajeros
print('cantidad de pasajeros dentro del autobus en cada parada: ', cantidadPasajeros)
print("La cantidad maxima de pasajeros es: ", maximo)
desviacionEstandar = statistics.pstdev(cantidadPasajeros)
print('desviacion estandar :', desviacionEstandar)

# ## Tareas
# 1. Calcula el número de paradas.
# 2. Asigna a una variable una lista cuyos elementos sean el número de pasajeros en cada parada (in-out),
# 3. Halla el máximo de ocupación del autobús.
# 4. Calcula la media de la ocupación. media de stops[0] Y la desviación estandard.
# opción "fea" que implica un recorrido múltiple y datos no asociados
