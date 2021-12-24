def jogar():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")

    palavra_secreta = "abacaxi"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print("--- simulando jogo ---")

        chute = input("Qual letra? ")

        indice = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra '{letra}' na posição {indice}")
            indice = indice + 1

    print("**** Fim do jogo ****")


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
