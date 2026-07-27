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
                "The Gemini API quota has been reached. "
                "Please try again later."
            )

        return f"API Error: {e}"

    except Exception:
        return (
            "An unexpected error occurred while generating the response. "
            "Please try again."
        )
