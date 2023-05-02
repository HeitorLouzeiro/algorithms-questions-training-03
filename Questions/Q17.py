'''

Foi feita uma pesquisa sobre a audiência de canal de TV
em várias casas de uma cidade,em determinado dia.
Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12)
e o número de pessoas que estavam assistindo àquele canal.
Se a televisão estivesse desligada, nada era anotado, ou seja, essa casa
não entrava na pesquisa. Faça um programa que:
leia um número indeterminado de dados (número do canal
e número de pessoas que estavam assistindo);
e calcule e mostre a porcentagem de audiência de cada canal.
Para encerrar a entrada de dados, digite o número do canal ZERO.

'''
cont = 1
canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
totalPessoas = 0

while cont > 0:
    canal = int(input('Digite o número do canal: '))
    if canal == 0:
        print('Programa encerrado!')
        print('-' * 50)
        cont = 0
        break
    else:
        pessoas = int(input('Digite o número de pessoas assistindo: '))
        if canal == 4:
            canal4 = canal4 + pessoas
        elif canal == 5:
            canal5 = canal5 + pessoas
        elif canal == 7:
            canal7 = canal7 + pessoas
        elif canal == 12:
            canal12 = canal12 + pessoas
        else:
            print('Canal inválido')
    totalPessoas = totalPessoas + pessoas

    print('Canal 4: ', (canal4/totalPessoas)*100, '%')
    print('Canal 5: ', (canal5/totalPessoas)*100, '%')
    print('Canal 7: ', (canal7/totalPessoas)*100, '%')
    print('Canal 12: ', (canal12/totalPessoas)*100, '%')
