def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

entrada = input("Digite uma frase ou texto: ")
print(f"Quantidade de palavras: {contar_palavras(entrada)}")
