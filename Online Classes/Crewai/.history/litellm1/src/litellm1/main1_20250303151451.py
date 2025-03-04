from crewai.flow import Flow, listen, start
# from dotenv import load_dotenv
from litellm import completion


# load_dotenv()

class LitellmFlow(Flow):
    
    
    @start()
    def start_function(self):
        output = completion(messages=[{"role": "user", "content": ", Who is the founder of Pakistan?"}])
        return output



def run_litellm_flow():
    flow = LitellmFlow()
    result = flow.kickoff()
    # flow.kickoff()
    print(result)



