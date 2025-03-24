def contarElementos(texto):
    #Definindo as listas de vogais e consoantes
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    #Definindo as variáveis de contagem
    quantidadeVogais = 0
    quantidadeConsoantes = 0
    quantidadeLetras = 0
    quantidadePalavras = 0

    #Contando palavras
    palavras = texto.split()
    quantidadePalavras = len(palavras)

    #Contando letras, vogais e consoantes
    for palavra in palavras:
        for letra in palavra:
            #Verifica se é uma letra
            if (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
                quantidadeLetras += 1
                if letra in vogais:
                    quantidadeVogais += 1
                elif letra in consoantes:
                    quantidadeConsoantes += 1

    print(f"Quantidade de vogais: {quantidadeVogais}")
    print(f"Quantidade de consoantes: {quantidadeConsoantes}")
    print(f"Quantidade total de letras: {quantidadeLetras}")
    print(f"Quantidade de palavras: {quantidadePalavras}")

#Entrada de dados
texto = input("Digite um texto: ")
#Saída de dados
contarElementos(texto)

    