import random


def jogar():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")

    # gerando lista de palavras secretas
    arquivo_de_palavras_secretas = open("palavras.txt", "r")
    lista_de_palavras_secretas = []
    for possivel_palavra_secreta in arquivo_de_palavras_secretas:
        possivel_palavra_secreta = possivel_palavra_secreta.strip()  # remove caracteres de nova linha (\n)
        lista_de_palavras_secretas.append(possivel_palavra_secreta)
    arquivo_de_palavras_secretas.close()

    # escolhendo palavra aleatória
    indice_aleatorio = random.randrange(0, len(lista_de_palavras_secretas))
    palavra_secreta = lista_de_palavras_secretas[indice_aleatorio]
    palavra_secreta = palavra_secreta.upper()

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

        enforcou = erros == 6  # critério para enforcar, 6 erros
        acertou = "_" not in letras_acertadas  # critério para vencer, nenhuma letra para descobrir

    if enforcou:
        print("- Que pena, você foi enforcado")
    elif acertou:
        print("--- PARABÉNS, você venceu! --- ")

    print("**** Fim do jogo ****")


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
