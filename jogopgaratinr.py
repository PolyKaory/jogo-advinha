import random

def jogo_advinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de advinhação")
    print("Estou pensando em um número entre 1 a 100.")

    while True: 
        try: 
            palpite = int(input("Digite seu palpite:"))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo!")
            elif palpite > numero_secreto:
                print("Muito alto!")
            else: 
                print(f"Parabéns! Você advinhou o número em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_advinhacao()