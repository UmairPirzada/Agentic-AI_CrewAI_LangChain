import os

from litellm import completion


os.environ['GEMINI_API_KEY'] = "AIzaSyC87bz8mIeqqB5jmWOUw7a77Hsnu4H_UO0"

def call_gemini():

    response = completion(
    model="gemini/gemini-pro", 
    messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
)
    print (response ['choices'][0]['message']['content'])