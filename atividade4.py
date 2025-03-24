#criação de variáveis e entrada de dados.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
i = 1

#laço de repetição para encontrar o menor múltiplo comum.
while i <= num1 and i <= num2:
    i += 1
    if num1 % i == 0 and num2 % i == 0:
        print("O menor múltiplo comum de", num1, "e", num2, "é igual a", i)
        break
