Sistema de Cadastro de Alunos com Python
👨‍🏫 Módulo 2: Primeiros Passos com Python
📌 Objetivos:
Compreender como utilizar print() e input()

Trabalhar com variáveis e tipos de dados básicos

📄 Trecho do código:
python

print("Bem-vindo ao sistema de cadastro de alunos!")
nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}! Vamos começar.\n")
✅ O que aprendemos:
A função print() exibe mensagens na tela.

A função input() coleta dados digitados pelo usuário.

O uso de f-strings permite criar mensagens personalizadas com variáveis.

🔁 Módulo 3: Lógica de Programação com Python
📌 Objetivos:
Utilizar laços de repetição e condições

Aplicar estruturas como while, if, elif, else

Praticar a entrada de dados e decisões lógicas

📄 Trecho do código:
python

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
    if continuar != 's':
        break
✅ O que aprendemos:
O laço while permite repetir instruções até que uma condição pare.

O input() pode ser combinado com int() e float() para ler números.

O break encerra o laço quando o usuário deseja parar.

📄 Condicional:
python

if aluno["nota"] >= 7:
    status = "Aprovado"
elif aluno["nota"] >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"
As estruturas condicionais ajudam a tomar decisões com base nos dados dos alunos.

📦 Módulo 4: Estruturas de Dados
📌 Objetivos:
Criar e manipular listas, dicionários e conjuntos

Organizar e analisar informações

📄 Lista de alunos:

Edit
alunos = []
Usamos uma lista para armazenar vários alunos.

📄 Dicionário de aluno:
python

aluno = {
    "nome": nome,
    "idade": idade,
    "nota": nota
}
O dicionário guarda os dados de cada aluno com chave e valor.

📄 Conjuntos:

Edit
nomes = {aluno['nome'] for aluno in alunos}
print("\nAlunos únicos cadastrados:", nomes)
O conjunto (set) elimina nomes repetidos e mostra apenas alunos únicos.

📊 Resultado final:
Ao final da execução, o programa apresenta:

Lista de alunos com nome, idade, nota e status (Aprovado, Recuperação ou Reprovado)

Lista única com os nomes cadastrados

🧠 Desafio para os alunos:
Adicione um campo para o curso do aluno.

Calcule a média geral das notas.

Conte quantos alunos foram aprovados.

