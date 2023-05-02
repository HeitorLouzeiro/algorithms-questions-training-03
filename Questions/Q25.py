'''

Uma agência bancária possui vários clientes que podem fazer
investimentos com rendimentos mensais,
conforme a tabela a seguir:
Tipo descrição rendimento mensal
1 Poupança 1,5%
2 Poupança plus 2%
3 Fundos de renda fixa 4%
Faça um programa que leia o código do cliente, o tipo do investimento
e o valor investido, e que calcule
e mostre o rendimento mensal de acordo com o tipo do investimento. No final,
o programa deverá mostrar
o total investido e o total de juros pagos.
A leitura terminará quando o código do cliente digitado for menor ou igual a 0.

'''
space = '-' * 50
count = 1


while count != 0:
    print('1 - Poupança')
    print('2 - Poupança Plus')
    print('3 - Fundos de renda fixa')
    print('0 - Sair')
    codigo = int(input('Digite o código do cliente: '))
    print(space)

    if codigo <= 0:
        print('Programa encerrado.')
        count = 0
        break

    if codigo == 1:
        rendimento = 1.5
    elif codigo == 2:
        rendimento = 2
    elif codigo == 3:
        rendimento = 4
    else:
        print('Código inválido.')
        break

    valor = float(input('Digite o valor investido: '))
    print(space)
    rendimento = valor * (rendimento / 100)

    print(f'O total investido é de R$ {valor:.2f}')
    print(f'O total de juros pagos é de R$ {rendimento:.2f}')

print('-' * 50)
