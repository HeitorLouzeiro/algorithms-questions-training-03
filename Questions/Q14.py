'''

Cada espectador de um cinema respondeu a um questionário
no qual constava sua idade e sua opinião em relação ao filme:
ótimo — 3; bom — 2; regular — 1.
Faça um programa que receba a idade e a opinião de quinze espectadores,
calcule e mostre:
a média das idades das pessoas que responderam ótimo;
a quantidade de pessoas que responderam regular;
e a percentagem de pessoas que responderam bom,
entre todos os espectadores analisados.

'''

qtdotimo = 0
qtdbom = 0
qtdregular = 0

somaotimo = 0
somaidade = 0

for i in range(15):
    idade = int(input('Digite a idade: '))
    print('1 - Regular, 2- Bom, 3 - Otimo')
    opiniao = int(input('Digite a opiniao: '))
    print('-' * 20)
    if opiniao == 3:
        qtdotimo = qtdotimo + 1
        somaotimo = somaotimo + idade

    if opiniao == 2:
        qtdbom = qtdbom + 1

    if opiniao == 1:
        qtdregular = qtdregular + 1

mediaidade = somaotimo / qtdotimo
percentualbom = (qtdbom / 15) * 100

print('Media das idades das pessoas que responderam otimo: ', mediaidade)
print('Quantidade de pessoas que responderam regular: ', qtdregular)
print('Percentual de pessoas que responderam bom: {:.2f}'.format(
    percentualbom), '%')
