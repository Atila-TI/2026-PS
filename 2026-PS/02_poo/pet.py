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

class Pet:
    '''Classe que representa um pet hospedado em um hotel para animais.'''

    def __init__(self, nome, especie, idade, nome_dono, peso, vacinado):
        # Atributos básicos do pet
        self.nome = nome
        self.especie = especie
        self.idade = idade

        # Atributo de controle de estado de hospedagem
        self.hospedado = False

        # Novos atributos adicionados como parte da atividade
        self.nome_dono = nome_dono
        self.peso = peso
        self.vacinado = vacinado

    def exibir_dados(self):
        '''Exibe os principais dados do pet.'''
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Nome do Dono: {self.nome_dono}")
        print(f"Peso: {self.peso} kg")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}\n")

    def registrar_entrada(self):
        '''Valida se o pet não está hospedado antes de registrar a entrada.'''
        if not self.hospedado:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel com sucesso.")
        else:
            print(f"Erro: {self.nome} já está hospedado e não pode entrar novamente.")

    def registrar_saida(self):
        '''Valida se o pet está hospedado antes de registrar a saída.'''
        if self.hospedado:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel com sucesso.")
        else:
            print(f"Erro: {self.nome} não está hospedado e não pode sair.")

    def calcular_diaria(self):
        '''Retorna o valor da diária de acordo com a idade do pet.'''
        if self.idade <= 3:
            return 50.00
        elif 4 <= self.idade <= 10:
            return 60.00
        else:
            return 75.00

    def verificar_vacinacao(self):
        '''Mostra se a vacinação do pet está em dia.'''
        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: vacinação pendente.")

    def atualizar_peso(self, novo_peso):
        '''Atualiza o peso do pet e informa o valor atualizado.'''
        self.peso = novo_peso
        print(f"Peso atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        '''Exibe um resumo completo do pet, incluindo o valor da diária.'''
        resumo = (
            f"Resumo do Pet:\n"
            f"- Nome: {self.nome}\n"
            f"- Espécie: {self.especie}\n"
            f"- Idade: {self.idade}\n"
            f"- Nome do Dono: {self.nome_dono}\n"
            f"- Peso: {self.peso} kg\n"
            f"- Vacinado: {'Sim' if self.vacinado else 'Não'}\n"
            f"- Hospedado: {'Sim' if self.hospedado else 'Não'}\n"
            f"- Diária: R$ {self.calcular_diaria():.2f}\n"
        )
        print(resumo)


# ===========================================================================
# TESTES DA CLASSE
# ===========================================================================
# Os testes a seguir criam três pets e chamam os métodos principais.
# Use este bloco para validar o comportamento do código.
# ===========================================================================
if __name__ == '__main__':
    pet1 = Pet("Rex", "Cachorro", 5, "João", 20.5, True)
    pet2 = Pet("Cupcake", "Dragão", 500, "Maria", 1000.75, False)
    pet3 = Pet("Luna", "Tigre", 2, "Ana", 2.1, True)

    pet1.exibir_dados()
    pet1.registrar_entrada()
    pet1.exibir_dados()
    pet1.emitir_resumo()

    pet2.exibir_dados()
    pet2.registrar_entrada()
    pet2.exibir_dados()
    pet2.emitir_resumo()

    pet3.exibir_dados()
    pet3.registrar_entrada()
    pet3.exibir_dados()
    pet3.emitir_resumo()