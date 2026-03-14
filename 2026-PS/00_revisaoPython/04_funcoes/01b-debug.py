def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem

print(saudacao("Ana"))
print(saudacao("Bruno", "tarde"))


def dobrar(x):
    return x * 2

print("Dobro de 5:", dobrar(5))


total = 0

def incrementar():
    global total
    total = total + 1

incrementar()
print("Total:", total)


def contagem(n):
    if n < 0:
        return
    print(n)
    contagem(n - 1)

contagem(3)