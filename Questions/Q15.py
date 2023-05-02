'''

Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou
não de um novo produto lançado. Para isso, forneceu o sexo do entrevistado
e sua resposta (S — sim; ou N — não).
Sabe-se
que foram entrevistadas dez pessoas.
Faça um programa que calcule e mostre:
o número de pessoas que responderam sim;
o número de pessoas que responderam não;
o número de mulheres que responderam sim;
e a percentagem de homens que responderam não,
entre todos os homens analisados.

'''
sexoM = 0
sexoF = 0

mulheresSim = 0
mulheresNao = 0

homensSim = 0
homensNao = 0


for i in range(10):
    sexo = input('Digite o sexo da pessoa (M/F): ').lower()
    resposta = input('Digite a resposta da pessoa (S/N): ')
    print('-' * 20)

    if sexo == 'm':
        sexoM = sexoM + 1
        if resposta == 'n':
            homensNao = homensNao + 1
        else:
            homensSim = homensSim + 1
    elif sexo == 'f':
        sexoF = sexoF + 1
        if resposta == 's':
            mulheresSim = mulheresSim + 1
        else:
            mulheresNao = mulheresNao + 1

totalSim = mulheresSim + homensSim

totalNao = mulheresNao + homensNao

porcentagemHomemNao = (homensNao / sexoM) * 100

print('O número de pessoas que responderam sim é: ', totalSim)
print('O número de pessoas que responderam não é: ', totalNao)
print('O número de mulheres que responderam sim é: ', mulheresSim)
print('A porcentagem de homens que responderam não é: {:.2f}'.format(
    porcentagemHomemNao), '%')
