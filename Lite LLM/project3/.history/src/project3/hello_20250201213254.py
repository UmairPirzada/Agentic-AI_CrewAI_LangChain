import os
os.environ["GEMINI_API_KEY"] = "your-api-key"
from litellm import completion


os.environ['GEMINI_API_KEY'] = ""

def call_gemini():

    response = completion(
    model="gemini/gemini-pro", 
    messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
)
    print (response(]))