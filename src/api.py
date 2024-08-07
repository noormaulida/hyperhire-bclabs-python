from flask import Flask, request, jsonify
from middleware import PrefixMiddleware
from llms.llama2 import init_llama2, generate_llama2_prompt, extract_llama2_response
from llms.mistral import init_mistral, send_request_mistral


# Create a Flask object
app = Flask("Distributed LLM API Server")
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api/v1')

@app.route('/llms', methods=['POST'])
def process_llm_response():
    selected_model = request.json['selected_model']
    question = request.json['question']
    
    try:
        if selected_model == "llama2" or selected_model == "mistral":
            if selected_model == "llama2":
                model = init_llama2()
                prompt = generate_llama2_prompt(question)
                output = model(prompt, max_tokens=2048)
                response = extract_llama2_response(output)
            else:
                model = init_mistral()
                output = send_request_mistral(model, question)
                response = ""
                for token in output:
                    response += token
            
            return jsonify({"status": "OK", "selected_model": selected_model, "question": question, "response": response}), 200

        else:
            return jsonify({"error": "LLM model not found"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

@app.route('/llms', methods=['GET'])
def check_server_status():
    return jsonify({"status": "Server API is up"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)