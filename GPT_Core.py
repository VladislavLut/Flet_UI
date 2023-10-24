import openai

api_key = "token"

def send_request(message):
    openai.api_Key = api_key
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", message=[{"role": "user", "content": message}])
    return chat_completion.choices[0].message['content']