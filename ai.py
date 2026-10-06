import ollama


def ask_ai(question, context):

    prompt = f"""
You are CodeBuddy AI.

You are a beginner-friendly programming assistant.

Use the information below to answer the user's question.

Knowledge:
{context}

User question:
{question}

Rules:

1. Explain in very simple English.
2. If code is needed, give a small example.
3. Explain why the code works.
4. Do not make up information.
5. If the question is about an error, explain:
   - What the error means
   - Why it happened
   - How to fix it
"""

    response = ollama.chat(

        model="llama3.2:3b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]