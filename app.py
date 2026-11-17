import streamlit as st

from src.retriever import create_retriever
from src.chatbot import generate_response

st.set_page_config(
    page_title="Interview Preparation Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Interview Preparation Assistant")
st.write("Prepare for technical and HR interviews using AI.")

@st.cache_resource
def load_retriever():
    return create_retriever()

try:
    retriever = load_retriever()
    st.success("Knowledge base loaded successfully!")

except Exception as e:
    st.error(f"Error loading knowledge base: {e}")
    st.stop()

mode = st.selectbox(
    "Select Preparation Mode",
    [
        "Technical Interview Questions",
        "HR Interview Questions",
        "Answer Evaluation",
        "Topic Explanation",
        "Mock Interview"
    ]
)

topic = st.text_input(
    "Enter your topic or question",
    placeholder="Example: Python, SQL, Machine Learning"
)

user_answer = ""

if mode == "Answer Evaluation":
    user_answer = st.text_area("Enter your interview answer")

if st.button("Generate Response"):

    if not topic.strip():
        st.warning("Please enter a topic or question.")

    elif mode == "Answer Evaluation" and not user_answer.strip():
        st.warning("Please enter your answer.")

    else:
        with st.spinner("Preparing your response..."):

            search_query = f"{mode} {topic} {user_answer}"

            documents = retriever.invoke(search_query)

            context = "\n\n".join(
                document.page_content
                for document in documents
            )

            response = generate_response(
                question=topic,
                context=context,
                mode=mode,
                user_answer=user_answer
            )

            st.subheader("Your AI Interview Assistant Response")
            st.write(response)