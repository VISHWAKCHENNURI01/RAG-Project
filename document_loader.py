from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP


def load_documents():
    documents = []

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Data directory not found: {DATA_DIR}"
        )

    for file_path in DATA_DIR.rglob("*.txt"):
        try:
            text = file_path.read_text(encoding="utf-8")

            if not text.strip():
                continue

            document = Document(
                page_content=text,
                metadata={
                    "source": str(file_path.relative_to(DATA_DIR)),
                    "filename": file_path.name,
                    "category": file_path.parent.name
                }
            )

            documents.append(document)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    return text_splitter.split_documents(documents)


def load_and_split_documents():
    """
    Load all TXT files from the data directory
    and split them into smaller chunks.
    """
    documents = load_documents()

    if not documents:
        raise ValueError(
            "No TXT documents found in the data directory."
        )

    chunks = split_documents(documents)

    return chunks


if __name__ == "__main__":

    print("=" * 60)
    print("AI CAREER ADVISOR - DOCUMENT LOADER")
    print("=" * 60)

    documents = load_documents()

    print(f"\nDocuments loaded: {len(documents)}")

    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    if chunks:

        print("\nSample chunk:")
        print("-" * 60)

        print(chunks[0].page_content)

        print("\nMetadata:")
        print(chunks[0].metadata)