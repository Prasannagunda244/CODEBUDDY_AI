from database import add_knowledge
from database import search_knowledge


def load_knowledge():

    with open(
        "knowledge.txt",
        "r"
    ) as file:

        text = file.read()


    # Split knowledge into paragraphs

    chunks = text.split("\n\n")


    for i, chunk in enumerate(chunks):

        if chunk.strip():

            add_knowledge(
                chunk,
                f"knowledge_{i}"
            )


def get_context(question):

    results = search_knowledge(
        question
    )

    documents = results["documents"][0]

    context = "\n\n".join(
        documents
    )

    return context