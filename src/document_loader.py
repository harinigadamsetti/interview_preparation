import json
from langchain_core.documents import Document

def load_documents():
    with open("data/interview_questions.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    documents = []

    for item in data:
        content = f"Category: {item['category']}\nQuestion: {item['question']}\nAnswer: {item['answer']}"

        documents.append(
            Document(
                page_content=content,
                metadata={"category": item["category"]}
            )
        )

    return documents