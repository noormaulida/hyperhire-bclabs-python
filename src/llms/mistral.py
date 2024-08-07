from mistralai import Mistral

SYSTEM_INSTRUCTIONS = "You're a helpful assistant."
model = "mistral-large-latest"
api_key = "ULUoH7kuftwlI2XfMgXajhh6CwkjZ2JX"


def init_mistral():
    return Mistral(api_key=api_key)


def send_request_mistral(client, message):
    messages = [
        {
            "role": "user",
            "content": message,
        },
    ]
    
    chat_response = client.chat.complete(
       model=model,
       messages=messages,
    )
    return chat_response.choices[0].message.content
