# Caracol y el pozo
import statistics

pozo = 125.0
sube = 30.0
resbala = 20.0
distancia = 0.0
dias = 0.0

while distancia <= pozo:
    distancia = distancia + (sube - resbala)
    dias = dias + 1

print('dias tardara en salir de el pozo: ', dias)


pozo = 125.0
resbala = 20.0
dias = 0.0
distancia = 0
i = 0
maximo = 0
minimo = 100

avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

while i < len(avance_cm):
    if (distancia <= pozo):
        distancia = distancia + (avance_cm[i] - resbala)
        dias = dias + 1

    if (avance_cm[i] <= minimo):
        minimo = avance_cm[i]

    if (avance_cm[i] >= maximo):
        maximo = avance_cm[i]

    i = i + 1

st_dev = statistics.pstdev(avance_cm)

print('Desviacion estandar: ' + str(st_dev))
print('dias que tardara en recorrer:', dias)
print('desplazamiento minimo en un dia:', minimo)
print('desplazamiento maximo en un dia:', maximo)
