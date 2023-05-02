'''

Faça um programa que receba o tipo da ação, ou seja,
uma letra a ser comercializada na bolsa de valores,
o preço de compra e o preço de venda de cada ação e que calcule e mostre:
o lucro de cada ação comercializada;
a quantidade de ações com lucro superior a R$ 1.000,00;
a quantidade de ações com lucro inferior a R$ 200,00;
o lucro total da empresa.
Finalize com o tipo de ação 'F'

'''
count = 1

lucroTotal = float(0)

qtdLucroSuperior1000 = 0
qtdLucroInferior200 = 0

while count > 0:
    tipoAcao = input('Digite o tipo da ação: ').upper()
    if tipoAcao == 'F':
        count = 0
        break
    else:
        precoCompra = float(input('Digite o preço de compra: '))
        precoVenda = float(input('Digite o preço de venda: '))
        lucro = precoVenda - precoCompra
        lucroTotal = lucroTotal + lucro

        if lucro > 1000:
            qtdLucroSuperior1000 = qtdLucroSuperior1000 + 1

        if lucro < 200:
            qtdLucroInferior200 = qtdLucroInferior200 + 1

        print('Tipo da ação: ', tipoAcao)
        print('Lucro: R$', lucro, '\n')
        print('-' * 50)
print('Quantidade de ações com lucro superior a R$ 1.000,00: ',
      qtdLucroSuperior1000)
print('Quantidade de ações com lucro inferior a R$ 200,00: ',
      qtdLucroInferior200)
print('Lucro total da empresa: ', lucroTotal)
