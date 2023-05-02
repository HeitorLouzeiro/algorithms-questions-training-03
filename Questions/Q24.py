'''

Faça um programa que receba um conjunto de valores inteiros e positivos,
calcule e mostre o maior e o
menor valor do conjunto. Considere que:
para encerrar a entrada de dados, deve ser digitado o valor zero;
para valores negativos, deve ser enviada uma mensagem;
os valores negativos ou iguais a zero não entrarão nos cálculos.

'''

valor = int(input('Digite um valor inteiro e positivo: '))
if valor <= 0:
    print('Valor inválido.')
else:
    maior = valor
    menor = valor

    while valor != 0:
        valor = int(
            input('Digite um valor inteiro e positivo (digite 0 para encerrar): '))  # noqa
        if valor < 0:
            print('Valor inválido.')
        elif valor > 0:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor

    print('O maior valor é:', maior)
    print('O menor valor é:', menor)
