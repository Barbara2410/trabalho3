print("=== Cadastro de Livros da Biblioteca ===")

total_livros = 0
total_novos = 0
titulo_mais_antigo = ""
ano_mais_antigo = None

while True:
    titulo = input("Digite o título do livro: ")

    ano = input("Digite o ano de publicação: ")
    while not ano.isdigit() or int(ano) <= 0:
        print("Erro: o ano deve ser um número inteiro maior que zero.")
        ano = input("Digite novamente o ano de publicação: ")
    ano = int(ano)

    estado = input("Digite o estado do livro ('novo' ou 'usado'): ").lower()
    while estado not in ["novo", "usado"]:
        print("Erro: o estado deve ser 'novo' ou 'usado'.")
        estado = input("Digite novamente o estado do livro ('novo' ou 'usado'): ").lower()

    # Atualiza contadores
    total_livros += 1
    if estado == "novo":
        total_novos += 1

    if ano_mais_antigo is None or ano < ano_mais_antigo:
        ano_mais_antigo = ano
        titulo_mais_antigo = titulo

    continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
    if continuar != 's':
        break

# Exibição dos resultados
print("\n=== Relatório Final ===")
print(f"Total de livros cadastrados: {total_livros}")
print(f"Total de livros novos: {total_novos}")
if total_livros > 0:
    print(f"Livro mais antigo: '{titulo_mais_antigo}' (publicado em {ano_mais_antigo})")