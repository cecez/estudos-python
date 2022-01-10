def imprime_mensagem_inicial():
    print("** JOGO DA VELHA **")


def inicializa_tabuleiro():
    return {
        1: {1: '_', 2: '_', 3: '_'},
        2: {1: '_', 2: '_', 3: '_'},
        3: {1: '_', 2: '_', 3: '_'},
    }


def obtem_jogadores():
    # solicita nome dos jogadores
    nome_jogador_1 = input("Digite o nome do jogador 1 (símbolo 'o'):")
    nome_jogador_2 = input("Digite o nome do jogador 2 (símbolo 'x'):")
    return {'o': nome_jogador_1, 'x': nome_jogador_2}


def imprime_tabuleiro(tabuleiro):
    print("    1   2   3 ")
    print(" 1  {} | {} | {} ".format(tabuleiro[1][1], tabuleiro[1][2], tabuleiro[1][3]))
    print("   -----------")
    print(" 2  {} | {} | {} ".format(tabuleiro[2][1], tabuleiro[2][2], tabuleiro[2][3]))
    print("   -----------")
    print(" 3  {} | {} | {} ".format(tabuleiro[3][1], tabuleiro[3][2], tabuleiro[3][3]))


def alguem_ganhou(tabuleiro):
    if (tabuleiro[1][1] == tabuleiro[1][2] == tabuleiro[1][3]) and (tabuleiro[1][1] != '_'):
        return True
    elif (tabuleiro[2][1] == tabuleiro[2][2] == tabuleiro[2][3]) and (tabuleiro[2][1] != '_'):
        return True
    elif (tabuleiro[3][1] == tabuleiro[3][2] == tabuleiro[3][3]) and (tabuleiro[3][1] != '_'):
        return True
    elif (tabuleiro[1][1] == tabuleiro[2][1] == tabuleiro[3][1]) and (tabuleiro[1][1] != '_'):
        return True
    elif (tabuleiro[1][2] == tabuleiro[2][2] == tabuleiro[3][2]) and (tabuleiro[1][2] != '_'):
        return True
    elif (tabuleiro[1][3] == tabuleiro[2][3] == tabuleiro[3][3]) and (tabuleiro[1][3] != '_'):
        return True
    elif (tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3]) and (tabuleiro[1][1] != '_'):
        return True
    elif (tabuleiro[1][3] == tabuleiro[2][2] == tabuleiro[3][1]) and (tabuleiro[1][3] != '_'):
        return True


def marca_jogada(jogada, jogador_da_vez, tabuleiro):
    linha = int(jogada[0])
    coluna = int(jogada[1])
    tabuleiro[linha][coluna] = jogador_da_vez


def jogada_permitida(jogada, tabuleiro):
    linha = int(jogada[0])
    coluna = int(jogada[1])
    return tabuleiro[linha][coluna] == '_'


def jogar():
    # inicializações
    imprime_mensagem_inicial()
    jogadores = obtem_jogadores()
    jogador_da_vez = 'o'
    tabuleiro = inicializa_tabuleiro()
    jogadas = 0
    vencedor = False
    print(f"Que comecem os jogos! O duelo será {jogadores['o']} X {jogadores['x']}! Que tenham uma partida justa!")

    # loop principal do jogo
    while True:

        imprime_tabuleiro(tabuleiro)

        print("--- Sua vez {}".format(jogadores[jogador_da_vez]))
        jogada = input("Qual a linha da sua jogada?")
        jogada += input("Qual a coluna da sua jogada?")

        if not jogada_permitida(jogada, tabuleiro):
            print("Alguém já escolheu esta opção, tente novamente")
            continue

        marca_jogada(jogada, jogador_da_vez, tabuleiro)

        jogadas += 1

        # analisa critério de vitória
        if alguem_ganhou(tabuleiro):
            vencedor = True
            break

        # empate, não há mais jogadas disponíveis
        if jogadas == 9:
            break

        # alterna jogador do próximo turno
        if jogador_da_vez == 'o':
            jogador_da_vez = 'x'
        else:
            jogador_da_vez = 'o'

    # término
    print("----------------------------------")
    print("-------- RESULTADO FINAL ---------")
    print("----------------------------------")
    if vencedor:
        print("Temos um vencedor! Parabéns " + jogadores[jogador_da_vez] + "!")
    else:
        print(".... empate. nheh")
    print("----------------------------------")


if __name__ == "__main__":
    jogar()
