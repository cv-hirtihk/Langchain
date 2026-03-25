from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
from langchain_ollama import ChatOllama
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A server for Langchain LLMs"
)

gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
ollama = ChatOllama(model="llama3")

gemini_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Write a haiku about the given topic."),
        ("user", "{topic}")
    ]
)
ollama_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "日本語ネイティブとして作文を書いてください。\
        条件：日本語のみ、英語禁止、100文字ちょうど、自然な文章。作文のみ出力。"),
        ("user", "{topic}")
    ]
)

add_routes(
    app,
    gemini_prompt | gemini,
    path="/haiku"
)

add_routes(
    app,
    ollama_prompt | ollama,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)