'''
Faça um programa que leia cinco grupos de quatro valores (A, B, C, D)
e mostre-os na ordem lida. Em seguida,
organize-os em ordem crescente e decrescente.

'''
cont = 0
while cont < 2:
    cont += 1
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    d = int(input('Digite o valor de D: '))

    if a > b and a > c and a > d:
        if b > c and b > d:
            if c > d:
                print(f'Ordem crescente: {d}, {c}, {b}, {a}')
                print(f'Ordem decrescente: {a}, {b}, {c}, {d}')
    elif b > a and b > c and b > d:
        if a > c and a > d:
            if c > d:
                print(f'Ordem crescente: {d}, {c}, {a}, {b}')
                print(f'Ordem decrescente: {b}, {a}, {c}, {d}')
    elif c > a and c > b and c > d:
        if a > b and a > d:
            if b > d:
                print(f'Ordem crescente: {d}, {b}, {a}, {c}')
                print(f'Ordem decrescente: {c}, {a}, {b}, {d}')
    elif d > a and d > b and d > c:
        if a > b and a > c:
            if b > c:
                print(f'Ordem crescente: {c}, {b}, {a}, {d}')
                print(f'Ordem decrescente: {d}, {a}, {b}, {c}')
    else:
        print(f'Ordem crescente: {a}, {b}, {c}, {d}')
        print(f'Ordem decrescente: {d}, {c}, {b}, {a}')

    print(f'Os valores digitados foram: {a}, {b}, {c}, {d}')
    print('-' * 50)
