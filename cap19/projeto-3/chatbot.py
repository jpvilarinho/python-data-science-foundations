# Data Science Academy - www.datascienceacademy.com.br
# Projeto 3 - Construindo Chatbot Personalizado com GPT e Linguagem Python

import os
from openai import OpenAI


def gera_texto(client: OpenAI, mensagem: str) -> str:
    """
    Gera resposta a partir de um modelo de chat.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um chatbot útil e educado. Responda em português do Brasil."},
            {"role": "user", "content": mensagem},
        ],
        max_tokens=200,
        temperature=0.8,
    )

    content = response.choices[0].message.content
    return (content or "").strip()


def main():
    print("\nBem vindo ao Chatbot do Projeto 3 do Curso Gratuito da Data Science Academy!")
    print("www.datascienceacademy.com.br")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\nERRO: variável de ambiente OPENAI_API_KEY não encontrada.")
        print("Defina a variável e tente novamente.")
        return

    client = OpenAI(api_key=api_key)

    while True:
        user_message = input("\nVocê: ").strip()

        if user_message.lower() == "sair":
            break

        if not user_message:
            print("Chatbot: Digite uma mensagem.")
            continue

        try:
            chatbot_response = gera_texto(client, user_message)
            print(f"\nChatbot: {chatbot_response}")
        except Exception as e:
            print("\nChatbot: Ocorreu um erro ao chamar a API.")
            print("Detalhes:", e)


if __name__ == "__main__":
    main()
