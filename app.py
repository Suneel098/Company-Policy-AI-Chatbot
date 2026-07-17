import streamlit as st
import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama

# Title in app
st.title("Company Policy Chatbot")
st.write("Ask questions about the company policy document.")

# Step 1: Load PDF
loader = PyPDFLoader("policy.pdf")
docs = loader.load()

# Step 2: Split PDF into small chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 4: Store embeddings in FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)

# Step 5: Load Ollama model
llm = ChatOllama(
    model="llama3",
    temperature=0
)

# Step 6: Create input box
query = st.text_input("Ask your question")

# Step 7: If user enters a question
if query:
    try:
        # Search relevant chunks from vector database
        result_docs = vectorstore.similarity_search(query, k=3)

        # Combine those chunks into one context
        context = "\n\n".join([doc.page_content for doc in result_docs])

        # Create final prompt
        prompt = f"""
You are a helpful assistant for answering questions from a company policy document.

Use only the context below to answer the question.
If the answer is not present in the context, say:
I could not find that in the policy document.

Context:
{context}

Question:
{query}

Answer:
"""

        # Send prompt to LLM
        response = llm.invoke(prompt)

        # Display answer
        st.write("### Answer")
        st.write(response.content)

    except Exception as e:
        st.error(f"Error: {e}")