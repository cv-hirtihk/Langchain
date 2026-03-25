# LangChain Project

A demonstration project showcasing LangChain integration with different Large Language Model (LLM) providers using Streamlit.

## Project Overview

This project contains two separate Streamlit applications that demonstrate LangChain's capabilities:
- **Google GenAI Integration** - Uses Google's Gemini API
- **Local Ollama Integration** - Uses Ollama with Llama3 for local inference

Both applications feature a simple chat interface that accepts user questions and returns responses powered by LangChain's prompt chaining and output parsing.

## Files

### `app.py`
Google Generative AI implementation using Gemini 2.5 Flash model.

**Features:**
- Integrates with Google's Generative AI API (Gemini)
- Uses LangChain's ChatPromptTemplate for structured prompts
- Implements a simple Streamlit web interface
- Includes LangSmith tracing for debugging and monitoring
- Model: `gemini-2.5-flash`

**Environment Variables Required:**
- `GOOGLE_API_KEY` - Your Google API key
- `LANGCHAIN_API_KEY` - Your LangChain API key

### `localama.py`
Local Ollama integration for running Llama3 on your machine.

**Features:**
- Runs inference locally using Ollama
- No external API calls required (privacy-focused)
- Uses LangChain's ChatOllama for local model integration
- Implements a simple Streamlit web interface
- Includes LangSmith tracing for debugging and monitoring
- Model: `llama3`

**Environment Variables Required:**
- `LANGCHAIN_API_KEY` - Your LangChain API key

**Prerequisites:**
- Ollama installed and running on your system
- Llama3 model downloaded: `ollama pull llama3`

### `requirements.txt`
Python dependencies for both applications:
- `langchain-google-genai` - Google Generative AI integration
- `langchain-core` - Core LangChain functionality
- `langchain-community` - Community integrations
- `streamlit` - Web framework
- `python-dotenv` - Environment variable management
- `langchain-ollama` - Ollama integration

## Installation

1. **Clone the repository and navigate to the project:**
   ```bash
   cd projects/Langchain
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

## Usage

### Running the Google GenAI Application
```bash
streamlit run app.py
```
This will launch a Streamlit app in your browser at `http://localhost:8501`. Enter your question in the text input field and receive responses from the Gemini model.

### Running the Ollama Application
```bash
streamlit run localama.py
```
Ensure Ollama is running locally before starting the app. This will launch a Streamlit app that uses your local Llama3 model for inference.

## Architecture

Both applications follow the same LangChain pattern:

1. **Prompt Template** - Defines the system message and user input structure
2. **LLM** - Instantiates the language model (Google Gemini or Ollama Llama3)
3. **Output Parser** - Converts model output to string format
4. **Chain** - Combines prompt, LLM, and output parser using LangChain's pipe operator (`|`)
5. **Streamlit UI** - Provides a simple web interface for user interaction

## Features

- **LangSmith Integration** - Both apps include LangSmith tracing (`LANGCHAIN_TRACING_V2=true`) for:
  - Monitoring prompt executions
  - Debugging chain behavior
  - Performance analysis
  
- **Modular Design** - Easy to swap different LLMs or modify prompts

- **Clean UI** - Simple Streamlit interface for quick testing

## Environment Variables

Create a `.env` file with the following (required for the respective application):

```
# Required for app.py
GOOGLE_API_KEY=your_key_here
LANGCHAIN_API_KEY=your_key_here

# Required for localama.py
LANGCHAIN_API_KEY=your_key_here
```

## Troubleshooting

**For `app.py`:**
- Ensure your Google API key has access to the Generative AI API
- Check that your `LANGCHAIN_API_KEY` is valid
- Verify internet connectivity

**For `localama.py`:**
- Ensure Ollama is running: `ollama serve`
- Verify Llama3 is installed: `ollama list`
- Pull the model if missing: `ollama pull llama3`
- Check local port availability (Ollama typically runs on `http://localhost:11434`)

## Future Enhancements

- Add conversation memory for multi-turn conversations
- Implement custom system prompts
- Add response formatting options
- Performance optimization and caching
- Support for additional LLM providers

## License

This project is provided as-is for educational purposes.

## References

- [LangChain Documentation](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [Ollama](https://ollama.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
