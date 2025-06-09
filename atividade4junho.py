print("=== Cadastro de Clientes e Compras ===")

total_clientes = 0
soma_gastos = 0
cliente_mais_gastou = ""
maior_gasto = 0

while True:
    nome = input("Digite o nome do cliente: ")

    valor = input("Digite o valor total gasto pelo cliente (em reais): ")
    while not valor.isdigit():
        print("Erro: o valor deve ser um número inteiro válido.")
        valor = input("Digite novamente o valor gasto: ")
    valor = int(valor)

    total_clientes += 1
    soma_gastos += valor

    if valor > maior_gasto:
        maior_gasto = valor
        cliente_mais_gastou = nome

    continuar = input("Deseja cadastrar outro cliente? (s/n): ").lower()
    if continuar != 's':
        break

# Exibição dos resultados
print("\n=== Relatório Final ===")
print(f"Total de clientes cadastrados: {total_clientes}")
print(f"Soma total dos valores gastos: R$ {soma_gastos}")
if total_clientes > 0:
    print(f"Cliente que mais gastou: {cliente_mais_gastou} (R$ {maior_gasto})")