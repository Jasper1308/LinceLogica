#Definindo a função calcularBhaskara que recebe três parâmetros a, b e c
def calcularBhaskara(a, b, c):
    #Calculando Delta
    delta = b**2 - 4*a*c
    #Condicional para verificar se a equação possui raízes reais
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        #Calculando a raiz
        x = -b / (2*a)
        return "A equação possui uma raiz real:", x
    else:
        #Calculando as raízes
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return "A equação possui duas raízes reais:", x1, x2

#Entrada de dados
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
print(calcularBhaskara(a, b, c))