def Leia():
    while True:
        try:
            n1 = int(input('Digite um número: '))
            break
        except ValueError:
            print('Número inválido! Digite um inteiro.')

    while True:
        try:
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Número inválido! Digite um inteiro.')

    op = input('Digite a operação [* / + -]:').strip()

    while op not in ('*', '/', '+', '-'):
        print('Essa operação é inválida!')
        op = input('Digite a operação [* / + -]:').strip()

    if op == '/' and n2 == 0:
        while True:
            try:
                n2 = int(input('Divisão por zero! Digite outro número (não zero): '))
                if n2 == 0:
                    print('O divisor não pode ser zero.')
                    continue
                break
            except ValueError:
                print('Número inválido! Digite um inteiro.')

    msg = f'{n1} {op} {n2}'

    if op == '+':
        res = Soma(n1, n2)
    elif op == '-':
        res = Subtração(n1, n2)
    elif op == '*':
        res = Multiplicação(n1, n2)
    elif op == '/':
        res = Divisão(n1, n2)
    Escreva(msg, res)

# Soma
def Soma(n1, n2):
    return(n1+n2)

# Subtração
def Subtração(n1, n2):
    return(n1-n2)

# Multiplicação
def Multiplicação(n1,n2):
    return(n1*n2)

# Divisão
def Divisão(n1,n2):
    return(n1/n2)

# Saida
def Escreva(msg, resultado):
    print(f'{msg} = {resultado}')

Leia()
