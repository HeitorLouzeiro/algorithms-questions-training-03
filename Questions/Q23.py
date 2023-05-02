'''

Faça um programa que apresente o menu de opções a seguir,
que permita ao usuário escolher a opção
desejada, receba os dados necessários para executar a operação
e mostre o resultado. Verifique a possibilidade de opção inválida
e não se preocupe com as restrições como salário inválido.
Menu de opções:
1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair
Digite a opção desejada.

Na opção 1: receber o salário de um funcionário,
calcular e mostrar o novo salário usando as regras a seguir:
salários percenTagem de aumento
Até R$ 210,00 15%
De R$ 210,00 a R$ 600,00 (inclusive) 10%
Acima de R$ 600,00 5%

Na opção 2: receber o salário de um funcionário,
calcular e mostrar o valor de suas férias. Sabe-se que as
férias equivalem a seu salário acrescido de um terço do salário.

Na opção 3: receber o salário de um funcionário
e o número de meses de trabalho na empresa, no máximo
doze, calcular e mostrar o valor do décimo terceiro.
Sabe-se que o décimo terceiro equivale a seu salário
multiplicado pelo número de meses de trabalho dividido por 12.

Na opção 4: sair do programa.

'''
count = 1
space = '-' * 60

while count != 0:
    print('Menu de opções:')
    print('1. Novo salário')
    print('2. Férias')
    print('3. Décimo terceiro')
    print('4. Sair')
    opcao = int(input('selecione um as opçoes acima:'))
    print(space)
    if opcao == 1:
        salario = float(input('Digite o salario do funcionario:'))
        print(space)
        if salario <= 210:
            novoSalario = salario + (salario * 0.15)
            print('O novo salario do funcionario é:', novoSalario)
        elif salario > 210 and salario <= 600:
            novoSalario = salario + (salario * 0.10)
            print('O novo salario do funcionario é:', novoSalario)
        elif salario > 600:
            novoSalario = salario + (salario * 0.05)
            print('O novo salario do funcionario é:', novoSalario)
        print(space)
    elif opcao == 2:
        salario = float(input('Digite o salario do funcionario:'))
        ferias = salario + (salario * 0.33)
        print(space)
        print('O valor das ferias do funcionario é:', ferias)
    elif opcao == 3:
        salario = float(input('Digite o salario do funcionario:'))
        print(space)
        meses = int(input('Digite o numero de meses trabalhados:'))
        decimoTerceiro = (salario * meses) / 12
        print(space)
        print('O valor do decimo terceiro do funcionario é:', decimoTerceiro)
        print(space)
    elif opcao == 4:
        print('Obrigado por usar o programa!')
        print(space)
        count = 0
        break
    else:
        print('Opção invalida, tente novamente!')
        print(space)
