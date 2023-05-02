'''

Foi feita uma pesquisa entre os habitantes de uma região.
Foram coletados os dados de idade, sexo (M/F)
e salário. Faça um programa que calcule e mostre:
a média dos salários do grupo;
a maior e a menor idade do grupo;
a quantidade de mulheres com salário até R$ 200,00;
a idade e o sexo da pessoa que possui o menor salário.
Finalize a entrada de dados ao ser digitada uma idade negativa.

'''

cont = 1

qtdPessoas = 0
mediaSalarios = float(0)

maiorIdade = 0
menorIdade = 999

qtdSalarioMAte200 = 0
menorSalario = float(999999)

idadeMenorSalario = 0
sexoMenorSalario = ''

while cont > 0:
    idade = int(input('Digite a idade: '))
    if idade < 0:
        cont = 0
        break
    else:
        sexo = input('Digite o sexo: ').upper()
        salario = float(input('Digite o salário: '))

        mediaSalarios = mediaSalarios + salario

        if idade > maiorIdade:
            maiorIdade = idade

        if idade < menorIdade:
            menorIdade = idade

        if sexo == 'F' and salario <= 200:
            qtdSalarioMAte200 = qtdSalarioMAte200 + 1

        if salario < menorSalario:
            menorSalario = salario
            idadeMenorSalario = idade
            sexoMenorSalario = sexo

        qtdPessoas = qtdPessoas + 1

        print('Média dos salários: ', mediaSalarios/qtdPessoas)
        print('Maior idade: ', maiorIdade)
        print('Menor idade: ', menorIdade)
        print('Quantidade de mulheres com salário até R$ 200,00: ',
              qtdSalarioMAte200)
        print('Idade e sexo da pessoa que possui o menor salário: ',
              idadeMenorSalario, sexoMenorSalario)
