# =========================================================
# SISTEMA DE CÁLCULO DE IMC
# =========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Atila do Nascimento Pereira]
# Data       : [2026/03/14]
# Repositório: https://github.com/[Atila-TI]/2026-PS
# =========================================================
#
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parâmetros,
# retorno, escopo e recursão.
# =========================================================

# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""  # docstring: documentação da função
    print("=" * 40)
    print("     SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

# Chamando a função
exibir_cabecalho()

# ---- FUNÇÃO COM PARÂMETROS E COM RETORNO ----

def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso (kg) e altura (m)."""
    return peso / (altura ** 2)

# ---- FUNÇÃO COM PARÂMETROS E SEM RETORNO ----

def exibir_classificacao(imc):
    """Recebe o IMC e exibe a classificação correspondente."""
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

# ---- FUNÇÃO PRINCIPAL (main) ----

def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    print(f"IMC calculado: {imc:.2f}")
    exibir_classificacao(imc)


if __name__ == "__main__":
    main()

# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""
    
    imc = peso / (altura ** 2)  # ** é o operador de potência
    
    return imc  # devolve o resultado para quem chamou


# Coletando dados do usuário
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))


# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura)

print(f"Seu IMC é: {resultado:.2f}")

# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"  # variável GLOBAL — existe fora de qualquer função


def demonstrar_escopo():
    mensagem = "Olá do interior da função"  # variável LOCAL

    print("Dentro da função:")
    print(f"  mensagem = {mensagem}")  # OK: local existe aqui
    print(f"  versao   = {versao}")    # OK: global é visível dentro


demonstrar_escopo()

print("\nFora da função:")
print(f"  versao = {versao}")  # OK: global existe aqui
# print(mensagem)           # ERRO: local não existe aqui!

# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação e emoji de status.
    Parâmetro 'unidade' tem valor padrão — não é obrigatório informar.
    """

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"

    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"

    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"

    else:
        classificacao = "Obesidade"
        emoji = "🔴"

    return classificacao, emoji  # retorna dois valores — Python empacota como tupla


# Chamada sem o parâmetro opcional (usa o padrão "kg/m²")
imc_teste = 22.5
classificacao, emoji = classificar_imc(imc_teste)

print(f"IMC {imc_teste} ({classificacao}) {emoji}")


# Chamada informando o parâmetro opcional
classificacao, emoji = classificar_imc(imc_teste, unidade="lb/in²")

print(f"Mesma chamada com unidade customizada: {classificacao} {emoji}")

# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação e emoji de status.
    Parâmetro 'unidade' tem valor padrão — não é obrigatório informar."""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"

    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"

    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"

    else:
        classificacao = "Obesidade"
        emoji = "🔴"

    return classificacao, emoji   # retorna dois valores — Python empacota como tupla


# Chamada sem o parâmetro opcional (usa o padrão "kg/m²")
imc_teste = 22.5

classificacao, emoji = classificar_imc(imc_teste)

print(f"IMC {imc_teste} ({classificacao}) {emoji}")


# Chamada informando o parâmetro opcional
classificacao, emoji = classificar_imc(imc_teste, unidade="lb/in²")

print(f"Mesma chamada com unidade customizada: {classificacao} {emoji}")

# ---- RECURSÃO BÁSICA ----

def contagem_regressiva(n):
    """Exibe contagem regressiva de n até 0 usando recursão."""

    if n < 0:        # CASO BASE: para a recursão
        return

    print(n)
    contagem_regressiva(n - 1)   # CHAMADA RECURSIVA: resolve problema menor


print("\n--- Contagem regressiva ---")
contagem_regressiva(5)


# Fatorial: exemplo clássico de recursão com retorno
def fatorial(n):
    """Calcula n! recursivamente. Ex: 5! = 5 × 4 × 3 × 2 × 1 = 120"""

    if n == 0 or n == 1:   # caso base
        return 1

    return n * fatorial(n - 1)   # caso recursivo


print("\n--- Fatorial ---")
for i in range(1, 7):
    print(f" {i}! = {fatorial(i)}")

# ---- FUNÇÃO PRINCIPAL ----

def processar_pessoa():
    """Coleta dados, calcula IMC e exibe resultado completo."""

    nome   = input("\nNome: ")
    peso   = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)   # reutiliza funções já definidas
    classificacao, emoji = classificar_imc(imc)

    print("\n--- Resultado ---")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {classificacao} {emoji}")


# ---- EXECUÇÃO PRINCIPAL ----

exibir_cabecalho()

continuar = "s"

while continuar == "s":
    processar_pessoa()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()

exibir_rodape()


