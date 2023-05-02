'''
Faça um programa que mostre as tabuadas dos números de 1 a 10

'''
numero = 1
for i in range(10):
    for j in range(11):
        mul = numero * j
        print(f'{numero} x {j} = {mul}')
    numero += 1
    print('-' * 20)
