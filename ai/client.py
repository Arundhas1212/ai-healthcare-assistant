from google import genai
from core.config import Config

client = genai.Client(api_key=Config.GOOGLE_API_KEY)


def get_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text
