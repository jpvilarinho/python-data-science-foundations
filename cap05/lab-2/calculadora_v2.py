# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


print("\n1 - Soma, \n2 - Subtração, \n3 - Multiplicação, \n4 - Divisão\n")
opc = int(input('Digite a operação desejada: '))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if opc == 1:
    print(f'{n1} + {n2} é igual a {soma(n1, n2)}')
elif opc == 2:
    print(f'{n1} - {n2} é igual a {sub(n1, n2)}')
elif opc == 3:
    print(f'{n1} x {n2} é igual a {mult(n1, n2)}')
elif opc == 4:
    print(f'{n1} / {n2} é igual a {div(n1, n2)}')
else:
    print('Opção inválida, tente novamente!')