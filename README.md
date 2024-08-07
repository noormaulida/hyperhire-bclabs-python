# hyperhire-bclabs-python

Distributed LLM Assignment Python

## Dependencies

- Python 3.12

## Notes

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main

docker build -t server .
docker run -p 8080:8080 server

pip install panel transformers
pip install ctransformers

pip install nvidia-pyindex
pip install nvidia-cublas-cu11
pip install nvidia-cuda-runtime-cu11

pip uninstall ctransformers --yes
CT_METAL=1 pip install ctransformers --no-binary ctransformers
