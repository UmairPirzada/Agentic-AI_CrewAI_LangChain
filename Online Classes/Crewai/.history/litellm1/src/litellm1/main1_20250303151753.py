from crewai.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion
import os


load_dotenv()

class LitellmFlow(Flow):
    
    
    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-2.0-flash",  # Specify the model
            messages=[{"role": "user", "content": "Who is the founder of Pakistan?"}]
        )
        return output[]



def run_litellm_flow():
    flow = LitellmFlow()
    result = flow.kickoff()
    # flow.kickoff()
    print(result)



