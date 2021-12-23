import random


def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontuacao = 1000

    print("Níveis de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite o número do nível escolhido:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range(1, total_de_tentativas + 1):
        print("-- Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute_str = input("- Digite um número entre 1 e 100:")
        chute = int(chute_str)

        if (chute < 1):
            print("- Número inválido. Digite um número acima de 1.")
            continue
        elif (chute > 100):
            print("- Número inválido. Digite um número abaixo de 100.")
            continue

        print("- Você digitou", chute)

        chute_certo = (chute == numero_secreto)
        chute_maior = (chute > numero_secreto)
        chute_menor = (chute < numero_secreto)

        if (chute_certo):
            print("- Parabéns, certa resposta!")
            print(f"- Você fez {pontuacao} pontos.")
            break  # sai do laço for
        else:
            if (chute_maior):
                print("- ERROU! Seu chute foi maior que o número secreto.")
            elif (chute_menor):
                print("- ERROU! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

    print(f"**** Número secreto: {numero_secreto} ****")
    print("**** Fim do jogo ****")

# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()