from ctransformers import AutoConfig, AutoModelForCausalLM, Config

SYSTEM_INSTRUCTIONS = "You're a helpful assistant."
mystral_model_file = "mistral-7b-instruct-v0.1.Q2_K.gguf"

def init_mistral():
    config = AutoConfig(
        config=Config(
            temperature=0.9, max_new_tokens=2048, context_length=2048, gpu_layers=1
        ),
    )
    return AutoModelForCausalLM.from_pretrained(
        "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        model_file=mystral_model_file,
        config=config,
    )


def generate_mistral_prompt(history):
    history = [message for message in history if message.user != "System"]
    prompt = ""
    for i, message in enumerate(history):
        if i == 0:
            prompt += f"<s>[INST]{SYSTEM_INSTRUCTIONS} {message.object}[/INST]"
        else:
            if message.user == "Mistral":
                prompt += f"{message.object}</s>"
            else:
                prompt += f"""[INST]{message.object}[/INST]"""
    return prompt
