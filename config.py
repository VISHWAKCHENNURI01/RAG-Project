from pathlib import Path
import os
from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
ENV_FILE = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_FILE)


# Directories
DATA_DIR = BASE_DIR / "data"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"


# API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Text splitting
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


# Retrieval
TOP_K = 4


# Gemini model
LLM_MODEL = "gemini-3.5-flash"