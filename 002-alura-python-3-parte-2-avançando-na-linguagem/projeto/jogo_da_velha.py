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


def jogar():
    imprime_mensagem_inicial()
    jogadores = obtem_jogadores()
    print(f'Que comecem os jogos! O duelo será {jogadores[1]} X {jogadores[2]}! Que tenham uma partida justa!')
    tabuleiro = inicializa_tabuleiro()

    tabuleiro[1][3] = 'X'

    print(tabuleiro)


if __name__ == "__main__":
    jogar()
