'''
Faça um programa que receba um número,
calcule e mostre a tabuada desse número.
Exemplo:
Digite um número: 5
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''
numero = input('Digite um número: ')
for i in range(11):
    mul = int(numero) * i
    print(f'{numero} x {i} = {mul}')
