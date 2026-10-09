from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL
)


def get_llm():

    if not GOOGLE_API_KEY:

        raise ValueError(
            "GOOGLE_API_KEY is not configured. "
            "Add it to your .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
        max_retries=3
    )

    return llm


if __name__ == "__main__":

    print(
        "Testing Gemini connection..."
    )

    llm = get_llm()

    response = llm.invoke(
        "Explain what RAG is in two sentences."
    )

    print("\nGemini response:")
    print(response.content)