'''

Faça um programa que apresente o menu de opções a seguir:
Menu de opções:
1. Média aritmética
2. Média ponderada
3. Sair
Digite a opção desejada.
Na opção 1: receber duas notas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos,
calcular e mostrar a média ponderada.
Na opção 3: sair do programa.
Verifique a possibilidade de opção inválida. Nesse caso,
o programa deverá mostrar uma mensagem.

'''
cont = 1
space = '-' * 50

while cont > 0:
    print('Menu de opções:')
    print('1. Média aritmética')
    print('2. Média ponderada')
    print('3. Sair')
    opcao = int(input('Digite a opção desejada: '))
    print(space)
    if opcao == 1:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        media = (nota1 + nota2) / 2
        print('Média aritmética: ', media)
        print(space)
    elif opcao == 2:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        peso1 = float(input('Digite o peso da primeira nota: '))
        peso2 = float(input('Digite o peso da segunda nota: '))
        peso3 = float(input('Digite o peso da terceira nota: '))
        media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (
            peso1 + peso2 + peso3)
        print('Média ponderada: ', media)
        print(space)
    elif opcao == 3:
        cont = 0
        break
    else:
        print('Opção inválida!')
    print(space)
