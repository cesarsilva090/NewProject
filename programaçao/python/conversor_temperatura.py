# conversor_temperatura.py

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def menu():
    print("\nConversor de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        c = float(input("Digite a temperatura em Celsius: "))
        print(f"{c}°C = {celsius_para_fahrenheit(c)}°F")
    elif escolha == '2':
        c = float(input("Digite a temperatura em Celsius: "))
        print(f"{c}°C = {celsius_para_kelvin(c)}K")
    elif escolha == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
