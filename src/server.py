import panel as pn
from llms.llama2 import init_llama2, generate_llama2_prompt
from llms.mistral import init_mistral, send_request_mistral

pn.extension()
llms = {}
llm_options = pn.widgets.Select(name='Please choose LLM models', options={'Llama2': 'llama2', 'Mistral': 'mistral'})


async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    response = "Unknown response"
    if llm_options.value == "mistral":
        if "mistral" not in llms:
            llms["mistral"] = init_mistral()

        history = [message for message in instance.objects]
        response = send_request_mistral(llms["mistral"], history[-1])
        
        message = ""
        for token in response:
            message += token
        
        yield message + "\n\n<i>Generated by Mistral</i>"
    
    if llm_options.value == "llama2": 
        if "llama2" not in llms:
            llms["llama2"] = init_llama2()
        
        history = [message for message in instance.objects]
        prompt = generate_llama2_prompt(history[-1])
        output = (llms["llama2"](prompt, max_tokens=2048))
        response = output["choices"][0]["text"] + "\n\n<i>Generated by Llama2</i>"
        
        yield response

    
panel_interface = pn.chat.ChatInterface(
    callback=callback,
    callback_user="Chatbot",
)

panel_interface.send(
    llm_options, user="System", respond=False
)

panel_interface.servable()

