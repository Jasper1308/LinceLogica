#criando variáveis para receber os valores digitados pelo usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#criando variável para armazenar o resultado da subtração
resultado = num1 - num2

#verificando se o resultado é negativo, se for, multiplicamos por -1 para torná-lo positivo
if resultado < 0:
    resultado = resultado * -1  

#saída de dados
print("O valor absoluto é: ", resultado)