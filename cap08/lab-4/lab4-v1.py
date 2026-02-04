# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

import random

# Board (tabuleiro)
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
    def __init__(self, word_list):
        self.word = random.choice(word_list).lower()
        self.letters_guessed = set()
        self.wrong_guesses = 0
        self.max_wrong = len(board) - 1

    # Método para adivinhar a letra
    def guess(self, letter: str):
        letter = letter.lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            return False, "Digite apenas UMA letra."

        if letter in self.letters_guessed:
            return False, "Você já tentou essa letra."

        self.letters_guessed.add(letter)

        if letter not in self.word:
            self.wrong_guesses += 1
            return True, "Errou!"
        return True, "Acertou!"

    # Método para verificar se o jogo terminou
    def is_over(self):
        return self.wrong_guesses >= self.max_wrong or self.is_won()

    # Método para verificar se o jogador venceu
    def is_won(self):
        return all(ch in self.letters_guessed for ch in self.word)

    # Método para não mostrar a letra no board (mostrar _ no lugar)
    def masked_word(self):
        return " ".join(ch if ch in self.letters_guessed else "_" for ch in self.word)

    # Método para checar o status do game e imprimir o board na tela
    def display(self):
        print(board[self.wrong_guesses])
        print("\nPalavra:", self.masked_word())
        print("Tentativas:", " ".join(sorted(self.letters_guessed)))
        print(f"Erros: {self.wrong_guesses}/{self.max_wrong}")

# Exemplo de execução
if __name__ == "__main__":
    words = ["Python", "Data", "Science", "Programacao", "Forca", "Objeto"]
    game = Hangman(words)

    while not game.is_over():
        game.display()
        letter = input("\nDigite uma letra: ")
        ok, msg = game.guess(letter)
        print(msg)

    game.display()
    if game.is_won():
        print("\n🎉 Você venceu!")
    else:
        print(f"\n💀 Você perdeu! A palavra era: {game.word}")
