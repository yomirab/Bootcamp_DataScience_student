hechi_gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
hechi_saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalf = 0
saruman = 0
ronda = ['primer', 'segundo', 'tercero', 'cuarto', 'quinto',
         'sexto', 'septimo', 'octavo', 'noveno', 'decimo']
nombre = ''

for i in range(0, len(hechi_gandalf), 1):
    if (hechi_gandalf[i] > hechi_saruman[i]):
        partidas_ganadas_gandalf = gandalf + 1
        nombre = 'gandalf'
        print('El', ronda[i], 'choque lo gana', nombre, ':',
              hechi_gandalf[i], 'contra', hechi_saruman[i], ', gana el ', hechi_gandalf[i])

    else:
        partidas_ganadas_saruman = saruman + 1
        nombre = 'saruman'
        print('El', ronda[i], 'choque lo gana', nombre, ':',
              hechi_gandalf[i], 'contra', hechi_saruman[i], ', gana el', hechi_saruman[i])


if gandalf > saruman:
    print('Gana Gandalf')
elif gandalf < saruman:
    print('gana Saruman ')
else:
    print('Empate')
