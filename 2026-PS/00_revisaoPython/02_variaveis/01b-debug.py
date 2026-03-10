# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do aluno: ")               # 1) OK (texto)
nota1 = float(input("Digite a nota 1 (0 a 10): "))     # 2) converte para float
nota2 = float(input("Digite a nota 2 (0 a 10): "))     # 3) converte para float

media = (nota1 + nota2) / 2                              # 4) adicionar parênteses para média correta

if media >= 6.0:
    situacao = "✅ Aprovado"
elif media >= 4.0:
    situacao = "⚠️ Recuperação"
else:
    situacao = "❌ Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")
