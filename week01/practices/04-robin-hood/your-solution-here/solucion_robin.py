from decimal import Subnormal


puntos = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5),
          (0, -2), (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

tuplas = ()
dianas = 0
suma = 0
minimo = 0
tuplas_repetidas = []
primer_cuadrante = []
segundo_cuadrante = []
tercer_cuadrante = []
cuarto_cuadrante = []

for x, j in enumerate(puntos):
    if j in puntos[:x]:  # "ya está anteriormente en la lista"
        tuplas_repetidas.append(j)

for i, a in (puntos):
    if (i >= 0 and a >= 0):
        primer_cuadrante.append((i, a))

    if (i < 0 and a > 0):
        segundo_cuadrante.append((i, a))

    if (i < 0 and a < 0):
        tercer_cuadrante.append((i, a))

    if (i < 0 and a > 0):
        cuarto_cuadrante.append((i, a))

    if (i > 9 and a > 9):
        dianas.append((i, a))
    if (i < -9 and a < -9):
        dianas.append((i, a))
    if (i+a):
        pass
#         suma.append((i, a))


# print(suma)
print('cantidad de flechas que hay que recoger en el bosque:', dianas)
print('tuplas repetidas:', tuplas_repetidas)
print('Primer cuadrante: ', primer_cuadrante)
print('cantidad de fechas en el cuadrante: ', len(primer_cuadrante))
print('Segundo cuadrante: ', segundo_cuadrante)
print('cantidad de fechas en el cuadrante: ', len(segundo_cuadrante))
print('tercer cuadrante: ', tercer_cuadrante)
print('cantidad de fechas en el cuadrante: ', len(tercer_cuadrante))
print('cuarto cuadrante: ', cuarto_cuadrante)
print('cantidad de fechas en el cuadrante: ', len(cuarto_cuadrante))


# 1. Robin Hood es famoso por acertar a una flecha con otra flecha. ¿Lo ha conseguido?

# 2. Calcula cuántos flechazos han caido en cada cuadrante.

# 3. Halla el punto más cercano al centro. Calcula su distancia al centro
# Definir una función que calcula la distancia al centro puede servir de ayuda.

# 4. Si la diana tiene un radio de 9, calcula el número de flechas que hay que recoger al bosque.

# Primer cuadrante "I": Región superior derecha positivo positivo
# Segundo cuadrante "II": Región superior izquierda negativo positivo
# Tercer cuadrante "III": Región inferior izquierda negativo negativo
# Cuarto cuadrante "IV": Región inferior derecha positivo negativo
