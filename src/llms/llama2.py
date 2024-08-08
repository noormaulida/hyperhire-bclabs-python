from llama_cpp import Llama

class Llama2Client:    
    def __init__(self):
        self.model_path = "src/models/llama-2-7b-chat.Q2_K.gguf"                
        self.system_instructions = "You're a helpful assistant."
        self.model = Llama(model_path=(self.model_path))

    def generate_prompt(self, message):
        prompt = ""
        prompt = f"""<s>[INST] <<SYS>>
        {(self.system_instructions)}
        <</SYS>>
        {message} [/INST]"""
        return prompt

    def extract_response(self, response):
        return response["choices"][0]["text"]
