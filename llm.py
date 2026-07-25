from google import genai
from google.genai.errors import ClientError
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:
        if "RESOURCE_EXHAUSTED" in str(e):
            return (
                "⚠️ Gemini API quota exceeded.\n\n"
                "Please try again after your daily quota resets "
                "or use another API key."
            )

        return f"API Error: {e}"

    except Exception as e:
        return f"Unexpected Error: {e}"
