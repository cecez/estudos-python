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
    return {1: nome_jogador_1, 2: nome_jogador_2}


def imprime_tabuleiro(tabuleiro):
    print("    1   2   3 ")
    print(" 1  {} | {} | {} ".format(tabuleiro[1][1], tabuleiro[1][2], tabuleiro[1][3]))
    print("   -----------")
    print(" 2  {} | {} | {} ".format(tabuleiro[2][1], tabuleiro[2][2], tabuleiro[2][3]))
    print("   -----------")
    print(" 3  {} | {} | {} ".format(tabuleiro[3][1], tabuleiro[3][2], tabuleiro[3][3]))


def jogar():
    # inicializações
    imprime_mensagem_inicial()
    jogadores = obtem_jogadores()
    jogador_da_vez = 1
    tabuleiro = inicializa_tabuleiro()
    turno = 0
    print(f'Que comecem os jogos! O duelo será {jogadores[1]} X {jogadores[2]}! Que tenham uma partida justa!')

    # loop principal do jogo
    while True:
        turno += 1

        # condição temporária para sair do loop
        if turno == 3:
            break

        imprime_tabuleiro(tabuleiro)
        jogada = input("{}, qual sua jogada? (ex: 1-2, linha 1 - coluna 2)".format(jogadores[jogador_da_vez]))

        # alterna jogador do próximo turno
        if jogador_da_vez == 1:
            jogador_da_vez = 2
        else:
            jogador_da_vez = 1

    # término


if __name__ == "__main__":
    jogar()
