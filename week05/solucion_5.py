# * Las ciudades Shanghai, Beijing, Delhi, Estambul, Karachi, Guangzhou y Kinshasa tienen más de 14 millones de habitantes. El resto de las ciudades de las que tenemos datos tienen 14 millones o menos de habitantes.
# * Las ciudades Delhi, Beijing, Kinshasa, Tokio, Moscow, Jakarta, Seoul y El Cairo son capitales del país donde se encuentran. El resto de las ciudades de las que tenemos datos no son capitales.
# * Las ciudades El Cairo, Kinshasa, Delhi y Tokio tienen una densidad de población por encima de los 20.000 habitantes por $km^2$. El resto de las ciudades de las que tenemos datos no superan los 20.000 habitantes por $km^2$.

import json
import re
import datetime
import time
# millones_habitan_14 = {'Delhi', 'Beijing', 'Kinshasa',
#                        'Tokio', 'Moscow', 'Jakarta', 'Seoul', 'El Cairo'}
# Capitales = {'Shanghai', 'Beijing', 'Delhi',
#              'Estambul', 'Karachi', 'Guangzhou', 'Kinshasa'}
# densidad_poblacion = {'El Cairo', 'Kinshasa', 'Delhi', 'Tokio'}

# # 1.1. ¿De cuántas ciudades (diferentes) tenemos datos? Asumiremos que no hay ninguna ciudad que no cumpla al menos una de las propiedades anteriores.

# print("Todos las localidades son:\t\t{}".format(
#     millones_habitan_14.union(Capitales).union(densidad_poblacion)
# ))

# # 1.2. ¿Cuántas ciudades tienen más de 14 millones de habitantes y una densidad de población por encima de los 20.000 habitantes por $ km ^ 2 $?

# print("Ciudades tienen más de 14 millones de habitantes y una densidad de población por encima de los 20.000 habitantes por $ km ^ 2:\t\t{}".format(
#     millones_habitan_14.union(Capitales).union(densidad_poblacion)
# ))

# # 1.3. ¿Qué ciudades tienen una densidad de población por encima de los 20.000 habitantes por $ km ^ 2 $ pero no más de 14 millones de habitantes?

# print("Densidad de población por encima de los 20.000 habitantes por km ^ 2, pero no más de 14 millones de habitantes:\t\t{}".format(
#     densidad_poblacion.intersection(millones_habitan_14)
# ))

# # 1.4. ¿Cuál es el país con mayor número de ciudades por encima de 14 millones de habitantes? ¿Cuántas ciudades de estas características hay en cada país?

# # Para responder a estas preguntas, nos faltará añadir información al conjunto de datos de ciudades disponible para realizar la actividad. Pensad cuál sería la estructura de datos más adecuada para almacenar esta información extra y calcular la respuesta a la pregunta planteada.


# diccionario = [
#     {'pais': 'India', 'ciudades': ['delhi']},
#     {'pais': 'Republica Democratica del Congo', 'ciudades': ['kinshasa']},
#     {'pais': 'Turkia', 'ciudades': ['Estambul']},
#     {'pais': 'Pakistan', 'ciudades': ['Karachi']},
#     {'pais': 'China', 'ciudades': ['Shangai', 'Beijing', 'Guangzhou']},
# ]


# cantidad = 0
# pais = ''

# for i in diccionario:
#     cantidad = len(i['ciudades'])
#     pais = i['pais']
#     print('Pregunta 2 = Ciudades con mas de 14mm de habitantes: ' +
#           str(cantidad) + ' en ' + pais)
#     if (len(i['ciudades']) > cantidad):
#         cantidad = len(i['ciudades'])
#         pais = i['pais']

# print('Pregunta 1 = El pais con mayor número de ciudades por encima de 14 millones de habitantes es: ' + pais)

# 2. Calculad cuántas horas ha trabajado la persona que ha escrito la siguiente frase:
# sentence = "I started working at 17:22:42 and finished at 22:00:00"
# # # print(lista)

# horas = [str(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
# # print(horas)

# hora_1 = horas[:3]
# hora_2 = horas[3:]

# str1 = ':'.join(hora_1)
# str2 = ':'.join(hora_2)
# conversion_1 = time.strptime(str1, "%H:%M:%S")
# conversion_2 = time.strptime(str2, "%H:%M:%S")
# print(conversion_1)
# print(conversion_2)
# print('Horas', conversion_2.tm_hour - conversion_1.tm_hour, 'Minutos', conversion_2.tm_min -
#       conversion_1.tm_min, 'Segundos', conversion_2.tm_sec - conversion_1.tm_sec)
# print(datetime.timedelta(conversion_1-conversion_2))


# 3. Dada la cadena de caracteres `sentence`, reemplazad todos los espacios en blanco por puntos.
# sentence = " From     time to time, Python makes  an    incompatible change " \
#     " to the   advertised semantics of core language constructs   "
# # puntos = sentence.replace(' ', '...')
# # print(puntos)


# # 4. Dada la misma cadena de caracteres del ejercicio anterior, reemplazad todos los espacios en blanco contiguos por un único punto. Es decir, si encontráis tres espacios en blanco consecutivos, estos se deben reemplazar por un único punto, y no por tres puntos como implementábamos en el ejercicio anterior. Eliminad los espacios que se encuentran al inicio y al final de la cadena antes de sustituirlos por puntos.

# pattern = "^\s+|\s+$"
# s1 = re.sub(pattern, "", sentence)
# sin_espacios = " ".join(s1.split())
# espacio_puntos = sin_espacios.replace(' ', '.')
# print(espacio_puntos)


# 5. Proporcionad una lista con todas las palabras de cuatro letras de la cadena de caracteres `sentence` que empiecen por `t` o `F`.
# hola = " From     time to time, Python makes  an    incompatible change " \
#     " to the   advertised semantics of core language constructs   "
# # regex = '\w[^tF]{4}'
# regex = r'\b[tF]\w{3}\b'
# lista = re.findall(regex, hola)
# print(lista)


# 6. Reemplazad todas las mayúsculas de la cadena `sentence` por interrogantes.
# sentence = " From     time to time, Python makes  an    incompatible change " \
#     " to the   advertised semantics of core language constructs   "
# new_sentence = re.sub("[A-Z]", "?", sentence)
# print(new_sentence)
