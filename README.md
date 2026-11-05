# 🎓 College Inquiry Chatbot using NLP and FLAN-T5

An AI-powered chatbot that answers college-related queries using **semantic similarity** and **Natural Language Generation (NLG)**. The chatbot first searches a predefined FAQ dataset using sentence embeddings and cosine similarity. If no suitable match is found, it generates a human-like response using Google's **FLAN-T5** language model.

---

## 📌 Project Overview

The College Inquiry Chatbot is designed to automate responses to common student queries regarding admissions, courses, fees, scholarships, placements, hostel facilities, and campus infrastructure.

Unlike traditional keyword-based chatbots, this system understands the **meaning** of user queries using **Sentence Transformers** and provides accurate, context-aware responses. For unseen questions, it leverages **FLAN-T5** to generate intelligent and natural answers.

---

## ✨ Features

- 🤖 AI-powered conversational chatbot
- 🔍 Semantic search using Sentence Transformers
- 📚 FAQ retrieval based on cosine similarity
- 💬 Human-like answer generation using FLAN-T5
- 🎯 Accurate responses even with different wording
- ⚡ Fast inference with lightweight MiniLM embeddings
- 🌐 Interactive Gradio interface
- 📈 Confidence score using similarity matching

---

# 🏗️ System Architecture

```
                  User Question
                        │
                        ▼
            Text Preprocessing
                        │
                        ▼
      Sentence Transformer (MiniLM)
             Generate Embeddings
                        │
                        ▼
           Cosine Similarity Search
                        │
          ┌─────────────┴─────────────┐
          │                           │
 Similarity ≥ 0.60             Similarity < 0.60
          │                           │
          ▼                           ▼
 Retrieve FAQ Answer          Generate Answer
                               using FLAN-T5
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 Final Response
                        │
                        ▼
                  Gradio Interface
```

---

# 🎯 Objectives

- Build an intelligent college inquiry chatbot.
- Automate responses to frequently asked questions.
- Improve response accuracy using semantic understanding.
- Generate natural responses for unseen questions.
- Reduce manual support for college inquiry systems.

---

# 📚 Use Cases

The chatbot can answer questions related to:

- Admission Process
- Eligibility Criteria
- Available Courses
- Fee Structure
- Scholarships
- Hostel Facilities
- Placements
- Internship Opportunities
- Library
- Campus Facilities
- Examination Details
- Student Support

---

# 🛠️ Technologies Used

## Programming Language

- Python

## NLP & Deep Learning

- Sentence Transformers
- Hugging Face Transformers
- FLAN-T5
- PyTorch

## Machine Learning

- Cosine Similarity
- Semantic Search

## Libraries

- Pandas
- NumPy
- Scikit-learn
- Gradio

---

# 🤖 Models Used

## 1. Sentence Transformer (all-MiniLM-L6-v2)

The Sentence Transformer converts text into dense vector embeddings that capture semantic meaning.

### Purpose

- Sentence Embedding
- Semantic Understanding
- FAQ Matching
- Fast Inference
- High Accuracy

---

## 2. FLAN-T5

FLAN-T5 is used whenever the chatbot cannot confidently retrieve an answer from the FAQ dataset.

### Purpose

- Natural Language Generation
- Human-like Responses
- Context-aware Answers
- Text-to-Text Learning

---

# ⚙️ Methodology

### Step 1 – Dataset Preparation

- Load a CSV dataset containing college FAQs.
- Each row contains a Question and Answer pair.

---

### Step 2 – Data Cleaning

- Remove missing values.
- Rename columns to standard format.
- Prepare data for processing.

---

### Step 3 – Generate Embeddings

- Convert every FAQ question into vector embeddings using **all-MiniLM-L6-v2**.

---

### Step 4 – User Query Processing

- Convert the user's question into an embedding using the same model.

---

### Step 5 – Similarity Matching

- Compute cosine similarity between the user query and stored FAQ embeddings.
- Select the most similar question.

---

### Step 6 – Decision Making

- If similarity score ≥ **0.60**, retrieve the corresponding FAQ answer.
- Otherwise, generate a new response using **FLAN-T5**.

---

### Step 7 – Response Generation

- FLAN-T5 generates a polite and context-aware response.
- The chatbot behaves like a virtual college counselor.

---

### Step 8 – Display Output

- Show the final answer.
- Display similarity score for transparency.

---

# 📂 Project Structure

```
College-Inquiry-Chatbot/
│
├── app.py
├── chatbot.py
├── preprocess.py
├── requirements.txt
├── README.md
├── college_qa_dataset.csv
│
├── models/
│
├── assets/
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/college-inquiry-chatbot.git
```

Move into the project folder

```bash
cd college-inquiry-chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python app.py
```

The chatbot launches on Gradio:

```
http://127.0.0.1:7860
```

---

# 📸 Sample Questions

- What courses are available?
- What is the admission process?
- What is the hostel fee?
- Are scholarships available?
- What are the placement opportunities?
- Is transportation available?
- What documents are required for admission?
- Does the college provide internships?

---

# 📊 Future Improvements

- Voice-enabled chatbot
- Multi-language support
- FAISS Vector Database
- RAG Pipeline
- LangChain Integration
- GPT-4 / Llama Support
- WhatsApp Integration
- PDF Document Search
- Student Login Portal
- Conversation Memory

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Natural Language Processing (NLP)
- Semantic Search
- Sentence Embeddings
- Hugging Face Transformers
- Large Language Models (LLMs)
- Prompt Engineering
- Retrieval-based Chatbots
- Python Development
- Machine Learning
- AI Application Development

---

# 👨‍💻 Author

**Harsh Kumar Gaurav**


