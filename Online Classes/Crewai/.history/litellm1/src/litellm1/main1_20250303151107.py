from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def run_litellm_flow():
    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[{"role": "user", "content": "Who is the founder of Pakistan?"}]
    )
    print(response.choices[0].message.content)
    return response



