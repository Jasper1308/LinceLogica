#Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Condicional para verificar qual número é maior
if(num1 > num2):
    resultado = num1 / num2
else:    
    resultado = num2 / num1

#Saída de dados
print("O resultado da divisão é: ", resultado)