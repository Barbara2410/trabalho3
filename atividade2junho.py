print("=== Controle de Veículos da Garagem ===")

total_dias = 0
total_veiculos = 0
modelo_mais_tempo = ""
maior_tempo = 0

while True:
    modelo = input("Digite o modelo do veículo: ")

    dias = input("Digite o número de dias que o veículo ficará estacionado: ")
    while not dias.isdigit():
        print("Erro: o número de dias deve ser um número inteiro válido.")
        dias = input("Digite novamente o número de dias: ")
    
    dias = int(dias)
    total_dias += dias
    total_veiculos += 1

    if dias > maior_tempo:
        maior_tempo = dias
        modelo_mais_tempo = modelo

    continuar = input("Deseja cadastrar outro veículo? (s/n): ").lower()
    if continuar != 's':
        break

# Cálculo da média
media_dias = total_dias / total_veiculos if total_veiculos > 0 else 0

# Saída final
print("\n=== Relatório Final ===")
print(f"Total de veículos cadastrados: {total_veiculos}")
print(f"Soma total de dias: {total_dias}")
print(f"Média de dias na garagem: {media_dias:.2f}")
print(f"Veículo que ficará mais tempo: {modelo_mais_tempo} ({maior_tempo} dias)")
