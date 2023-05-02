'''

Faça um programa que receba dez números, calcule e
mostre a soma dos números pares e a soma dos
números primos.

'''

soma_pares = 0
soma_primos = 0

for i in range(10):
    numero = int(input('Digite um número: '))

    if (numero % 2 == 0):
        soma_pares = soma_pares + numero

    else:
        primo = True
        for j in range(2, numero):
            if (numero % j == 0):
                primo = False
                break

        if primo and numero > 1:
            soma_primos = soma_primos + numero

print('-' * 20)
print(f'Soma dos números pares: {soma_pares}')
print(f'Soma dos números primos: {soma_primos}')
