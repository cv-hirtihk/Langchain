from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's query in a concise manner."),
        ("user", "Question: {question}")
    ]
)

# streamlit framework
st.title("OLlama Llama3")
input_text = st.text_input("Enter your question:")

# Ollama LLama3 LLM
llm = ChatOllama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run on input
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)