# Módulo 2: Primeiros passos
print("Bem-vindo ao sistema de cadastro de alunos!")
nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}! Vamos começar.\n")

# Módulo 4: Estruturas de dados
alunos = []

# Módulo 3: Estrutura de repetição
while True:
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota (0 a 10): "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if  continuar!= 's':
        break

# Análise dos dados
print("\nResumo dos alunos cadastrados:\n")

for aluno in alunos:
    # Módulo 3: Condicional
    if aluno["nota"] >= 7:
        status = "Aprovado"
    elif aluno["nota"] >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"

    print(f"{aluno['nome']} ({aluno['idade']} anos) - Nota: {aluno['nota']} - {status}")

# Módulo 4: Conjuntos
nomes = {aluno['nome'] for aluno in alunos}
print("\nAlunos únicos cadastrados:", nomes)
