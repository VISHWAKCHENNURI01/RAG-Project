from src.retriever import (
    get_retriever,
    format_documents
)

from src.prompt import get_prompt

from src.llm import get_llm


class CareerAdvisorRAG:

    def __init__(self):

        self.retriever = get_retriever()

        self.prompt = get_prompt()

        self.llm = get_llm()


    def ask(self, question):
        """
        Ask a question using the RAG pipeline.
        """

        if not question.strip():

            return {
                "answer": "Please enter a question.",
                "sources": []
            }

        # Retrieve relevant documents
        documents = self.retriever.invoke(
            question
        )

        if not documents:

            return {
                "answer": (
                    "I could not find relevant "
                    "information in the career "
                    "knowledge base."
                ),
                "sources": []
            }

        # Convert documents into context
        context = format_documents(
            documents
        )

        # Create prompt
        messages = self.prompt.invoke(
            {
                "context": context,
                "question": question
            }
        )

        # Generate answer
        response = self.llm.invoke(
            messages
        )

        # Extract sources
        sources = []

        for document in documents:

            source = document.metadata.get(
                "source"
            )

            if source and source not in sources:

                sources.append(
                    source
                )

        return {
            "answer": response.content,
            "sources": sources
        }


if __name__ == "__main__":

    advisor = CareerAdvisorRAG()

    print("=" * 60)
    print("AI CAREER ADVISOR")
    print("=" * 60)

    while True:

        question = input(
            "\nAsk your career question "
            "(type 'exit' to stop): "
        )

        if question.lower() == "exit":

            print(
                "\nGoodbye!"
            )

            break

        result = advisor.ask(
            question
        )

        print("\nANSWER:")
        print("-" * 60)

        print(
            result["answer"]
        )

        print("\nSOURCES:")
        for source in result["sources"]:
            print(
                f"- {source}"
            )