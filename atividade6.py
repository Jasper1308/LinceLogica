#Definindo função calcularHipotenusa que recebe dois parâmetros cateto1 e cateto2
def calcularHipotenusa(cateto1, cateto2):
    #Calculando a hipotenusa
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

#Entrada de dados
cateto1 = int(input("Digite o valor do primeiro cateto: "))
cateto2 = int(input("Digite o valor do segundo cateto: "))
#Saída de dados
print("O valor da hipotenusa é:", calcularHipotenusa(cateto1, cateto2))
    