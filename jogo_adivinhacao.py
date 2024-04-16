from random import randint

dicionario = dict()

dicionario['numero_secreto'] = randint(1,101)

dicionario['tentativas_restantes'] = 10



while True:
    if dicionario['tentativas_restantes'] == 0:
        print(f'você perdeu, o numero secreto era {dicionario['numero_secreto']}')
        break

    while True:
        numero = input('Escolha um número: ')
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('digite apenas números')

    
    if numero == dicionario['numero_secreto']:
        print('você ganhou')
        break
    elif numero > dicionario['numero_secreto']:
        dicionario['tentativas_restantes'] -= 1
        print('menor')
    else:
        print('maior')
        dicionario['tentativas_restantes'] -= 1