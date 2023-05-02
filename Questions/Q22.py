'''

Faça um programa que receba a idade e a altura de várias pessoas,
calcule e mostre a média das alturas
daquelas com mais de 50 anos. Para encerrar a entrada de dados,
digite idade menor ou igual a zero.

'''

qtdAlturas = 0
somaAlturas = float(0)
count = 1

while count != 0:
    idade = int(input('Digite a idade: '))
    if idade <= 0:
        print('Fim da entrada de dados.')
        print('-' * 50)
        count = 0
        break

    altura = float(input('Digite a altura: '))
    print('-' * 50)

    if idade > 50:
        qtdAlturas = qtdAlturas + 1
        somaAlturas = somaAlturas + altura

if qtdAlturas == 0:
    print('Não foi possível calcular a média das alturas das pessoas com mais de 50 anos.')  # noqa
else:
    media = somaAlturas / qtdAlturas

    print('A média das alturas das pessoas com mais de 50 anos é: ', media)

print('-' * 50)
