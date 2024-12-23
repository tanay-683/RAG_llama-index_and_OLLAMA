from llama_index.core import VectorStoreIndex
from rag_2.config.config import *
from rag_2.llm.llm import document_loader
from pathlib import Path
import logging

path = Path("./data/")
documents = document_loader(path=path)
logging.info("Documents loaded")
index = VectorStoreIndex.from_documents(
    documents, embed_model = Settings.embed_model
)
logging.info("stored embedding into local memory")

query_engine = index.as_query_engine(llm=Settings.llm)

logging.info("starting the query engine")
query = "What is an attention mechanism?"
logging.info(f"Query: {query}")
response = query_engine.query(query)

logging.info(response.response)
print(response.response)