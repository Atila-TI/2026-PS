# =========================================================
# SISTEMA DE BIBLIOTECA - DESAFIO
# =========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : [Atila do Nascimento Pereira]
# Data       : [12/03/2026]
# Repositório: https://github.com/[Atila-TI]/2026-PS
# =========================================================
#
# DESCRIÇÃO:
# Catálogo que permite a vizualização de livros, cadastro de novos livros e consulta por título.
# =========================================================

# Catálogo inicial com pelo menos 3 livros
catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": True},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "disponivel": False},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": True},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "disponivel": True},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967, "disponivel": False},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "disponivel": False},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997, "disponivel": True},
    {"titulo": "O Código Da Vinci", "autor": "Dan Brown", "ano": 2003, "disponivel": True},
    {"titulo": "A Menina que Roubava Livros", "autor": "Markus Zusak", "ano": 2005, "disponivel": False},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "disponivel": True},
    {"titulo": "O Morro dos Ventos Uivantes", "autor": "Emily Brontë", "ano": 1847, "disponivel": True}, 
    {"titulo": "Star Wars: O Despertar da Força", "autor": "Alan Dean Foster", "ano": 2015, "disponivel": False},
    {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "ano": 1979, "disponivel": True}
]

# Exibiçao de Livros

def exibir_livro(livro):
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f"Título : {livro['titulo']}")
    print(f"Autor  : {livro['autor']}")
    print(f"Ano    : {livro['ano']}")
    print(f"Status : {status}")
    print("-" * 40)


# Catálogo de Itens
print("=== CATÁLOGO DE LIVROS ===")
print()
for livro in catalogo:
    exibir_livro(livro)

# Contagem de disponíveis e emprestados
disponiveis = sum(1 for livro in catalogo if livro["disponivel"])
emprestados = len(catalogo) - disponiveis
print("=== RESUMO DE DISPONIBILIDADE ===")
print(f"Disponíveis : {disponiveis}")
print(f"Emprestados: {emprestados}")
print()

# Cadastro de novos livros
resposta = input("Deseja cadastrar um novo livro? (s/n): ").strip().lower()
if resposta == "s":
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    # Validação do ano
    ano_texto = input("Ano: ").strip()
    if ano_texto.isdigit():
        ano = int(ano_texto)
    else:
        ano = 0
        print("Ano inválido; O livro e armazenará como 0.")

    # Adição de livro ao catálogo (usa a mesma chave "ano" dos livros iniciais)
    novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True}
    catalogo.append(novo_livro)

    # Exibição de catálogo atualizado
    print()
    print("=== CATÁLOGO ATUALIZADO ===")
    print()
    for livro in catalogo:
        exibir_livro(livro)

# Busca pelo autor
busca_autor = "s"
while busca_autor == "s":
    busca_autor = input("Deseja buscar livros por autor? (s/n): ").strip().lower()
    if busca_autor != "s":
        break

    termo = input("Digite o nome (ou parte) do autor: ").strip().lower()
    encontrados = [livro for livro in catalogo if termo in livro["autor"].lower()]

    if encontrados:
        print(f"\nLivros encontrados para autor '{termo}':")
        for livro in encontrados:
            exibir_livro(livro)
    else:
        print(f"\nNenhum livro encontrado para autor '{termo}'.")

# Registro de empréstimo/devolução
operacao = "s"
while operacao == "s":
    operacao = input("\nDeseja registrar um empréstimo/devolução? (s/n): ").strip().lower()
    if operacao != "s":
        break

    titulo_busca = input("Digite o título do livro: ").strip().lower()

    livro_encontrado = None
    for livro in catalogo:
        if livro["titulo"].lower() == titulo_busca:
            livro_encontrado = livro
            break

    if livro_encontrado:
        # Alterna entre disponível e emprestado
        livro_encontrado["disponivel"] = not livro_encontrado["disponivel"]
        status = "Disponível" if livro_encontrado["disponivel"] else "Emprestado"
        acao = "Disponibilizado" if livro_encontrado["disponivel"] else "Emprestado"
        print(f"Livro '{livro_encontrado['titulo']}' {acao} com sucesso. Status: {status}.")
    else:
        print(f"Livro '{titulo_busca}' não encontrado no catálogo.")

# Relatório final
print("\n=== RELATÓRIO FINAL ===")
print(f"Total de livros  : {len(catalogo)}")
disponiveis = sum(1 for livro in catalogo if livro["disponivel"])
emprestados = len(catalogo) - disponiveis
print(f"Disponíveis      : {disponiveis}")
print(f"Emprestados      : {emprestados}")

if emprestados > 0:
    print("\nLivros atualmente emprestados:")
    for livro in catalogo:
        if not livro["disponivel"]:
            print(f"- {livro['titulo']}")
