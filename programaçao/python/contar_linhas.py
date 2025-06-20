def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return 0

arquivo = input("Digite o nome do arquivo texto: ")
print(f"O arquivo tem {contar_linhas(arquivo)} linhas.")
