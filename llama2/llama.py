from llama_cpp import Llama
# from flask import jsonify

def process(data, model):
    system_message = "You are a helpful assistant"
    user_message = data['user_message']
    max_tokens = int(data['max_tokens'])

    prompt = f"""<s>[INST] <<SYS>>
    {system_message}
    <</SYS>>
    {user_message} [/INST]"""
        
    # Run the model
    output = model(prompt, max_tokens=max_tokens, echo=True)
    return (output)