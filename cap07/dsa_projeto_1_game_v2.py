import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[chances]

def pedir_tentativa(letras_tentativas):
    tentativa = input("\nDigite uma letra: ").strip().lower()

    if not tentativa:
        print("Digite alguma coisa.")
        return None

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas UMA letra (a-z).")
        return None

    if tentativa in letras_tentativas:
        print("Você já tentou essa letra. Escolha outra!")
        return None

    return tentativa

def aplicar_tentativa(palavra, tabuleiro, tentativa):
    acertou = False
    for i, letra in enumerate(palavra):
        if letra == tentativa:
            tabuleiro[i] = tentativa
            acertou = True
    return acertou

def venceu(tabuleiro):
    return "_" not in tabuleiro

def game():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)

    tabuleiro = ["_"] * len(palavra)
    chances = 6
    letras_tentativas = []

    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        tentativa = pedir_tentativa(letras_tentativas)
        if tentativa is None:
            continue

        letras_tentativas.append(tentativa)

        if aplicar_tentativa(palavra, tabuleiro, tentativa):
            print("Você acertou a letra!")
            if venceu(tabuleiro):
                print(f"\nVocê venceu! A palavra era: {palavra}")
                return
        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1

    print(f"\nVocê perdeu! A palavra era: {palavra}.")

if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")
