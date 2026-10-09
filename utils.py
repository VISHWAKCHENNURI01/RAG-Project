def clean_text(text):
    """
    Remove unnecessary whitespace.
    """

    if not text:
        return ""

    return " ".join(
        text.split()
    )


def get_unique_sources(documents):
    """
    Extract unique source filenames.
    """

    sources = []

    for document in documents:

        source = document.metadata.get(
            "source"
        )

        if source and source not in sources:

            sources.append(
                source
            )

    return sources