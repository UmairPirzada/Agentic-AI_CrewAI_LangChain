from crewai import Agent, Task, Crew
from crewai.project import  CrewBase, agent, crew, task

@CrewBase
class TeachingCrew(Crew):
    
                # max_tokens=100,
                # temperature=0.5,
          
            )
            self.state["content"] = response['choices'][0]['message']['content']
    
            print(f"Step 2 Content: {self.state['content']}")
            )

