from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv,  find_dotenv
from litellm import completion
from project1.crews.teaching_crew.teaching_crew import TeachingCrew

_: bool = load_dotenv(find_dotenv())
class PanaFlow(Flow):

    @start()
    def generate_topic (self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                
                {"role": "user",
                 "content": "Share the most trending ai topic name"
                 }
            ],

            # max_tokens=100,
            # temperature=0.5,
      
        )
        self.state["topic"] = response['choices'][0]['message']['content']

        print(f"Step 1 Topic: {self.state['topic']}")

    @listen("generate_topic")
    def generate_content(self):
        #1. Create Crew
        print ("IN GENERATE CONTENT")
        result = TeachingCrew().crew().kickoff(
            inputs={
                "topic": self.state["topic"]
            
            }
        )
        print(result.raw)

        #2. Run Crew
        
        
def kickoff():
    flow = PanaFlow()
    flow.kickoff()
