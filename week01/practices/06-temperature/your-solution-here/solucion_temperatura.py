
temperaturas_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76,
                  80, 69, 80, 83, 68, 79, 61, 53, 50, 49, 53, 48, 45, 39]

temp_max = max(temperaturas_C)
temp_min = min(temperaturas_C)
promedio = sum(temperaturas_C)/len(temperaturas_C)
print('temperatura minima:', temp_min)
print('temperatura maxima:', temp_max)
print('promedio de la temperatura en 24 horas:', promedio)

prod = [i * 1.8 for i in temperaturas_C]


F = [i + 32 for i in prod]
print('La temperatura leida en grados Fahrenheit: ', F)


# Temperaturas igual o superior a 70ºC
cambio_refrigeracion = "no"
auxiliar = 0
igual_supe = 0
num_desco = 0

for i in range(0, len(temperaturas_C), 1):

    if (temperaturas_C[i] >= 70):
        auxiliar += 1
        if (auxiliar > 4):
            cambio_refrigeracion = "El sistema de refrigeracion debe ser cambiado"

    if (temperaturas_C[i] > 80):
        cambio_refrigeracion = "El sistema de refrigeracion debe ser cambiado"

    if (temperaturas_C[i] == num_desco):
        temperaturas_C[i] = round(promedio, 2)

if (promedio > 65):
    cambio_refrigeracion = "El sistema de refrigeracion debe ser cambiado"


if (cambio_refrigeracion != "no"):
    print(cambio_refrigeracion)

print(temperaturas_C)
