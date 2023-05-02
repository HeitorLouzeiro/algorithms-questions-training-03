'''

Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
1, 2, 3, 4 Votos para os respectivos candidatos
5 Voto nulo
6 Voto em branco
Faça um programa que calcule e mostre:
o total de votos para cada candidato;
o total de votos nulos;
o total de votos em branco;
a porcentagem de votos nulos sobre o total de votos; e
a porcentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos, tem-se o valor zero e,
para códigos inválidos, o programa deverá
mostrar uma mensagem.

'''

count = 1

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0

space = '-' * 50
while count != 0:
    print('1 - Candidato 1')
    print('2 - Candidato 2')
    print('3 - Candidato 3')
    print('4 - Candidato 4')
    print('5 - Voto nulo')
    print('6 - Voto em branco')
    print('0 - Fim da votação')
    print(space)

    voto = int(input('Digite o código do candidato: '))
    print(space)
    if voto == 0:
        print('Fim da votação.')
        print(space)
        count = 0
        break
    else:
        if voto == 1:
            cand1 = cand1 + 1
        elif voto == 2:
            cand2 = cand2 + 1
        elif voto == 3:
            cand3 = cand3 + 1
        elif voto == 4:
            cand4 = cand4 + 1
        elif voto == 5:
            nulo = nulo + 1
        elif voto == 6:
            branco = branco + 1
        else:
            print('Voto inválido.')
            print(space)
        total = cand1 + cand2 + cand3 + cand4 + nulo + branco
        porcentagem_nulo = (nulo / total) * 100
        porcentagem_branco = (branco / total) * 100
print(f'Total de votos para o candidato 1: {cand1}')
print(f'Total de votos para o candidato 2: {cand2}')
print(f'Total de votos para o candidato 3: {cand3}')
print(f'Total de votos para o candidato 4: {cand4}')
print(f'Total de votos nulos: {nulo}')
print(f'Total de votos em branco: {branco}')
print(f'Porcentagem de votos nulos: {porcentagem_nulo:.2f}%')
print(f'Porcentagem de votos em branco: {porcentagem_branco:.2f}%')
