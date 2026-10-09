# AI Career Advisor using RAG

## Overview

AI Career Advisor is a Retrieval-Augmented Generation (RAG) application that provides personalized career guidance, skill recommendations, learning roadmaps, project ideas, and interview preparation using a curated knowledge base and Google Gemini.

## Features

* Personalized career guidance based on skills and experience.
* Semantic document retrieval using FAISS.
* Context-aware responses using Google Gemini.
* Career roadmaps, skill-gap guidance, and project recommendations.
* Interactive chat interface built with Streamlit.
* Source references for retrieved knowledge.

## Tech Stack

* **Language:** Python
* **LLM:** Google Gemini
* **Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** Hugging Face Sentence Transformers
* **Frontend:** Streamlit

## Project Workflow

1. Load career-related text documents.
2. Split documents into smaller chunks.
3. Generate embeddings using Hugging Face.
4. Store embeddings in FAISS.
5. Retrieve relevant documents based on user queries.
6. Generate contextual career advice using Gemini.
7. Display responses through Streamlit.

## Installation

```bash
git clone <your-repository-url>
cd AI-Career-Advisor
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Generate the vector store:

```bash
python -m src.vector_store
```

Run the application:

```bash
streamlit run app.py
```

## Security

Keep your `.env` file and API key private. Upload `.env.example` with a placeholder key instead.

## Future Enhancements

* Resume analysis and job description matching.
* Career recommendations based on job-market trends.
* Multi-turn conversational memory.
* Expanded career knowledge base.
