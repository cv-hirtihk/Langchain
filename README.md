# LangChain Project

A comprehensive demonstration project showcasing LangChain integration with different Large Language Model (LLM) providers using FastAPI backend and Streamlit frontend.

## Project Overview

This project has evolved into a client-server architecture with:
- **FastAPI Backend** (`/api/app.py`) - Exposes LLM endpoints via REST API using LangServe
- **Streamlit Client** (`/api/client.py`) - Web UI that consumes the API
- **Original Streamlit Apps** (`app.py`, `localama.py`) - Standalone applications for direct LLM interaction

The project demonstrates:
- **Google GenAI Integration** - Uses Google's Gemini 2.5 Flash for haiku generation
- **Ollama Integration** - Uses Llama3 for Japanese essay generation
- **API-First Design** - LangServe for easy API routing and LLM serving

## Files

### API Folder (`/api/`)

#### `api/app.py` (FastAPI Backend)
FastAPI server exposing LLM endpoints using LangServe for easy routing and API management.

**Features:**
- FastAPI REST API server
- LangServe integration for automatic API routing
- Two main endpoints:
  - `/haiku` - Generates haikus about a given topic using Gemini
  - `/essay` - Generates Japanese essays about a given topic using Ollama
- Chains both models with custom prompts
- Runs on `localhost:8000`

**Models Used:**
- Google Gemini 2.5 Flash
- Ollama Llama3 (requires local Ollama installation)

#### `api/client.py` (Streamlit Frontend)
Streamlit web application that consumes the FastAPI backend.

**Features:**
- User-friendly web interface
- Text input for topic specification
- Displays both Gemini haikus and Ollama essays side-by-side
- Makes HTTP POST requests to the FastAPI backend
- Robust error handling for API failures and response parsing
- 30-second timeout protection for API calls
- Runs on `localhost:8501`

**Dependencies:**
- Requires FastAPI server to be running

### Root Level Files

### `app.py`
Google Generative AI implementation using Gemini 2.5 Flash model (Streamlit standalone).

**Features:**
- Integrates with Google's Generative AI API (Gemini)
- Uses LangChain's ChatPromptTemplate for structured prompts
- Implements a simple Streamlit web interface
- Model: `gemini-2.5-flash`

### `localama.py`
Local Ollama integration for running Llama3 on your machine (Streamlit standalone).

**Features:**
- Runs inference locally using Ollama
- Uses LangChain's ChatOllama for local model integration
- Implements a simple Streamlit web interface
- Model: `llama3`

### `requirements.txt`
Python dependencies for the project:
- `langchain-google-genai` - Google Generative AI integration
- `langchain-core` - Core LangChain functionality
- `langchain-community` - Community integrations
- `streamlit` - Web framework
- `python-dotenv` - Environment variable management
- `langchain-ollama` - Ollama integration
- `fastapi` - API framework
- `langserve` - LangChain API serving
- `uvicorn` - ASGI server
- `requests` - HTTP client

## Installation

1. **Navigate to the project:**
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

5. **Prerequisites for Ollama:**
   - Install and run Ollama: https://ollama.ai/
   - Pull the Llama3 model:
   ```bash
   ollama pull llama3 (or model of your choice)
   ollama serve
   ```

## Usage

### Option 1: API Backend + Streamlit Client (Recommended)

**Terminal 1 - Start the FastAPI server:**
```bash
cd api
python app.py
```
The API server will start on `http://localhost:8000`

Available endpoints:
- `POST http://localhost:8000/haiku/invoke` - Generate haikus
- `POST http://localhost:8000/essay/invoke` - Generate Japanese essays

**Terminal 2 - Start the Streamlit client:**
```bash
cd api
streamlit run client.py
```
The client will open in your browser at `http://localhost:8501`. Enter a topic and get responses from both Gemini and Ollama.

### Option 2: Standalone Streamlit Applications

**Run the Google GenAI Application:**
```bash
streamlit run app.py
```

**Run the Ollama Application:**
```bash
streamlit run localama.py
```

## Architecture

### API Backend Architecture
The FastAPI backend follows this pattern:

1. **LLM Initialization** - Instantiate language models (ChatGoogleGenerativeAI, ChatOllama)
2. **Prompt Templates** - Define system and user message prompts with variable placeholders
3. **Chain Composition** - Combine prompts and LLMs using the pipe operator (`|`)
4. **Route Registration** - Register chains as API endpoints using LangServe's `add_routes()`
5. **Request/Response** - Accept JSON requests and return LLM-generated responses

**Endpoints:**
- `/haiku` - Accepts `{"topic": "..."}` and returns a haiku
- `/essay` - Accepts `{"topic": "..."}` and returns a Japanese essay

### Client Architecture
The Streamlit client communicates with the API:

1. **User Input** - Text input for topic specification
2. **API Calls** - Makes POST requests to `/haiku/invoke` and `/essay/invoke`
3. **Response Display** - Shows results from both endpoints

### Standalone Applications
The original Streamlit apps (`app.py` and `localama.py`) follow this pattern:

1. **Prompt Template** - Defines the system message and user input structure
2. **LLM** - Instantiates the language model (Google Gemini or Ollama Llama3)
3. **Output Parser** - Converts model output to string format
4. **Chain** - Combines prompt, LLM, and output parser using LangChain's pipe operator (`|`)
5. **Streamlit UI** - Provides a simple web interface for user interaction

## Features

- **FastAPI Backend** - Fast, scalable API for LLM serving using LangServe
- **Automatic API Documentation** - FastAPI provides interactive docs at `/docs` and `/redoc`
- **Streamlit Frontend** - User-friendly interface for API consumption
- **Multi-Model Support** - Easily add or swap LLM providers
- **Modular Design** - Prompts and chains are easily customizable
- **Japanese Language Support** - Specialized prompts for Japanese essay generation
- **Local Inference Option** - Privacy-focused Ollama integration
- **Production-Ready** - LangServe handles routing, serialization, and error handling

## Environment Variables

Create a `.env` file in the project root with:

```
# Required for Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# Optional: For LangSmith debugging and monitoring
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

## Troubleshooting

**FastAPI Server Issues:**
- Ensure port `8000` is available: `netstat -ano | findstr :8000` (Windows)
- Check that dependencies are installed: `pip install -r requirements.txt`
- Verify `GOOGLE_API_KEY` is set in `.env` file

**Streamlit Client Issues:**
- Ensure FastAPI server is running at `http://localhost:8000`
- Confirm port `8501` is available
- Check that requests library is installed: `pip install requests`

**Gemini/Google API Issues:**
- Verify your Google API key has access to Generative AI API
- Check internet connectivity
- Ensure the API key is in the `.env` file

**Ollama Issues:**
- Ensure Ollama is running: `ollama serve`
- Verify Llama3 is installed: `ollama list`
- Pull the model if missing: `ollama pull llama3`
- Check that Ollama is accessible at `http://localhost:11434`
- Verify the system has adequate resources (Llama3 requires ~4GB RAM)

## API Documentation

When running the FastAPI server, you can access:
- **Swagger UI** - `http://localhost:8000/docs` - Interactive API exploration
- **ReDoc** - `http://localhost:8000/redoc` - API documentation in ReDoc format

Both provide full documentation of available endpoints and request/response schemas.

## Future Enhancements

- Add authentication/authorization for the API
- Implement response caching for identical requests
- Add conversation memory for multi-turn interactions
- Support for additional LLM providers (OpenAI, Anthropic, etc.)
- Database integration for request/response logging
- WebSocket support for streaming responses
- Rate limiting and quota management
- Docker containerization for easy deployment
- Custom system prompts via API parameters
- Response formatting options (JSON, plain text, markdown)

## License

This project is provided as-is for educational purposes.

## References

- [LangChain Documentation](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [Ollama](https://ollama.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
