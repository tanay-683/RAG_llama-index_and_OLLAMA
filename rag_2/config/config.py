from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


Settings.llm = Ollama(model="llama3.2:latest", request_timeout=100)
Settings.node_parser = SentenceSplitter(chunk_size=512)
Settings.embed_model = HuggingFaceEmbedding(
    model_name= "sentence-transformers/all-mpnet-base-v2"
)
