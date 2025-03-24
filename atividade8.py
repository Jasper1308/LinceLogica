#Definindo função calcularTabuada
def calcularTabuada(numero):
    #Laço de repetição para calcular a tabuada
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

#Entrada de dados
n = int(input("Digite um número : "))
#Saída de dados
calcularTabuada(n)