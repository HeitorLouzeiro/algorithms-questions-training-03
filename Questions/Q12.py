'''

Faça um programa que receba dez números inteiros e
mostre a quantidade de números primos dentre os
números que foram digitados

'''

qtdprimo = 0

for i in range(10):
    num = int(input('Digite um número: '))

    primo = True
    for j in range(2, num):
        if num % j == 0:
            primo = False
            break

    if primo and num > 1:
        qtdprimo = qtdprimo + 1
print(f'Foram digitados {qtdprimo} números primos')
