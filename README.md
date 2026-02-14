# basic_ai_agent
Simple Python AI Agent using Google Gemini.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
```

Install dependencies:
```bash
pip install "google-genai==1.12.1" "python-dotenv==1.1.0"
```

## Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY="your_api_key_here"
```

> DO NOT COMMIT `.env`. INCLUDE IN `.gitignore`.

## Run

```bash
python main.py
```

## Dependencies
- google-genai==1.12.1
- python-dotenv==1.1.0


