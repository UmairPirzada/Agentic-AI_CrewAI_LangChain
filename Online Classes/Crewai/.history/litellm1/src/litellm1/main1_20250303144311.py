from crewai.flow import Flow, listen, start
from dotenv import load_dotenv

load_dotenv()

from litellm import completion

class LitellmFlow(Flow):
    
    
    @start()
    def start_function(self):
        output = completion(messages=[{"role": "user", "content": ", Who is the founder of Pakistan?"}])

def run_litellm_flow():
    onj  = LitellmFlow()
    flow.kickoff()

if __name__ == "__main__":
    run_litellm_flow()
