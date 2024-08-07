from llama_cpp import Llama

SYSTEM_INSTRUCTIONS = "You're a helpful assistant."

def init_llama2():
    model_path = "src/models/llama-2-7b-chat.Q2_K.gguf"                
    return Llama(model_path=model_path)


def generate_llama2_prompt(message):
    prompt = ""
    prompt = f"""<s>[INST] <<SYS>>
    {SYSTEM_INSTRUCTIONS}
    <</SYS>>
    {message} [/INST]"""
    
    return prompt

def extract_llama2_response(response):
    return response["choices"][0]["text"]
