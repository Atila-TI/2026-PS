# ================================================
# CONTROLE DE ESTOQUE - DESAFIO
# ================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 02 – Variáveis
# Autor      : [Atila do Nascimenta Pereira]
# Data       : [12/03/2026]
# Repositório: https://github.com/[Atila-TI]/2026-PS
# ================================================
#
# DESCRIÇÃO:
# Um programa para o controle de estoque, que deve de incio armazenar pelo menos 3 itens para conceito C, e exibir a situação do estoque de cada item.
# ================================================

# LISTA DE PRODUTOS
produtos = [
    {"nome": "Caneta", "quantidade": 2},
    {"nome": "Caderno", "quantidade": 10},
    {"nome": "Borracha", "quantidade": 15},
    {"nome": "Celulares, Tablets e Acessórios", "quantidade": 1},
    {"nome": "Computadores e Notebooks", "quantidade": 5},
    {"nome": "Mouses e Teclados", "quantidade": 12},
    {"nome": "Fones de Ouvido", "quantidade": 0},
    {"nome": "Impressoras e Suprimentos", "quantidade": 8},
    {"nome": "Monitores e Acessórios", "quantidade": 3},
    {"nome": "Componentes de Hardware", "quantidade": 20},
    {"nome": "Redes e Roteadores", "quantidade": 4}
]

print("=== SITUAÇÃO DO ESTOQUE ===")
print()

# Contadores para o relatório geral
critico = 0
adequado = 0
excesso = 0

# Laço For
for produto in produtos:
    nome = produto["nome"]
    qtd = produto["quantidade"]

    # Quantidade
    if qtd <= 2:
        situacao = "🔴 Crítico"
        critico += 1
    elif qtd <= 10:
        situacao = "🟡 Adequado"
        adequado += 1
    else:
        situacao = "🟢 Excesso"
        excesso += 1

    # Dados do produto
    print(f"Produto   : {nome}")
    print(f"Quantidade: {qtd}")
    print(f"Situação  : {situacao}")
    print("-" * 30)

# Relatório dos itens
print()
print("=== RESUMO ===")
print(f"Crítico : {critico}")
print(f"Adequado: {adequado}")
print(f"Excesso : {excesso}")

# Adição de produtos
print()
print("=== ADICIONAR PRODUTOS ===")
adicionar = "s"
while adicionar == "s":
    adicionar = input("Deseja adicionar um novo produto? (s/n): ").strip().lower()
    if adicionar != "s":
        break

    nome_novo = input("Nome do produto: ").strip()

    # Validação
    while True:
        entrada = input("Quantidade em estoque: ").strip()
        try:
            quantidade_nova = int(entrada)
            if quantidade_nova < 0:
                print("ERRO: A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("ERRO: Digite um número inteiro válido.")

    produtos.append({"nome": nome_novo, "quantidade": quantidade_nova})
    print(f"Produto '{nome_novo}' adicionado com sucesso!\n")

# Recalculando valorespara o relatório
critico = 0
adequado = 0
excesso = 0
for produto in produtos:
    qtd = produto["quantidade"]
    if qtd <= 2:
        critico += 1
    elif qtd <= 10:
        adequado += 1
    else:
        excesso += 1

print("=== RESUMO ATUALIZADO ===")
print(f"Crítico : {critico}")
print(f"Adequado: {adequado}")
print(f"Excesso : {excesso}")

# Consulta dos produtos pelo nome
consulta = "s"
while consulta == "s":
    consulta = input("\nDeseja consultar a condição de um produto? (s/n): ").strip().lower()
    if consulta != "s":
        break

    busca = input("Digite o nome do produto: ").strip()

    encontrado = None
    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            encontrado = produto
            break

    if encontrado:
        qtd = encontrado["quantidade"]
        if qtd <= 2:
            situacao = "🔴 Crítico"
        elif qtd <= 10:
            situacao = "🟡 Adequado"
        else:
            situacao = "🟢 Excesso"

        print(f"Produto   : {encontrado['nome']}")
        print(f"Quantidade: {qtd}")
        print(f"Situação  : {situacao}")
    else:
        print(f"Produto '{busca}' não está na lista.")

    print("-" * 30)

# Produto em menor quantidade
if produtos:
    mais_critico = min(produtos, key=lambda p: p["quantidade"])
    print()
    print("=== PRODUTO MAIS CRÍTICO ===")
    print(f"Produto   : {mais_critico['nome']}")
    print(f"Quantidade: {mais_critico['quantidade']}")
    print("(é o item com menor estoque)")
