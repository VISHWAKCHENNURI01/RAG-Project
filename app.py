import streamlit as st

from src.rag_chain import CareerAdvisorRAG


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("🎯 AI Career Advisor")
st.subheader(
    "Personalized Career Guidance using RAG + Gemini"
)

st.write(
    "Ask questions about career paths, skills, "
    "learning roadmaps, projects, and interview preparation."
)


# --------------------------------------------------
# Initialize RAG System
# --------------------------------------------------

@st.cache_resource
def load_career_advisor():

    return CareerAdvisorRAG()


try:

    advisor = load_career_advisor()

except Exception as e:

    st.error(
        "Unable to initialize the AI Career Advisor."
    )

    st.exception(e)

    st.stop()


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("👤 Career Profile")

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name"
    )

    education = st.text_input(
        "Education",
        placeholder="e.g. BS-MS Computer Science"
    )

    experience = st.selectbox(
        "Experience Level",
        [
            "Fresher",
            "0-1 Years",
            "1-2 Years",
            "2+ Years"
        ]
    )

    target_role = st.selectbox(
        "Target Career",
        [
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Generative AI Engineer",
            "Software Developer"
        ]
    )

    st.divider()

    st.subheader("💻 Current Skills")

    python_skill = st.checkbox(
        "Python"
    )

    sql_skill = st.checkbox(
        "SQL"
    )

    statistics_skill = st.checkbox(
        "Statistics"
    )

    machine_learning_skill = st.checkbox(
        "Machine Learning"
    )

    deep_learning_skill = st.checkbox(
        "Deep Learning"
    )

    nlp_skill = st.checkbox(
        "NLP"
    )

    generative_ai_skill = st.checkbox(
        "Generative AI"
    )

    rag_skill = st.checkbox(
        "RAG"
    )

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# Collect Current Skills
# --------------------------------------------------

current_skills = []

if python_skill:
    current_skills.append("Python")

if sql_skill:
    current_skills.append("SQL")

if statistics_skill:
    current_skills.append("Statistics")

if machine_learning_skill:
    current_skills.append("Machine Learning")

if deep_learning_skill:
    current_skills.append("Deep Learning")

if nlp_skill:
    current_skills.append("NLP")

if generative_ai_skill:
    current_skills.append("Generative AI")

if rag_skill:
    current_skills.append("RAG")


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            sources = message["sources"]

            if sources:

                with st.expander(
                    "📚 Sources"
                ):

                    for source in sources:

                        st.write(
                            f"📄 {source}"
                        )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask your career question..."
)


# --------------------------------------------------
# Process Question
# --------------------------------------------------

if question:

    # Display user question
    with st.chat_message("user"):

        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # --------------------------------------------------
    # Build Personalized Question
    # --------------------------------------------------

    profile_context = f"""
User Career Profile:

Name: {name if name else "Not provided"}

Education: {
    education if education else "Not provided"
}

Experience Level: {experience}

Target Career: {target_role}

Current Skills:
{
    ", ".join(current_skills)
    if current_skills
    else "No skills selected"
}
"""


    enhanced_question = f"""
{profile_context}

User Question:
{question}

Provide career guidance based on the user's profile
and the retrieved career knowledge.
"""


    # --------------------------------------------------
    # Generate Response
    # --------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Analyzing your career question..."
        ):

            try:

                result = advisor.ask(
                    enhanced_question
                )

                answer = result["answer"]

                sources = result["sources"]


                # Display answer
                st.markdown(
                    answer
                )


                # Display sources
                if sources:

                    with st.expander(
                        "📚 Retrieved Sources"
                    ):

                        for source in sources:

                            st.write(
                                f"📄 {source}"
                            )


                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    }
                )


            except Exception as e:

                st.error(
                    "Something went wrong while "
                    "generating the response."
                )

                st.exception(e)