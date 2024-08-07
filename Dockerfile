# Use an stable Python runtime as a parent image
FROM python:3.12-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./server.py /app/server.py
COPY ./llama2/llama.py /app/llama2/llama.py
RUN wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf?download=true
RUN mv llama-2-7b-chat.Q2_K.gguf /app/llama2/models/llama-2-7b-chat.Q2_K.gguf

# Install the needed packages
RUN apt-get update && apt-get install build-essential -y
RUN apt-get install -y gcc g++ procps
RUN CMAKE_ARGS="-DLLAMA_OPENBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83
RUN pip install Flask
# Expose port 8080 outside of the container
EXPOSE 8080

# Run server.py when the container launches
CMD ["python", "server.py"]