from pathlib import Path

from langchain_community.vectorstores import FAISS

from src.config import VECTORSTORE_DIR
from src.document_loader import load_and_split_documents
from src.embeddings import get_embedding_model


def create_vector_store():
    """
    Create a FAISS vector store from the
    career knowledge base.
    """

    print(
        "\nLoading documents..."
    )

    chunks = load_and_split_documents()

    print(
        f"Total chunks: {len(chunks)}"
    )

    if not chunks:
        raise ValueError(
            "No documents were found in the data directory."
        )

    print(
        "\nLoading embedding model..."
    )

    embeddings = get_embedding_model()

    print(
        "\nCreating FAISS vector store..."
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    VECTORSTORE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(
        str(VECTORSTORE_DIR)
    )

    print(
        "\nFAISS vector store created successfully."
    )

    print(
        f"Saved at: {VECTORSTORE_DIR}"
    )

    return vector_store


def load_vector_store():
    """
    Load an existing FAISS vector store.
    """

    if not VECTORSTORE_DIR.exists():

        raise FileNotFoundError(
            "Vector store does not exist. "
            "Run create_vector_store() first."
        )

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


if __name__ == "__main__":

    print("=" * 60)
    print("CREATING FAISS VECTOR DATABASE")
    print("=" * 60)

    create_vector_store()