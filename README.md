# Company-Policy-AI-Chatbot
Built a Company Policy AI Chatbot using Python, Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Ollama Llama 3. It processes PDF policy documents, performs semantic search, and provides accurate, context-aware answers through a user-friendly interface.
# 📄 Company Policy AI Chatbot

An AI-powered chatbot that allows employees to ask questions about company policies in natural language. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded PDF documents and generates accurate responses using **Llama 3** through **Ollama**.

---

# 🚀 Features

* Upload company policy PDF documents
* Extract and process PDF content
* Split documents into semantic chunks
* Generate vector embeddings
* Store embeddings using FAISS
* Ask questions in natural language
* Retrieve relevant policy information
* Generate AI-powered answers
* Simple Streamlit web interface
* Runs completely on your local machine

---

# 🛠️ Technologies Used

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming Language |
| Streamlit             | Web Application      |
| LangChain             | LLM Framework        |
| Ollama                | Local LLM Runtime    |
| Llama 3               | Large Language Model |
| FAISS                 | Vector Database      |
| Sentence Transformers | Text Embeddings      |
| PyPDF                 | PDF Processing       |

---

# 📂 Project Structure

```
Company-Policy-Chatbot/
│
├── app.py
├── policy.pdf
├── requirements.txt
├── README.md
├── vectorstore/
│
└── screenshots/
    ├── home.png
    ├── upload.png
    └── chatbot.png
```

---


# 🖥️ How to Use

1. Launch the application.
2. Upload a company policy PDF.
3. Wait until embeddings are generated.
4. Ask questions related to company policies.
5. Receive AI-generated responses based on the uploaded document.

---

# 🧠 Project Workflow

```
               Company Policy PDF
                        │
                        ▼
                 PDF Loader (PyPDF)
                        │
                        ▼
                 Text Splitter
                        │
                        ▼
          Sentence Transformer Embeddings
                        │
                        ▼
               FAISS Vector Database
                        │
                        ▼
               User Question
                        │
                        ▼
          Similarity Search (Retriever)
                        │
                        ▼
        Relevant Document Chunks
                        │
                        ▼
             Llama 3 (Ollama)
                        │
                        ▼
             AI Generated Answer
                        │
                        ▼
              Streamlit Interface
```

---

# 🔍 Example Questions

* What is the company's leave policy?
* How many casual leaves are allowed?
* What are the working hours?
* Is work from home available?
* What is the employee code of conduct?
* What are the holiday policies?
* What is the notice period?
* What is the dress code policy?

---

# 🎯 Future Improvements

* Multiple PDF support
* Chat history
* Voice input
* Authentication and user login
* Cloud deployment
* Admin dashboard
* Multi-language support
* Conversation memory

---

# 📈 Skills Demonstrated

* Generative AI
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* LangChain
* Prompt Engineering
* Vector Databases
* Streamlit
* Python Development
* Document Question Answering
* AI Application Development

---

# 👨‍💻 Author

**Dadi Suneel**

Aspiring AI Engineer | Data Science & Generative AI Enthusiast

GitHub: https://github.com/Suneel098



## ⭐ If you found this project useful, please give it a Star on GitHub!
