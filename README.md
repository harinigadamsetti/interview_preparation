# 🎓 Interview Preparation Assistant Using Basic RAG and LLM

## 📌 Project Overview

The **Interview Preparation Assistant** is an AI-powered web application designed to help students and job seekers prepare for technical and HR interviews.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a manually created knowledge base and generates responses using the Groq API and Large Language Model.

It provides an interactive platform where users can practise interview questions, understand technical concepts, evaluate their answers, and improve their interview preparation.

## ✨ Features

- **Technical Interview Questions:** Practise technical questions related to programming, Python, Machine Learning, SQL, and other subjects.
- **HR Interview Questions:** Prepare for commonly asked HR interview questions.
- **Topic Explanation:** Get simple and clear explanations of technical topics.
- **Answer Evaluation:** Submit answers and receive feedback, identify mistakes, and get improved answers.
- **Mock Interview:** Practise interview-related questions and responses.
- **RAG-Based Retrieval:** Retrieve relevant information from the knowledge base using FAISS.
- **AI Response Generation:** Generate interview-related responses using the Groq API.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| LangChain | Document loading and text splitting |
| Hugging Face Embeddings | Text embedding generation |
| FAISS | Vector database and similarity search |
| Groq API | AI response generation |
| GPT-OSS-20B | Language model |
| JSON | Interview knowledge base |
| python-dotenv | Environment variable management |

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation workflow.

1. **User Input:** The user enters a question and selects an interview preparation mode.
2. **Document Loading:** Interview questions and answers are loaded from the JSON knowledge base.
3. **Text Splitting:** LangChain divides the documents into smaller text chunks.
4. **Embedding Generation:** Hugging Face Embeddings converts text into numerical vector representations.
5. **Vector Search:** FAISS retrieves relevant information based on the user's query.
6. **Prompt Preparation:** The retrieved context is combined with the user's question and selected mode.
7. **LLM Integration:** The prepared prompt is sent to the Groq API.
8. **Response Generation:** The language model generates a suitable response.
9. **Output Display:** Streamlit displays the generated response to the user.

## 📂 Project Structure

```text
Interview-Preparation-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── data/
│   └── interview_questions.json
│
└── src/
    ├── __init__.py
    ├── chatbot.py
    ├── document_loader.py
    ├── embeddings.py
    └── retriever.py
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harinigadamsetti/interview_preparation.git
```

### 2. Navigate to the Project Folder

```bash
cd interview_preparation
```

### 3. Create a Virtual Environment

```bash
py -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Required Packages

```bash
py -m pip install -r requirements.txt
```

### 6. Configure the API Key

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/keys

**Important:** Never upload your `.env` file or expose your API key publicly.

### 7. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your default browser. If it does not open automatically, visit:

```text
http://localhost:8501
```

## 📚 Knowledge Base

The application uses a manually created JSON knowledge base containing interview-related questions and answers.

The knowledge base is stored in:

`data/interview_questions.json`

It provides information that can be retrieved using the RAG pipeline to support relevant response generation.

## 🔮 Future Enhancements

- Expand the interview question knowledge base.
- Add voice-based interview practice.
- Introduce performance tracking and scoring.
- Add multiple language support.
- Integrate user authentication.
- Maintain interview practice history.
- Improve answer evaluation with detailed feedback.

## 👩‍💻 Author

**Harini Gadamsetti**

GitHub: https://github.com/harinigadamsetti

## 📄 License

This project is developed for academic and educational purposes.
