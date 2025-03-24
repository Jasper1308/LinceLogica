nums = [0] * 5
impares = [0] * 5
i = 0
print("Digite os 5 números: ")
while i<5:
    nums[i] = int(input())
    if nums[i] % 2 == 0:
        impares[i] = nums[i]
    i += 1

print("Números impares: ", end="")
for i in range(5):
    if impares[i] != 0:
        print(impares[i], end=" ")
