inicial= int(input("Digite o número inicial:"))
final= int(input("Digite o número final:"))
print ("*" * 30)

for numeros in range(inicial, final + 1):
        print(numeros)
        
if (final < inicial):   
    print ("Por favor, digite os números na ordem correta.")

