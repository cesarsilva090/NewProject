import random

def jogo_adivinhacao():
    numero = random.randint(1, 100)
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        tentativas += 1
        if palpite == numero:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

if __name__ == "__main__":
    jogo_adivinhacao()
