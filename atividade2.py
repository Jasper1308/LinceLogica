#Criação de vetores de 5 posições.
nums = [0] * 5
impares = [0] * 5
i = 0

#Entrada e processamento dos números, com verificação de paridade.
print("Digite os 5 números: ")
while i<5:
    nums[i] = int(input())
    if nums[i] % 2 == 0:
        impares[i] = nums[i]
    i += 1

#Saída de dados
print("Números impares: ")
for i in range(5):
    if impares[i] != 0:
        print(impares[i], end=" ")
