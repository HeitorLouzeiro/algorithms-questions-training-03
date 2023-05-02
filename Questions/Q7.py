'''
Faça um programa que receba a idade,
a altura e o peso de cinco pessoas, calcule e mostre:
a quantidade de pessoas com idade superior a 50 anos;
a média das alturas das pessoas com idade entre 10 e 20 anos;
a porcentagem de pessoas com peso inferior a 40 kg
    entre todas as pessoas analisadas.
'''
qtdIdade = float(0)
somaAltura = float(0)
qtdAltura = float(0)
qtdPeso = float(0)

for i in range(5):
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))
    if (idade > 50):
        qtdIdade = qtdIdade + 1
    if (idade >= 10 and idade <= 20):
        somaAltura = somaAltura + altura
        qtdAltura = qtdAltura + 1
    if (peso < 40):
        qtdPeso = qtdPeso + 1

mediaAltura = somaAltura / qtdAltura
porcentagemPeso = (qtdPeso / 5) * 100

print('Quantidade de pessoas com idade superior a 50 anos: ', qtdIdade)
print('Média das alturas das pessoas com idade entre 10 e 20 anos: ', mediaAltura)  # noqa
print('Porcentagem de pessoas com peso inferior a 40 kg: ', porcentagemPeso, '%')  # noqa
