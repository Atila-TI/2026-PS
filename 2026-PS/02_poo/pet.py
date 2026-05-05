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
# SEÇÃO DE TESTES
# ===========================================================================
# Este bloco testa a classe Pet criando 3 pets diferentes e executando
# os métodos principais para validar se o código funciona corretamente.
# "if __name__ == '__main__'" significa que este código só roda se o
# arquivo for executado diretamente (não quando importado em outro arquivo).
# ===========================================================================

if __name__ == '__main__':
    # CRIANDO 3 OBJETOS (instâncias) DA CLASSE PET
    pet1 = Pet("Rex", "Cachorro", 5, "João", 20.5, True)
    pet2 = Pet("Cupcake", "Dragão", 500, "Guto", 100000.75, False)
    pet3 = Pet("Luna", "Cerberus", 100000, "Satãn", 1000.55, True)

    # === TESTANDO PET 1 ===
    pet1.exibir_dados()  # Mostra dados iniciais
    pet1.registrar_entrada()  # Registra chegada
    pet1.exibir_dados()  # Mostra dados após entrada
    pet1.emitir_resumo()  # Mostra resumo completo
    pet1.atualizar_peso(22.0)  # Atualiza o peso do pet1

    # === TESTANDO PET 2 ===
    pet2.exibir_dados()  # Mostra dados iniciais
    pet2.registrar_entrada()  # Registra chegada
    pet2.exibir_dados()  # Mostra dados após entrada
    pet2.emitir_resumo()  # Mostra resumo completo
    pet2.atualizar_peso(12000.0)  # Atualiza o peso do pet2

    # === TESTANDO PET 3 ===
    pet3.exibir_dados()  # Mostra dados iniciais
    pet3.registrar_entrada()  # Registra chegada
    pet3.exibir_dados()  # Mostra dados após entrada
    pet3.emitir_resumo()  # Mostra resumo completo
    pet3.atualizar_peso(1100.0)  # Atualiza o peso do pet3