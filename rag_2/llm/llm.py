from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import PromptTemplate
from pathlib import Path

def document_loader(path:Path):
# loading the documents
    documents = SimpleDirectoryReader(path).load_data() 
    return documents

system_prompt = """<|SYSTEM|># You are a Q&A Assistant. You are given a question and a context. You have to find the answer to the question in the context."""

query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")




