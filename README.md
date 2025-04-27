# Rag pipline using LLAMA-INDEX and OLLAMA

steps to run this project in your local environment:
1. clone the repo
2. build the docker file
```bash
docker build -t <image_name> .
```

3. run the built docker image
```bash 
docker run -it --rm <image_name>
```

### Disclaimer
in `main.py` file, the query is hardcoded, so every time you run the docker image, it will run the same query.