from crewai.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()

class LitellmFlow(Flow):
    
    
    @start()
    def start_function(self):
        output = completion(messages=[{"role": "user", "content": ", Who is the founder of Pakistan?"}])
        return output

def simple_llm():
    # Load environment variables from .env file
    load_dotenv()
    
    # Simple test message
    messages = [{"role": "user", "content": "Write hello world"}]
    
    try:
        # Make the API call
        response = completion(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        # Print the response
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def run_litellm_flow():
    flow = LitellmFlow()
    # flow.kickoff()

if __name__ == "__main__":
    simple_llm()

