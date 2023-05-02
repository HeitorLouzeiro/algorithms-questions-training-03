'''

Faça um programa que receba a idade e o peso de quinze pessoas,
e que calcule e mostre as médias dos pesos das pessoas da mesma faixa etária.
As faixas etárias são:
de 1 a 10 anos,
de 11 a 20 anos,
de 21 a 30 anos e
de 31 anos para cima

'''

qtd1a10 = 0
qtd11a20 = 0
qtd21a30 = 0
qtd31 = 0
soma1a10 = float(0)
soma11a20 = float(0)
soma21a30 = float(0)
soma31 = float(0)

for i in range(15):
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    print('-' * 50)

    if idade >= 1 and idade <= 10:
        qtd1a10 = qtd1a10 + 1
        soma1a10 = soma1a10 + peso
    elif idade >= 11 and idade <= 20:
        qtd11a20 = qtd11a20 + 1
        soma11a20 = soma11a20 + peso
    elif idade >= 21 and idade <= 30:
        qtd21a30 = qtd21a30 + 1
        soma21a30 = soma21a30 + peso
    elif idade >= 31:
        qtd31 = qtd31 + 1
        soma31 = soma31 + peso

if qtd1a10 > 0:
    media1a10 = soma1a10 / qtd1a10

if qtd11a20 > 0:
    media11a20 = soma11a20 / qtd11a20

if qtd21a30 > 0:
    media21a30 = soma21a30 / qtd21a30

if qtd31 > 0:
    media31 = soma31 / qtd31

print(f'A média de peso das pessoas de 1 a 10 anos é {media1a10}')
print(f'A média de peso das pessoas de 11 a 20 anos é {media11a20}')
print(f'A média de peso das pessoas de 21 a 30 anos é {media21a30}')
print(f'A média de peso das pessoas de 31 anos ou mais é {media31}')
