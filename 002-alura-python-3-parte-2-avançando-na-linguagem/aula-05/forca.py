def jogar():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")

    palavra_secreta = "cama".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_erradas = set()

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(f"Palavra secreta: {letras_acertadas}")
        print(f"Letras chutadas: {letras_erradas}")

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in letras_erradas:
            print("Você já realizou este chute. Tente novamente.")
            continue

        if chute in palavra_secreta:
            indice = 0
            for letra in palavra_secreta:
                if chute == letra.upper():  # comparando os dois caracteres em maiúsculo
                    letras_acertadas[indice] = letra.upper()
                indice = indice + 1
        else:
            erros = erros + 1
            letras_erradas.add(chute)
            print(f"Letra errada! Restam {6 - erros} tentativas")

        enforcou = erros == 6 # critério para enforcar, 6 erros
        acertou = "_" not in letras_acertadas # critério para vencer, nenhuma letra para descobrir

    if enforcou:
        print("- Que pena, você foi enforcado")
    elif acertou:
        print("--- PARABÉNS, você venceu! --- ")

    print("**** Fim do jogo ****")


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
