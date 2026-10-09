from src.vector_store import load_vector_store
from src.config import TOP_K


def get_retriever():
    """
    Load FAISS and return a retriever.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": TOP_K
        }
    )

    return retriever


def retrieve_documents(query):
    """
    Retrieve documents relevant to a query.
    """

    retriever = get_retriever()

    documents = retriever.invoke(
        query
    )

    return documents


def format_documents(documents):
    """
    Format retrieved documents into context
    for the LLM.
    """

    formatted_documents = []

    for doc in documents:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        content = doc.page_content

        formatted_documents.append(
            f"Source: {source}\n"
            f"Content:\n{content}"
        )

    return "\n\n".join(
        formatted_documents
    )


if __name__ == "__main__":

    query = input(
        "\nEnter your career question: "
    )

    documents = retrieve_documents(
        query
    )

    print(
        f"\nRetrieved documents: "
        f"{len(documents)}"
    )

    for index, document in enumerate(
        documents,
        start=1
    ):

        print(
            f"\n--- Result {index} ---"
        )

        print(
            document.page_content
        )

        print(
            "Source:",
            document.metadata.get(
                "source"
            )
        )