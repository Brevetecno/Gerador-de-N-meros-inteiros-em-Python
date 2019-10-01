# Instagram: @brevetecno
# Youtube: Brevetecno

# Biblioteca para gerar números aleatórios
from random import randint

# Variável Int para guardar os 6 números
numbers = []

while True:
    print('-----------------------------------')
    print('Gerador de números')
    print('-----------------------------------')

    print('Gerar quantos números?')
    number_qtd = int(input('Resposta: '))

    print('Qual número mínimo?')
    number_min = int(input('Resposta: '))

    print('Qual número máximo?')
    number_max = int(input('Resposta: '))

    print('-----------------------------------')


    for n in range(number_qtd):

        # Adiciona o número aleatório de 1 até 60 na lista numbers
        numbers.append(randint(number_min, number_max))

        # Mostra resultado
        print('{}ª valor - {}'.format((n+1), numbers[n]))


    print('-----------------------------------')
    print('Desenvolvedor - Brevetecno')
    print('-----------------------------------')
    print('')


