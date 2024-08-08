from mistralai import Mistral


class MistralClient:    
    def __init__(self):
        self.model_type = "mistral-large-latest"
        self.api_key = "ULUoH7kuftwlI2XfMgXajhh6CwkjZ2JX"
        self.model = Mistral(api_key=self.api_key)


    def send_request(self, message):
        messages = [
            {
                "role": "user",
                "content": message,
            },
        ]
        
        chat_response = self.model.chat.complete(
        model=self.model_type,
        messages=messages,
        )
        return chat_response.choices[0].message.content
