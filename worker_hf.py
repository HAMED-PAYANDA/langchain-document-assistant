import os
import torch
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFaceEmbeddings,
    ChatHuggingFace,
)

# Check for GPU availability
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Global variables
conversation_retrieval_chain = None
chat_history = []
llm_hub = None
embeddings = None

# Initialize the language model and embeddings
def init_llm():
    global llm_hub, embeddings

    logger.info("Initializing Hugging Face LLM and embeddings...")

    # Replace with your actual token when testing locally/in Cloud IDE
    # Force the exact token
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR_HUGGING_FACE_TOKEN_HERE"

    # Initialize base LLM endpoint
    base_llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        temperature=0.1,
        max_new_tokens=600,
    )

    # Wrap the base LLM with ChatHuggingFace
    llm_hub = ChatHuggingFace(llm=base_llm)

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": DEVICE},
    )
    logger.debug("Hugging Face LLM and Embeddings initialized.")

# Process a PDF document
def process_document(document_path):
    global conversation_retrieval_chain

    logger.info("Loading document from path: %s", document_path)
    loader = PyPDFLoader(document_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=64
    )
    texts = text_splitter.split_documents(documents)

    db = Chroma.from_documents(texts, embedding=embeddings)

    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
        input_key="question",
    )
    logger.info("RetrievalQA chain created successfully.")

# Process a user prompt
def process_prompt(prompt):
    global conversation_retrieval_chain, chat_history

    logger.info("Processing prompt: %s", prompt)
    output = conversation_retrieval_chain.invoke(
        {"question": prompt, "chat_history": chat_history}
    )
    answer = output["result"]

    chat_history.append((prompt, answer))
    logger.debug("Chat history updated. Total exchanges: %d", len(chat_history))
    return answer.strip()

# Initialize LLM and embeddings
init_llm()
logger.info("Hugging Face LLM initialization complete.")


