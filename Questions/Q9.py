'''

Faça um programa que receba dez idades, pesos e alturas, calcule e mostre:
a média das idades das dez pessoas;
a quantidade de pessoas com
peso superior a 90 kg e altura inferior a 1,50 metro;
ea porcentagem de pessoas com
idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m.

'''
somaIdade = 0
qtd_pessoas_peso90_altura150 = 0
qtd_pessoas_idade10_30_altura190 = 0

for i in range(10):
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    print('-' * 50)

    if (peso > 90 and altura < 1.50):
        qtd_pessoas_peso90_altura150 = qtd_pessoas_peso90_altura150 + 1

    if (idade >= 10 and idade <= 30 and altura > 1.90):
        qtd_pessoas_idade10_30_altura190 = qtd_pessoas_idade10_30_altura190 + 1

    somaIdade = somaIdade + idade

media_idades = somaIdade / 10

porcentagem_idade10_30_altura190 = (
    qtd_pessoas_idade10_30_altura190 / 10) * 100

print('-' * 20)

print(f'Média das idades das dez pessoas: {media_idades:.2f}')
print(
    f'Quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro: {qtd_pessoas_peso90_altura150}')  # noqa
print(
    f'Porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m: {porcentagem_idade10_30_altura190:.2f}%')  # noqa
