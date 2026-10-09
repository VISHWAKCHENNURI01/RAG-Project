from langchain_huggingface import HuggingFaceEmbeddings

from src.config import EMBEDDING_MODEL


def get_embedding_model():
    """
    Load the Hugging Face embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    return embeddings


if __name__ == "__main__":

    print(
        "Loading embedding model..."
    )

    embeddings = get_embedding_model()

    print(
        "Embedding model loaded successfully."
    )

    test_text = (
        "Python is an important skill "
        "for Data Science."
    )

    vector = embeddings.embed_query(
        test_text
    )

    print(
        f"Embedding dimensions: {len(vector)}"
    )