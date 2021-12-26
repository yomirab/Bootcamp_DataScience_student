

# import unittest

# # Ejercicio 1
# # Escribe una función que devuelva el mayor de dos números


# def greater(a, b):

#     if a > b:
#         print('El número mayor es:', a)
#     elif a < b:
#         print('El numero mayor es:', b)
#     return a, b


# print(greater(15, 90))


# # Ejercicio 2
# # Ahora escribe una función que devuelva el elemento más grande en una lista.

# x = [8, 9, 5, 6, 10]


# def greatest(lista):
#     control = 0

#     for i in range(len(lista)):
#         if lista[i] > control:
#             control = lista[i]
#     return control


# print('numero mayor de la lista:', greatest(x))

# # Ejercicio 3
# # Escribe una función que sume todos los elementos de una lista


# h = [5, 789, 2, 4]


# def sum_all(suma):
#     sumita = 0
#     for i in range(len(suma)):
#         sumita = sumita + suma[i]
#     return sumita


# print('suma total de la lista:', sum_all(h))

# # Ejercicio 4
# # Escribe otra función que multiplique todos los elementos de una lista

# c = [4, 7, 8]


# def mult_all(multiplica):
#     mul = 1
#     for i in range(len(multiplica)):
#         mul = mul * multiplica[i]
#     return mul


# print('multiplicacion de la lista:', mult_all(c))


# # Ejercicio 5.
# # Ahora combine esas dos ideas y escriba una función que reciba una lista y "+" o "*" y genere los resultados correspondientes

# lis_5 = [8, 9, 10]


# def oper_all(arr, operador):
#     sumas = 0
#     multi = 1
#     resultado = 0

#     for i in range(len(arr)):
#         if (operador == '+'):
#             sumas = sumas + arr[i]
#             resultado = sumas
#         elif (operador == '*'):
#             multi = multi * arr[i]
#             resultado = multi
#         else:
#             print('el operador no esta definido')

#     return resultado


# multiplicando_sumando = oper_all(lis_5, '+')
# print('resultado de ejercicio 5:', multiplicando_sumando)

# Ejercicio 6
# Función que devuelva el factorial de un número

# def factoriales(n):
#     factor = 1
#     i = 1
#     if n == 0:
#         return 1
#     while (n > i):
#         factor = factor * i
#         i = i + 1
#     return factor


# e = 8
# print('factorial:', factoriales(e))

# Ejercicio 7.
# Escribe una función que tome una lista y devuelva una lista de valores únicos.


# def unique(arr):
#     lst = []
#     for i in range(0, len(arr), 1):
#         for j in range(0, len(arr), 1):
#             if (arr[i] != arr[j]):
#                 lst.append(arr[j])


#         return lst


# arr = [7, 7, 7, 9, 2]
# print('numeros unicos:', unique(arr))

# Ejercicio 8.
# Escribe una función que devuelva la moda de una lista, es decir: el elemento que aparece más veces.

# def mode_counter(arr):
#     lst = []
#     for i in range(0, len(arr), 1):
#         for j in range(0, len(arr), 1):
#             if (arr[i] == arr[j]):
#                 lst.append(arr[j])

#         return lst


# arr = [7, 7, 7, 9, 2]
# print('elementos que se repiten:', mode_counter(arr))

# ejercicio 9
# Escribe una función que calcule la desviación estándar de una lista.

# from statistics import stdev
# x = [6, 8, 9]


# def st_dev(x):
#     distancia_media = []
#     distanci_cuadrado = []
#     a = []

#     suma = sum(x)
#     media = suma / len(x)

#     for i in range(len(x)):
#         distancia_media.append(x[i] - media)
#     for i in range(len(distancia_media)):
#         distanci_cuadrado.append(distancia_media[i]**2)

#     a = (sum(distanci_cuadrado)/len(distancia_media))**0.5

#     return a


# print(st_dev(x))

# Ejericio 10
# Escribe una función para comprobar si una cadena es un pangrama, es decir: si contiene todas las letras del alfabeto al menos una vez.
# Tenga en cuenta que las cadenas pueden contener caracteres que no sean letras.

# import string
# entrada = 'abcdefghijklmnopqrstuv'

# cadena = list(entrada)


# def es_pangrama(cadena):

#     alfabeto = string.ascii_lowercase + "ñ"
#     lis_alfa = list(alfabeto)
#     pragma = []
#     print(lis_alfa)
#     for i in range(len(lis_alfa)):
#         for j in range(0, len(cadena), 1):
#             if (lis_alfa[i] == cadena[j]):
#                 pragma.append(cadena[j])
#     if (pragma == lis_alfa):
#         print('la frese es un pragma, contiene todas las letras del abecedario')
#     else:
#         print(
#             'la frase no es una pangrama, porque no estan todas las letras del abcedario')


# print(es_pangrama(cadena))

# Ejercicio 11.
# Escriba una función que reciba una cadena de palabras separadas por comas y devuelva una cadena de palabras separadas por comas ordenadas alfabéticamente.


# Ejercicio 12
# Escribe una función para verificar si una contraseña dada es segura (al menos 8 caracteres, al menos una minúscula,
#  al menos una mayúscula, al menos un número y al menos un carácter especial). Debería mostrar True si es fuerte y False si no.
# `Caracteres especiales válidos:

# import os

# texto = 'sjjjjjj2$jJs'
# caracteres = '@ ! $ % & () ^ * [] {} `'
# carac = caracteres.split(' ')


# def check_pass(pw, permitidos):
#     has_mayus = False
#     has_lower = False
#     has_digit = False
#     has_spec = False
#     if len(pw) < 8:
#         print("La contrasena debe tener minimo 8 caracteres")

#     for i in pw:
#         if i.isupper():
#             has_mayus = True
#         if i.islower():
#             has_lower = True
#         if i.isdigit():
#             has_digit = True

#     if any(letra in texto for letra in permitidos):
#         has_spec = True

#     if not has_mayus:
#         print('su contrasena debe tener un caracter en mayuscula')
#     if not has_lower:
#         print('su contrasena debe tener un caracter en minuscula')
#     if not has_digit:
#         print('su contrasena debe tener al menos un numero')
#     if not has_spec:
#         print(
#             'Debe tener al menos uno de los siguientes caracteres: # @! $% & () ^ * [] {}')
#     if has_mayus and has_lower and has_digit and has_spec:
#         print('todo ok')


# check_pass(texto, carac)


# Ejercicio 13

# Definid una función que reciba como parámetros dos valores (x  y) que serán dos vectores de enteros, y devuelva la `distancia euclídea` entre los puntos representados por los vectores. Es necesario que el cuerpo de la función contenga una única expresión, que calcule y evuelva el resultado. Los vectores pueden tener un tamaño arbitrario, pero ambos vectores tendrán el mismo número de elementos. **Solo se pueden utilizar funciones de la librería estándar de Python**.

# a = [3, 6]
# b = [7, 8]


# def funcion1(x, y):

#     return (sum([abs(coord[0] - coord[1])**2 for coord in zip(x, y)]))**0.5


# print(funcion1(a, b))


# Ejercicio 14

# Definid una función que reciba como parámetros dos valores (x  y) que serán dos vectores de enteros, y devuelva l
# a `distancia de Manhattan` entre los puntos representados por los vectores. Es necesario que el cuerpo de la función contenga
# una única expresión, que calcule y devuelva el resultado. Los vectores pueden tener un tamaño arbitrario, pero ambos vectores
# tendrán el mismo número de elementos. **Solo se pueden utilizar funciones de la librería estándar de Python**.

# a = [3, 6]
# b = [7, 8]


# def funcion(x, y):

#     return sum([abs(coord[0] - coord[1]) for coord in zip(x, y)])


# print(funcion(a, b))


# Ejercicio 15

# Definid una función `compute_all_distances` que reciba como parámetros dos valores $(x \quad y)$ que
# serán dos vectores de enteros, y devuelva una tupla de dos elementos, con las `distancias euclidiana` y distancia de Manhattan` entre los puntos representados por los vectores. Los vectores pueden tener un tamaño arbitrario,
# pero ambos vectores tendrán el mismo número de elementos. **Solo se pueden utilizar funciones de la librería estándar de Python**.

# Para ello, encapsulad el código de las funciones de las actividades anteriores dentro de la función `compute_all_distances`.

# a = [3, 6]
# b = [7, 8]


# def compute_all_distances(x, y):

#     return (sum([abs(coord[0] - coord[1]) for coord in zip(x, y)]), (sum([abs(coord[0] - coord[1])**2 for coord in zip(x, y)]))**0.5)


# print(compute_all_distances(a, b))

# Ejercicio 16

# En la frutería del barrio tienen un problema que requiere de nuestra ayuda. Reiteradamente, se les rompen las estanterías donde ponen las naranjas, y quieren evitar que esto vuelva a pasar. Han calculado que los estantes de madera soportan sin problemas un peso de `50 kilos`, y los de plástico `30 kilos`, pero siempre dudan de si pueden añadir algún piso de naranjas más (ya que esto siempre luce más delante de los clientes).

# Las naranjas se encuentran apiladas en una pirámide de base cuadrada. Así pues, en lo alto hay una sola naranja, en el segundo piso hay 4, en el tercer piso hay 9, etc. Los pisos siempre están completos.

# Definid una función que reciba como parámetros el número de pisos de naranjas que quieren hacer, el peso medio de cada naranja, y el tipo de material del estante, y devuelva un booleano indicando si el estante aguantará el peso o no.

# La función siempre recibirá el número de pisos de naranjas, pero los parámetros de peso medio y material son opcionales, y tomarán un valor por defecto de 0.2 y madera ("Wood"), respectivamente.
# def naranjas(pisos, peso = 0.2, material = 50):

# def naranjas(pisos, peso=0.2, material='wood'):
#     cantidad_naranaja_cadapiso = [1, 4, 9, 18, 36, 72, 144, 288]

#     if pisos > len(cantidad_naranaja_cadapiso):
#         return print('la cantidad de pisos es superior a la cantidad que soportan los materiales')

#     elif material == 'wood':
#         resistencia = 50
#         naranjas_madera = resistencia / peso  # 250
#         suma = 0
#         for i in range(0, pisos, 1):
#             suma = suma + cantidad_naranaja_cadapiso[i]

#         if suma < naranjas_madera:
#             return print('puedes colocar la cantidad de pisos elegida')
#         else:
#             return print('Elige otra cantidad de pisos, otro peso o otro material')

#     elif material == 'plastic':
#         resistencia = 30
#         naranjas_plastic = resistencia / peso  # 150
#         suma = 0
#         for i in range(0, pisos, 1):
#             suma = suma + cantidad_naranaja_cadapiso[i]

#         if suma < naranjas_plastic:
#             return print('puedes colocar la cantidad de pisos elegida')
#         else:
#             return print('Elige otra cantidad de pisos, otro peso o otro material')

#     else:
#         return print('Elige otra cantidad de pisos, otro peso o otro material')


# naranjas(3, 2, 'plastic')

# Ejercicio 17

# Definid una función que pueda recibir un número de parámetros cualquiera, superior a 1, y que devuelva el resultado de sumar el resultado de aplicar la función que recibe como primer parámetro a cada uno de los otros parámetros.

# Por ejemplo, si la función recibe como primer argumento una función que calcula cuadrados, como segundo argumento un 5, y como tercer argumento un 10, debería devolver 52+102=125.

# Llamad a la función definida con los valores del ejemplo mencionado en el enunciado, y comprobad que se obtiene el resultado correcto. Comprobad también que la función devuelve los resultados esperados para una llamada con dos argumentos y con cinco argumentos.

# def fun(x):
#     num = x**2
#     return num

# x = 3
# print(fun(x))

# def fun1(fun, a, b, c=8, d=9, e=1):
#     if a and b and c and d and e:
#         return fun(a) + fun(b) + fun(c) + fun(d) + fun(e)
#     elif a and b:
#         return fun(a) + fun(b)

# a = 4
# b = 5
# print(fun1(fun, a, b))

# Ejercicio 18

# Definid una función que reciba dos parámetros, una lista de enteros y un entero, y devuelva una lista con los mismos elementos que la lista original eliminando todas las apariciones del entero especificado.

# lista = [5, 7, 4, 7, 9]
# numero = 7

# def num(x, y):
#     for i in x:
#         if i == y:
#             x.remove(i)
#     print('Eliminando el numero que se repite en la lista', x)

# # funcion1 = num(lista, numero)
# # Ejercicio 18.1
# # Implementad una función que **modifique la lista original**. Haced una llamada a la función definida y mostrad que, efectivamente, la lista original se modifica.

# def modifica(k):
#     k.pop(0)
#     print('verificando que la lista original se modifica', k)

# # Ejercicio 17.2

# # Implementad una función que **no modifique** la lista original. Haced una llamada a la función definida y mostrad que, efectivamente, no se modifica la lista original.

# def no_modifica(x):
#     print('No se modifica la lista original', x)

# no_modifica(lista)
# modifica(lista)
# num(lista, numero)
