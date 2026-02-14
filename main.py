import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Missing GEMINI_API_KEY. Insert into .env file. (Reminder: Do not share API keys)"
        )

    contents="Using only a single paragraph, what is the difference between information technology and information security?"

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )

    usage = response.usage_metadata
    if usage is None:
        raise RuntimeError(
            "No usage_metadata returned."
        )
    
    print(f"User prompt: {contents}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    raise SystemExit(main())
