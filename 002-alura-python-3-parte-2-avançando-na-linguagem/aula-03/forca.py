def jogar():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")

    palavra_secreta = "cama"
    letras_acertadas = ["_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(letras_acertadas)

        chute = input("Qual letra? ")
        chute = chute.strip()   # removendo espaços no início e fim da string

        indice = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():  # comparando os dois caracteres em maiúsculo
                letras_acertadas[indice] = letra.upper()
            indice = indice + 1

    print("**** Fim do jogo ****")


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
