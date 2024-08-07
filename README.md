# hyperhire-bclabs-python

Distributed LLM Assignment Python

## Dependencies

- Python 3.12

## Notes

docker build -t hyperhire-bclabs-python .
docker run -p 8080:8080 hyperhire-bclabs-python

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main

docker build -t server .
docker run -p 5000:5000 server
