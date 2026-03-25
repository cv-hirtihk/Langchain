import requests
import streamlit as st

def get_gemini_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/haiku/invoke",
            json={"input": {"topic": input_text}},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("output", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        return f"Error calling API: {str(e)}"
    except (KeyError, ValueError) as e:
        return f"Error parsing response: {str(e)}"

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"input": {"topic": input_text}},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("output", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        return f"Error calling API: {str(e)}"
    except (KeyError, ValueError) as e:
        return f"Error parsing response: {str(e)}"

st.title("LLM Client")
input_text = st.text_input("Enter a topic:")
if input_text:
    gemini_response = get_gemini_response(input_text)
    ollama_response = get_ollama_response(input_text)

    st.subheader("Gemini Haiku")
    st.write(gemini_response)

    st.subheader("Ollama Essay")
    st.write(ollama_response)