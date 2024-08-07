from flask import Flask, request, jsonify
from llama_cpp import Llama
from llama2.llama import process

# Create a Flask object
app = Flask("Llama server")
model = None

@app.route('/llama', methods=['POST'])
def generate_response():
    global model
    
    try:
        data = request.get_json()

        # Check if the required fields are present in the JSON data
        if 'user_message' in data and 'max_tokens' in data:
            if model is None:
                model_path = "llama2/models/llama-2-7b-chat.Q2_K.gguf"                
                model = Llama(model_path=model_path)
            
            return jsonify(process(data, model))

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)