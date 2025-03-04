from crewai import Agent, Task, Crew
from crewai.project import  CrewBase, agent, crew, task

@CrewBase
class TeachingCrew(Crew):
    @agent()
    class PanaAgent(Agent):
        @task()
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
    
        @task()
        def generate_content(self):
            response = completion(
                model="gemini/gemini-2.0-flash",
                messages=[
                    
                    {"role": "user",
                     "content": "Generate content for the topic"
                     }
                ],
    
                # max_tokens=100,
                # temperature=0.5,
          
            )
            self.state["content"] = response['choices'][0]['message']['content']
    
            print(f"Step 2 Content: {self.state['content']}")
            )

