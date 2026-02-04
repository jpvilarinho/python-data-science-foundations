# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

import random
from os import system, name


# Função para limpar a tela
def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# Board (tabuleiro) - usando raw strings para evitar warnings com "\"
board = [
r'''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', 
r'''

+---+
|   |
O   |
    |
    |
    |
=========''', 
r'''

+---+
|   |
O   |
|   |
    |
    |
=========''', 
r'''

+---+
|   |
O   |
/|  |
    |
    |
=========''', 
r'''

+---+
|   |
O   |
/|\ |
    |
    |
=========''', 
r'''

+---+
|   |
O   |
/|\ |
/   |
    |
=========''', 
r'''

+---+
|   |
O   |
/|\ |
/ \ |
    |
========='''
]


class Hangman:
    def __init__(self, palavra: str):
        self.palavra = palavra.lower().strip()
        self.letras_erradas: list[str] = []
        self.letras_escolhidas: list[str] = []
        self.max_erros = len(board) - 1  # 6

    # Método para adivinhar a letra
    def guess(self, letra: str) -> bool:
        letra = letra.lower().strip()

        # validação básica
        if len(letra) != 1 or not letra.isalpha():
            return False

        # não penaliza repetidas
        if letra in self.letras_escolhidas or letra in self.letras_erradas:
            return False

        if letra in self.palavra:
            self.letras_escolhidas.append(letra)
            return True

        self.letras_erradas.append(letra)
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self) -> bool:
        return self.hangman_won() or (len(self.letras_erradas) >= self.max_erros)

    # Método para verificar se o jogador venceu
    def hangman_won(self) -> bool:
        return "_" not in self.hide_palavra()

    # Método para não mostrar a letra no board
    def hide_palavra(self) -> str:
        return "".join(letra if letra in self.letras_escolhidas else "_" for letra in self.palavra)

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        erros = len(self.letras_erradas)

        print(board[erros])
        print("\nPalavra: " + " ".join(self.hide_palavra()))
        print(f"\nErros: {erros}/{self.max_erros}")

        print("\nLetras erradas: " + (" ".join(self.letras_erradas) if self.letras_erradas else "-"))
        print("Letras corretas: " + (" ".join(self.letras_escolhidas) if self.letras_escolhidas else "-"))
        print()


# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra() -> str:
    palavras = ["banana", "abacate", "uva", "morango", "laranja"]
    return random.choice(palavras)


def main():
    limpa_tela()

    game = Hangman(rand_palavra())

    while not game.hangman_over():
        game.print_game_status()

        user_input = input("Digite uma letra: ")
        ok = game.guess(user_input)

        if not ok:
            print("Entrada inválida ou letra repetida. Digite apenas 1 letra nova (a-z).")

        # opcional: limpar a tela a cada rodada
        # input("\nPressione Enter para continuar...")
        # limpa_tela()

    game.print_game_status()

    if game.hangman_won():
        print("\nParabéns! Você venceu!! 🎉")
    else:
        print("\nGame over! Você perdeu. 💀")
        print("A palavra era: " + game.palavra)

    print("\nFoi bom jogar com você! Agora vá estudar!\n")


if __name__ == "__main__":
    main()
