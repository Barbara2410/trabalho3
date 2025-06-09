# Inicialização das variáveis
soma_notas = 0
total_alunos = 0
maior_nota = -1
aluno_maior_nota = ""

while True:
    nome = input("Digite o nome do aluno: ")
    
    nota_input = input("Digite a nota final do aluno (apenas números inteiros): ")
    while not nota_input.isdigit():
        print("Nota inválida! Por favor, digite um número inteiro.")
        nota_input = input("Digite a nota final do aluno (apenas números inteiros): ")
    
    nota = int(nota_input)
    
    # Atualiza soma, total e maior nota
    soma_notas += nota
    total_alunos += 1

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = nome

    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro aluno? (s para sim, qualquer outra tecla para não): ")
    if continuar.lower() != 's':
        break

# Calcula média
if total_alunos > 0:
    media = soma_notas / total_alunos
    print("\nCadastro finalizado.")
    print(f"Total de alunos cadastrados: {total_alunos}")
    print(f"Média da turma: {media:.2f}")
    print(f"Aluno com a maior nota: {aluno_maior_nota} (Nota: {maior_nota})")
else:
    print("Nenhum aluno foi cadastrado.")
