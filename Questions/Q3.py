'''
3. Faça um programa que receba a idade de oito pessoas, calcule e mostre:
a) a quantidade de pessoas em cada faixa etária;
b) a porcentagem de pessoas na primeira faixa etária
    com relação ao total de pessoas.
c) a porcentagem de pessoas na última faixa etária
    com relação ao total de pessoas

faiXa eTária idade
1 a Até 15 anos
2 a De 16 a 30 anos
3 a De 31 a 45 anos
4 a De 46 a 60 anos
5 a Acima de 60 anod

'''
faixa_15 = 0
faixa_30_60 = 0
faixa_31_45 = 0
faixa_46_60 = 0
faixa_60 = 0

for i in range(3):
    idade = int(input('Digite a idade: '))

    if idade <= 15:
        faixa_15 = faixa_15 + 1
    elif idade >= 16 and idade <= 30:
        faixa_30_60 = faixa_30_60 + 1
    elif idade >= 31 and idade <= 45:
        faixa_31_45 = faixa_31_45 + 1
    elif idade >= 46 and idade <= 60:
        faixa_46_60 = faixa_46_60 + 1
    else:
        faixa_60 = faixa_60 + 1

print('Quantidade de pessoas na faixa de 15 anos: ', faixa_15)
print('Quantidade de pessoas na faixa de 30 a 60 anos: ', faixa_30_60)
print('Quantidade de pessoas na faixa de 31 a 45 anos: ', faixa_31_45)
print('Quantidade de pessoas na faixa de 46 a 60 anos: ', faixa_46_60)
print('Quantidade de pessoas na faixa de 60 anos: ', faixa_60)
