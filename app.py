import streamlit as st

from rag import load_knowledge
from rag import get_context

from ai import ask_ai


# --------------------------------
# Page settings
# --------------------------------

st.set_page_config(

    page_title="CodeBuddy AI",

    page_icon="💻"
)


# --------------------------------
# Title
# --------------------------------

st.title("💻 CodeBuddy AI")

st.write(
    "Your beginner-friendly coding assistant"
)


# --------------------------------
# Load knowledge
# --------------------------------

if "knowledge_loaded" not in st.session_state:

    load_knowledge()

    st.session_state.knowledge_loaded = True


# --------------------------------
# Menu
# --------------------------------

option = st.selectbox(

    "Choose what you want",

    [
        "Ask a Coding Question",
        "Explain My Code"
    ]
)


# =================================
# ASK QUESTION
# =================================

if option == "Ask a Coding Question":

    question = st.text_area(

        "Ask your programming question",

        placeholder=
        "Example: What is a for loop?"
    )


    if st.button("🤖 Ask CodeBuddy"):

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Thinking..."
            ):

                context = get_context(
                    question
                )

                answer = ask_ai(
                    question,
                    context
                )


            st.subheader(
                "💡 CodeBuddy Answer"
            )

            st.write(
                answer
            )


# =================================
# EXPLAIN CODE
# =================================

elif option == "Explain My Code":

    code = st.text_area(

        "Paste your code here",

        height=250,

        placeholder=
        """for i in range(5):
    print(i)"""
    )


    if st.button("🔍 Explain Code"):

        if code.strip() == "":

            st.warning(
                "Please enter some code."
            )

        else:

            question = f"""
Explain the following code
like I am a beginner.

Code:

{code}

Tell me:

1. What the code does
2. What each important line means
3. Example output
4. Any mistakes
5. How to improve it
"""


            with st.spinner(
                "Analyzing your code..."
            ):

                context = get_context(
                    "Python programming code explanation errors"
                )

                answer = ask_ai(
                    question,
                    context
                )


            st.subheader(
                "🧠 Code Explanation"
            )

            st.write(
                answer
            )