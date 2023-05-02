'''

Uma loja utiliza o código V para transação à vista e P para transação a prazo.
Faça um programa que receba
o código e o valor de quinze transações, calcule e mostre:
o valor total das compras à vista;
o valor total das compras a prazo;
o valor total das compras efetuadas;
e o valor da primeira prestação das compras a prazo juntas,
sabendo-se que serão pagas em três vezes.

'''
valor_vista = float(0)
valor_prazo = float(0)
valor_total = float(0)
valor_prestacao = float(0)

cont = 0

while (cont < 5):
    print('Digite V para transação à vista e P para transação a prazo.')
    codigo = input('Digite o codigo da transação: ').lower()
    valor = float(input('Digite o valor da transação: '))
    print('-' * 50)

    if (codigo == 'v'):
        valor_vista = valor_vista + valor
    elif (codigo == 'p'):
        valor_prazo = valor_prazo + valor
        valor_prestacao = valor_prestacao + (valor / 3)
    valor_total = valor_total + valor
    cont = cont + 1

print(f'Valor total das compras à vista: {valor_vista}')
print(f'Valor total das compras a prazo: {valor_prazo}')
print(f'Valor total das compras efetuadas: {valor_total}')
print(
    f'Valor da primeira prestação das compras a prazo juntas: {valor_prestacao}')  # noqa
