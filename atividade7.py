#Definindo função calcularFatorial
def calcularFatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    else:
        return n * calcularFatorial(n-1)
    
#Entrada de dados
n = int(input("Digite um número : "))
#Saída de dados
print("O fatorial de", n, "é:", calcularFatorial(n))