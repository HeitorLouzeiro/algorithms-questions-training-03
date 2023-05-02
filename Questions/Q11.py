'''

Faça um programa que receba o valor de um carro e
mostre uma tabela com os seguintes dados:
preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
o preço final para compra à vista tem desconto de 20%;
a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60; e
os percentuais de acréscimo encontram-se na tabela a seguir.



QuanTidade          percenTual de acr éscimo
de parcelas         sobre o preço final

6                       3%
12                      6%
18                      9%
24                      12%
30                      15%
36                      18%
42                      21%
48                      24%
54                      27%
60                      30%

'''

preco = float(input('Digite o preço do carro: '))

print('-' * 20)


# Cálculo do preço final com desconto de 20%
preco_final = preco * 0.8

print("\nPreço final do carro: R$ {:.2f}".format(preco_final))
print("Tabela de parcelamento:")

# Cálculo do valor da parcela para cada quantidade de parcelas
for parcelas in range(6, 61, 6):
    if parcelas == 6:
        percentual_acrescimo = 0.03
    else:
        # Cálculo do percentual de acréscimo
        # 0.03 + 0.03 * (12 // 6)
        # 12 // 6 = 2
        # 0.06 * 2 = 0.12
        percentual_acrescimo = 0.03 + 0.03 * (parcelas // 6)

    valor_parcela = (preco_final * (1 + percentual_acrescimo)) / parcelas
    print(f'{parcelas}x de R$ {valor_parcela:.2f}')
