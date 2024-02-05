import openai

key  = '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'

openai.api_key = key

def send_mensage(mensagem, mensage_list=[]):
    mensage_list.append(
        {'role': 'user', 'content':mensagem }
    )


    resposta = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = mensage_list,

    )

    return resposta["choices"][0]["message"]

mensage_list = []
while True:

    user_text = input('Escreva sua mensagem')

    if user_text == 'sair':
        print('Fico feliz em ajudá-lo, até mais ;)')
        break

    else:
        resposta = send_mensage(user_text)
        mensage_list.append(resposta)
        print('chatbot:', resposta['content'])


