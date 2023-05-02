'''

Faça um programa que receba a idade, o peso, a altura, a cor dos olhos
(A — azul; P — preto; V — verde; e C — castanho)
e a cor dos cabelos
(P — preto; C — castanho; L — louro; e R — ruivo) de seis pessoas,
calcule e mostre:
a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
a média das idades das pessoas com altura inferior a 1,50 m;
a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
a quantidade de pessoas ruivas e que não possuem olhos azuis.

'''
qtd_pessoas_idade50_peso60 = 0
somaIdade_abaixo150 = 0
qtd_pessoas_olhos_azuis = 0
qtd_pessoas_ruivas_sem_olhos_azuis = 0


cont = 0
while (cont < 6):
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    print('A — azul; P — preto; V — verde; e C — castanho')
    corOlhos = input('Digite a cor dos olhos: ').upper()
    print('P — preto; C — castanho; L — louro; e R — ruivo')
    corCabelos = input('Digite a cor dos cabelos: ').upper()
    print('-' * 50)

    if (idade > 50 and peso < 60):
        qtd_pessoas_idade50_peso60 = qtd_pessoas_idade50_peso60 + 1

    if (altura < 1.50):
        somaIdade_abaixo150 = somaIdade_abaixo150 + idade

    if (corOlhos == 'A'):
        qtd_pessoas_olhos_azuis = qtd_pessoas_olhos_azuis + 1

    if (corCabelos == 'R' and corOlhos != 'A'):
        qtd_pessoas_ruivas_sem_olhos_azuis = qtd_pessoas_ruivas_sem_olhos_azuis + 1  # noqa

    cont = cont + 1

media_idades_abaixo_150 = somaIdade_abaixo150 / 6
porcentagem_olhos_azuis = (qtd_pessoas_olhos_azuis / 6) * 100


# Exibindo os resultados
print('-' * 50)
print('Resultados:')
print(
    f'Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg:{qtd_pessoas_idade50_peso60}')  # noqa
print(
    f'Média das idades das pessoas com altura inferior a 1,50 m: {media_idades_abaixo_150:.2f}')  # noqa
print(
    f'Porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas: {porcentagem_olhos_azuis:.2f}%')  # noqa
print(
    f'Quantidade de pessoas ruivas e que não possuem olhos azuis: {qtd_pessoas_ruivas_sem_olhos_azuis}')  # noqa
