'''
===========================================================================
# ARQUIVO   : pet.py
# Disciplina: Programação de Sistemas (2026-2)
# Aula      : Aula 20 - Por que POO?
# Autor     : [Atila do Nascimento Pereira]
# Conceitos : Classes, objeto, atributos, métodos, encapsulamento
# Atividade : Classe Pet
===========================================================================
'''

import os
import pickle
import time

# CLASSE: Representa um pet (animal de estimação) em um hotel para animais
class Pet:
    '''Classe que representa um pet hospedado em um hotel para animais.'''

    # MÉTODO CONSTRUTOR: Inicializa um novo pet com suas características
    # Este método é chamado automaticamente quando criamos um novo objeto
    def __init__(self, nome, especie, idade, nome_dono, peso, vacinado):
        
        # Atributos básicos do pet (informações principais)
        self.nome = nome  # O nome do animal
        self.especie = especie  # Tipo do animal (cachorro, gato, etc)
        self.idade = idade  # Idade em anos

        # Atributo de controle de estado (acompanha se está hospedado)
        self.hospedado = False  # Começa sempre como NOT hospedado (False)

        # Novos atributos adicionados como parte da atividade
        self.nome_dono = nome_dono  # Quem é o dono do pet
        self.peso = peso  # Peso em quilogramas
        self.vacinado = vacinado  # Se está vacinado ou não (True/False)

    # MÉTODO: Exibe todos os dados do pet de forma organizada e legível
    def exibir_dados(self):
        '''Exibe os principais dados do pet.'''
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Nome do Dono: {self.nome_dono}")
        print(f"Peso: {self.peso} kg")
        # Ternário: Se vacinado=True mostra "Sim", senão mostra "Não"
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        # Ternário: Se hospedado=True mostra "Sim", senão mostra "Não"
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}\n")

    # MÉTODO: Registra a chegada de um pet ao hotel
    # Só deixa entrar se o pet ainda não está hospedado
    def registrar_entrada(self):
        '''Valida se o pet não está hospedado antes de registrar a entrada.'''
        # Se o pet NÃO está hospedado (not self.hospedado = True)
        if not self.hospedado:
            self.hospedado = True  # Marca como hospedado
            print(f"{self.nome} entrou no hotel com sucesso.")
        else:
            # Se já estava hospedado, mostra mensagem de erro
            print(f"Erro: {self.nome} já está hospedado e não pode entrar novamente.")

    # MÉTODO: Registra a saída de um pet do hotel
    # Só deixa sair se o pet realmente está hospedado
    def registrar_saida(self):
        '''Valida se o pet está hospedado antes de registrar a saída.'''
        # Se o pet ESTÁ hospedado (self.hospedado = True)
        if self.hospedado:
            self.hospedado = False  # Marca como NÃO hospedado
            print(f"{self.nome} saiu do hotel com sucesso.")
        else:
            # Se não estava hospedado, mostra mensagem de erro
            print(f"Erro: {self.nome} não está hospedado e não pode sair.")

    # MÉTODO: Calcula o valor da diária baseado na idade do pet
    # Pets mais velhos pagam mais (critério de preço)
    def calcular_diaria(self):
        '''Retorna o valor da diária de acordo com a idade do pet.'''
        if self.idade <= 400:  # Filhotes até 400 anos
            return 100.00
        elif 401 <= self.idade <= 800:  # Pets adultos de 401 a 800 anos
            return 120.00
        else:  # Pets idosos acima de 800 anos
            return 150.00

    # MÉTODO: Verifica e mostra o status de vacinação do pet
    def verificar_vacinacao(self):
        '''Mostra se a vacinação do pet está em dia.'''
        if self.vacinado:  # Se vacinado = True
            print("Vacinação em dia.")
        else:  # Se vacinado = False
            print("Atenção: vacinação pendente.")

    # MÉTODO: Atualiza o peso do pet (recebe um novo valor como parâmetro)
    def atualizar_peso(self, novo_peso):
        '''Atualiza o peso do pet e informa o valor atualizado.'''
        self.peso = novo_peso  # Assign novo valor ao atributo peso
        print(f"Peso atualizado para {self.peso} kg.")

    # MÉTODO: Exibe um resumo COMPLETO do pet (todas as informações em uma visualização)
    # Este método usa outro método (calcular_diaria) dentro dele
    def emitir_resumo(self):
        '''Exibe um resumo completo do pet, incluindo o valor da diária.'''
        # Cria uma string com todas as informações formatadas
        resumo = (
            f"Resumo do Pet:\n"
            f"- Nome: {self.nome}\n"
            f"- Espécie: {self.especie}\n"
            f"- Idade: {self.idade}\n"
            f"- Nome do Dono: {self.nome_dono}\n"
            f"- Peso: {self.peso} kg\n"
            f"- Vacinado: {'Sim' if self.vacinado else 'Não'}\n"
            f"- Hospedado: {'Sim' if self.hospedado else 'Não'}\n"
            f"- Diária: R$ {self.calcular_diaria():.2f}\n"  # Chama calcular_diaria() para obter o valor
        )
        print(resumo)  # Exibe o resumo


# ===========================================================================
# FUNÇÕES AUXILIARES DE ARQUIVOS E MENU
# ===========================================================================

DATA_FILE = os.path.join(os.path.dirname(__file__), 'pets.bin')


def carregar_pets(arquivo):
    '''Carrega a lista de pets de um arquivo binário pickle, se existir.'''
    if not os.path.exists(arquivo):
        return []

    try:
        with open(arquivo, 'rb') as arquivo_bin:
            registros = pickle.load(arquivo_bin)
    except (EOFError, pickle.UnpicklingError, AttributeError):
        print('Arquivo de dados corrompido ou inválido. Iniciando lista vazia.')
        return []

    pets = []
    for registro in registros:
        try:
            hospedado = registro.pop('hospedado', False)
            pet = Pet(**registro)
            pet.hospedado = hospedado
            pets.append(pet)
        except TypeError:
            continue
    return pets


def salvar_pets(pets, arquivo):
    '''Salva a lista de pets em um arquivo binário usando pickle.'''
    registros = [
        {
            'nome': pet.nome,
            'especie': pet.especie,
            'idade': pet.idade,
            'nome_dono': pet.nome_dono,
            'peso': pet.peso,
            'vacinado': pet.vacinado,
            'hospedado': pet.hospedado,
        }
        for pet in pets
    ]

    with open(arquivo, 'wb') as arquivo_bin:
        pickle.dump(registros, arquivo_bin)

    print(f"\nDados salvos em '{arquivo}'.")


def cadastrar_pet(pets):
    '''Lê os dados de um pet via input e adiciona à lista.'''
    print('\n=== Cadastrar Novo Pet ===')
    nome = input('Nome: ').strip()
    especie = input('Espécie: ').strip()

    while True:
        idade_texto = input('Idade (anos): ').strip()
        if idade_texto.isdigit():
            idade = int(idade_texto)
            break
        print('Por favor, informe um número inteiro válido para a idade.')

    nome_dono = input('Nome do dono: ').strip()

    while True:
        peso_texto = input('Peso (kg): ').strip().replace(',', '.')
        try:
            peso = float(peso_texto)
            break
        except ValueError:
            print('Por favor, informe um número válido para o peso.')

    while True:
        resposta = input('Vacinado? [s/n]: ').strip().lower()
        if resposta in ('s', 'sim', 'y', 'yes'):
            vacinado = True
            break
        if resposta in ('n', 'nao', 'não', 'no'):
            vacinado = False
            break
        print('Responda apenas com "s" ou "n".')

    pet = Pet(nome, especie, idade, nome_dono, peso, vacinado)
    pets.append(pet)
    print(f"\nPet '{nome}' cadastrado com sucesso.")
    time.sleep(1)


def escolher_pet(pets, acao):
    '''Retorna um pet escolhido pelo usuário ou None se inválido.'''
    if not pets:
        print('\nNenhum pet cadastrado.')
        return None

    listar_pets(pets)
    while True:
        escolha = input(f'Número do pet para {acao} (ou ENTER para cancelar): ').strip()
        if escolha == '':
            return None
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(pets):
                return pets[indice]
        print('Escolha inválida. Digite um número válido ou ENTER para cancelar.')


def check_in(pets):
    pet = escolher_pet(pets, 'check-in')
    if pet is not None:
        pet.registrar_entrada()
        time.sleep(0.8)


def check_out(pets):
    pet = escolher_pet(pets, 'check-out')
    if pet is not None:
        pet.registrar_saida()
        time.sleep(0.8)


def atualizar_peso_pet(pets):
    pet = escolher_pet(pets, 'atualizar peso')
    if pet is None:
        return

    while True:
        peso_texto = input(f'Novo peso para {pet.nome} (kg): ').strip().replace(',', '.')
        try:
            novo_peso = float(peso_texto)
            pet.atualizar_peso(novo_peso)
            time.sleep(0.8)
            break
        except ValueError:
            print('Por favor, informe um número válido para o peso.')


def buscar_pet_por_nome(pets):
    '''Busca pets por nome parcial e mostra os que combinam.'''
    if not pets:
        print('\nNenhum pet cadastrado.')
        return

    busca = input('\nDigite o nome (parcial) do pet: ').strip().lower()
    if not busca:
        print('Busca cancelada.')
        return

    resultados = [pet for pet in pets if busca in pet.nome.lower()]

    if not resultados:
        print(f'Nenhum pet encontrado com o nome "{busca}".')
        return

    print(f'\n=== Resultados da Busca por "{busca}" ===')
    for indice, pet in enumerate(resultados, start=1):
        print(f'\nPet {indice}:')
        pet.exibir_dados()


def relatorio_hospedados(pets):
    '''Lista pets hospedados (hospedado=True) e mostra o total da diária.'''
    hospedados = [pet for pet in pets if pet.hospedado]

    if not hospedados:
        print('\nNenhum pet hospedado no momento.')
        return

    print('\n=== Relatório de Pets Hospedados ===')
    total_diaria = 0.0

    for indice, pet in enumerate(hospedados, start=1):
        print(f'\nPet {indice}:')
        pet.exibir_dados()
        diaria = pet.calcular_diaria()
        total_diaria += diaria

    print(f'\n--- Total da Diária do Dia ---')
    print(f'Total: R$ {total_diaria:.2f}')
    time.sleep(1)


def resumo_individual(pets):
    '''Exibe o resumo individual de um pet escolhido (usa emitir_resumo()).'''
    pet = escolher_pet(pets, 'resumo individual')
    if pet is not None:
        pet.emitir_resumo()
        time.sleep(1)


def salvar_em_txt(pets, arquivo):
    '''Salva a lista de pets em formato texto (.txt).'''
    arquivo_txt = arquivo.replace('.bin', '.txt')
    try:
        with open(arquivo_txt, 'w', encoding='utf-8') as f:
            f.write('=== LISTA DE PETS DO HOTEL ===\n\n')
            for indice, pet in enumerate(pets, start=1):
                f.write(f'Pet {indice}:\n')
                f.write(f'Nome: {pet.nome}\n')
                f.write(f'Espécie: {pet.especie}\n')
                f.write(f'Idade: {pet.idade}\n')
                f.write(f'Dono: {pet.nome_dono}\n')
                f.write(f'Peso: {pet.peso} kg\n')
                f.write(f'Vacinado: {"Sim" if pet.vacinado else "Não"}\n')
                f.write(f'Hospedado: {"Sim" if pet.hospedado else "Não"}\n')
                f.write(f'Diária: R$ {pet.calcular_diaria():.2f}\n')
                f.write('-' * 40 + '\n\n')
        print(f"Dados salvos em '{arquivo_txt}'.")
        time.sleep(0.8)
    except IOError as e:
        print(f'Erro ao salvar em TXT: {e}')


def salvar_ambos_formatos(pets, arquivo_bin):
    '''Salva os dados em ambos os formatos: binário (pickle) e texto (.txt).'''
    salvar_pets(pets, arquivo_bin)
    salvar_em_txt(pets, arquivo_bin)


def listar_pets(pets):
    '''Chama exibir_dados() para cada pet cadastrado.'''
    if not pets:
        print('\nNenhum pet cadastrado.')
        return

    print('\n=== Lista de Pets ===')
    for indice, pet in enumerate(pets, start=1):
        print(f'\nPet {indice}:')
        pet.exibir_dados()


def exibir_menu():
    '''Mostra as opções do menu principal.'''
    print('\n=== Menu do Hotel de Pets ===')
    print('1 - Cadastrar pet')
    print('2 - Listar pets')
    print('3 - Check-in pet')
    print('4 - Check-out pet')
    print('5 - Atualizar peso')
    print('6 - Buscar pet por nome')
    print('7 - Relatório de pets hospedados')
    print('8 - Resumo individual de pet')
    print('9 - Sair')


def main():
    pets = carregar_pets(DATA_FILE)
    if pets:
        print(f'Foram carregados {len(pets)} pet(s) do arquivo.')
    else:
        print('Nenhum arquivo de pets encontrado. Iniciando lista vazia.')

    try:
        while True:
            exibir_menu()
            opcao = input('Escolha uma opção: ').strip()
            if opcao == '1':
                cadastrar_pet(pets)
            elif opcao == '2':
                listar_pets(pets)
            elif opcao == '3':
                check_in(pets)
            elif opcao == '4':
                check_out(pets)
            elif opcao == '5':
                atualizar_peso_pet(pets)
            elif opcao == '6':
                buscar_pet_por_nome(pets)
            elif opcao == '7':
                relatorio_hospedados(pets)
            elif opcao == '8':
                resumo_individual(pets)
            elif opcao == '9':
                salvar_ambos_formatos(pets, DATA_FILE)
                print('Encerrando o programa. Até logo!')
                break
            else:
                print('Opção inválida. Digite de 1 a 9.')
    except KeyboardInterrupt:
        print('\nInterrupção detectada. Salvando antes de sair...')
        salvar_ambos_formatos(pets, DATA_FILE)


if __name__ == '__main__':
    main()