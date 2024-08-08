from flask import Flask, request, jsonify
from middleware import PrefixMiddleware
from llms.llama2 import Llama2Client
from llms.mistral import MistralClient


# Create a Flask object
app = Flask("Distributed LLM API Server")
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api/v1')

@app.route('/llms', methods=['POST'])
def process_llm_response():
    selected_model = request.json['model']
    questions = request.json['questions']
    
    try:
        if selected_model == "llama2" or selected_model == "mistral":
            results = []
            if selected_model == "llama2":
                client = Llama2Client()
                for question in questions:    
                    prompt = client.generate_prompt(question)
                    output = client.model(prompt, max_tokens=2048)
                    response = client.extract_response(output)
                    results.append({'question':question, 'answer':response})
            else:
                client = MistralClient()
                for question in questions:    
                    output = client.send_request(question)
                    response = ""
                    for token in output:
                        response += token
                    results.append({'question':question, 'answer':response})
            
            return jsonify({"status": "OK", "model": selected_model, "results": results}), 200

        else:
            return jsonify({"error": "LLM model not found"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

@app.route('/llms', methods=['GET'])
def check_server_status():
    return jsonify({"status": "Server API is up"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)