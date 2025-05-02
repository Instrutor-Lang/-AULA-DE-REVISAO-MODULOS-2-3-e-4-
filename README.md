🖥️ Sistema de Cadastro de Alunos com Python
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

A função input() coleta dados do usuário.

O uso de f-strings permite personalizar mensagens com variáveis.

🔁 Módulo 3: Lógica de Programação com Python
📌 Objetivos:
Utilizar laços de repetição e condições

Aplicar estruturas como while, if, elif, else

Praticar entrada de dados e decisões lógicas

📄 Trecho do código:
python

alunos = []

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
O laço while permite repetir instruções enquanto o usuário desejar.

O input() pode ser combinado com int() e float() para coletar números.

O comando break encerra o laço.

📄 Condicional para avaliar a nota:
python

if aluno["nota"] >= 7:
    status = "Aprovado"
elif aluno["nota"] >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"
As estruturas condicionais ajudam a tomar decisões com base nos dados do aluno.

📦 Módulo 4: Estruturas de Dados
📌 Objetivos:
Criar e manipular listas, dicionários e conjuntos

Organizar e analisar informações

📄 Lista de alunos:
python

alunos = []
Armazena todos os alunos cadastrados.

📄 Dicionário para armazenar um aluno:
python

aluno = {
    "nome": nome,
    "idade": idade,
    "nota": nota
}
Guarda os dados de cada aluno com chave-valor.

📄 Conjuntos para nomes únicos:
python

nomes = {aluno['nome'] for aluno in alunos}
print("\nAlunos únicos cadastrados:", nomes)
O set remove nomes duplicados automaticamente.

📊 Resultado Final:
Ao final da execução, o sistema apresenta:

Lista com nome, idade, nota e status (Aprovado, Recuperação ou Reprovado).

Lista única com os nomes dos alunos cadastrados.

🧠 Desafios para os Alunos:
Adicione um campo de curso para cada aluno.

Calcule a média geral das notas.

Conte quantos alunos foram aprovados.
