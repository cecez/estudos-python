import random


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = gera_palavra_secreta(nome_arquivo="palavras.txt", linha_inicial=0)  # parâmetro nomeado (pode
    # ser usado em qualquer ordem)
    letras_acertadas = gera_lista_de_letras_acertadas(palavra_secreta)
    letras_erradas = set()

    enforcou = False
    acertou = False
    erros = 0
    total_de_erros_para_enforcar = 7

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
            print(f"Letra errada! Restam {total_de_erros_para_enforcar - erros} tentativas")
            desenha_forca(erros)

        enforcou = erros == total_de_erros_para_enforcar  # critério para enforcar, 6 erros
        acertou = "_" not in letras_acertadas  # critério para vencer, nenhuma letra para descobrir

    if enforcou:
        imprime_mensagem_derrota(palavra_secreta)
    elif acertou:
        imprime_mensagem_vitoria()

    print("**** Fim do jogo ****")


def imprime_mensagem_abertura():
    print("*********************************")
    print("** Bem-vindo ao jogo de forca! **")
    print("*********************************")


def gera_palavra_secreta(linha_inicial=0, nome_arquivo="palavras.txt"):  # parâmetros opcionais e nomeados
    # gerando lista de palavras secretas
    arquivo_de_palavras_secretas = open(nome_arquivo, "r")
    lista_de_palavras_secretas = []
    for possivel_palavra_secreta in arquivo_de_palavras_secretas:
        possivel_palavra_secreta = possivel_palavra_secreta.strip()  # remove caracteres de nova linha (\n)
        lista_de_palavras_secretas.append(possivel_palavra_secreta)
    arquivo_de_palavras_secretas.close()

    # escolhendo palavra aleatória
    indice_aleatorio = random.randrange(linha_inicial, len(lista_de_palavras_secretas))
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


def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# indica que script foi chamado/executado diretamente pela linha de comando
if __name__ == "__main__":
    jogar()
