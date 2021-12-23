import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("**     Bem-vindo aos jogos!    **")
    print("*********************************")

    print("Escolha seu jogo.")
    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Digite o número do jogo:"))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()