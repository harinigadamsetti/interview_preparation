
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(question, context, mode, user_answer=""):

    prompt = f"""
    You are an Interview Preparation Assistant.

    Mode: {mode}

    Retrieved Knowledge:
    {context}

    User Question:
    {question}

    User Answer:
    {user_answer}

    Instructions:
    - Give simple and clear explanations.
    - Generate relevant interview questions.
    - Evaluate answers and explain mistakes.
    - Suggest improved answers.
    - Provide useful interview preparation tips.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_completion_tokens=2048
    )

    return response.choices[0].message.content
