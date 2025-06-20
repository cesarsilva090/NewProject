def calculadora():
    print("Calculadora simples")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    if op == '+':
        print(f"Resultado: {a + b}")
    elif op == '-':
        print(f"Resultado: {a - b}")
    elif op == '*':
        print(f"Resultado: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Erro: divisão por zero")
    else:
        print("Operação inválida")

if __name__ == "__main__":
    calculadora()
