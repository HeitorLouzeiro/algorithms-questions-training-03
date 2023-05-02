'''

Faça um programa que receba várias idades,
calcule e mostre a média das idades digitadas.
Finalize digitando idade igual a zero.

'''
cont = 1
while cont > 0:
    idade = int(input('Digite a primeira idade: '))
    idade2 = int(input('Digite a segunda idade: '))
    if idade == 0 or idade2 == 0:
        print('Fim do programa!')
        cont = 0
        print('-' * 50)
        break

    media = (idade + idade2) / 2
    print('A média das idades digitadas é: ', media)
    print('-' * 50)
    print('Digite em uma das idades 0 para sair do programa!')
    print('-' * 20)
