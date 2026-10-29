import time
from google import genai
from google.genai.errors import ServerError

client = genai.Client(api_key="YOUR_API_KEY")

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="What are pokemon",
        )
        print(response.text)
        break
    except ServerError:
        print(f"Server busy, retrying in 3 seconds... (Attempt {attempt + 1}/3)")
        time.sleep(3)