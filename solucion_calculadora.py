a = input('Ingrese un numero: ')
operacion = input('Ingrese un operador: ')
b = input('Ingrese un numero: ')
operadores = ['+', '-', '*', '/', '//' '%']
resultado = []
aux = []

# append es el unico operador que me funciono despues de varias pruebas
for j in range(0, len(operadores), 1):
    if (operacion != operadores[j]):
        aux.append(operadores[j])

# Descomentando la siguiente linea podemos verificar si la variable aux esta funcionando correctamente
# print(aux)

# Cuando la operacion introducida no se encuentre en la lista de operaciones dara como resultado la siguiente impresion:
if (aux == operadores):
    print('esta operacion no existe')
# Si la operacion introducida se encuentra en la lista de operaciones evaluaremos si los datos en las variables a y b son numeros
elif (a.isnumeric() and b.isnumeric()):
    for i in range(0, len(operadores), 1):
        # Cuando la operacion introducida se encuentre dentro de la lista de operadores y los datos de a y b sean numeros vamos a realizar la operacion
        if (operacion == operadores[i]):
            resultado = [a, operadores[i], b]
    complement = ''.join(resultado)
    print(eval(complement))
    # join() convierte una lista en un string unico y eval() realiza una operacion algebraica si esta es posible dentro de un conjunto de caracteres (string)

# Cuando los datos en las variables a y b no sean numeros vamos a recibir como respuesta el siguiente mensaje
else:
    print("Alguno de los valores introducidos no es un numero")
