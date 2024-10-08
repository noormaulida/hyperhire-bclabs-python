import panel as pn
from llms.llama2 import Llama2Client
from llms.mistral import MistralClient

pn.extension()
llms = {}
llm_options = pn.widgets.Select(name='Please choose LLM models', options={'Llama2': 'llama2', 'Mistral': 'mistral'})


async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    response = "Unknown response"
    if llm_options.value == "llama2": 
        if "llama2" not in llms:
            llms["llama2"] = Llama2Client()
        
        history = [message for message in instance.objects]
        prompt = llms["llama2"].generate_prompt(history[-1].object)
        output = llms["llama2"].model(prompt, max_tokens=2048)
        response = llms["llama2"].extract_response(output) + "\n\n<i>Generated by Llama2</i>"
        
        yield response

    if llm_options.value == "mistral":
        if "mistral" not in llms:
            llms["mistral"] = MistralClient()

        response = llms["mistral"].send_request(instance.objects[-1].object)
        
        message = ""
        for token in response:
            message += token
        
        yield message + "\n\n<i>Generated by Mistral</i>"
    
    
    
panel_interface = pn.chat.ChatInterface(
    callback=callback,
    callback_user="Chatbot",
)

panel_interface.send(
    llm_options, user="System", respond=False
)

panel_interface.servable()

