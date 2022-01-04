import random


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = gera_lista_de_letras_acertadas(palavra_secreta)
    letras_erradas = set()

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(f"Palavra secreta: {letras_acertadas}")
        print(f"Letras chutadas: {letras_erradas}")

        chute = pede_chute()

        if chute in letras_erradas:
            print("Você já realizou este chute. Tente novamente.")
            continue

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            marca_chute_incorreto(letras_erradas, chute)
            erros = erros + 1
            print(f"Letra errada! Restam {6 - erros} tentativas")

        enforcou = erros == 6  # critério para enforcar, 6 erros
        acertou = "_" not in letras_acertadas  # critério para vencer, nenhuma letra para descobrir

    if enforcou:
        imprime_mensagem_derrota()
    elif acertou:
        imprime_mensagem_vitoria()

    print("**** Fim do jogo ****")


def imprime_mensagem_abertura():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")


def gera_palavra_secreta():
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

    return palavra_secreta


def gera_lista_de_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    indice = 0
    for letra in palavra_secreta:
        if chute == letra.upper():  # comparando os dois caracteres em maiúsculo
            letras_acertadas[indice] = letra.upper()
        indice = indice + 1


def marca_chute_incorreto(letras_erradas, chute):
    letras_erradas.add(chute)


def imprime_mensagem_derrota():
    print("- Que pena, você foi enforcado")


def imprime_mensagem_vitoria():
    print("--- PARABÉNS, você venceu! --- ")


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
