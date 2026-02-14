# basic_ai_agent
Simple Python AI Agent using Google Gemini.

## Prerequisites
- Python 3.12+
- `uv` installed

## Setup

Add the project dependencies.
This updates `pyproject.toml` and creates/updates `uv.lock`.

```bash
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

## Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY="your_api_key_here"
```

> DO NOT COMMIT `.env`. INCLUDE IN `.gitignore`.

## Run

Display only the model's response:

```bash
uv run main.py "Insert your Gemini prompt here..."
```

Display prompt, token counts, and the model's repsponse:

```bash
uv run main.py "Insert your Gemini prompt here..." --verbose
```
