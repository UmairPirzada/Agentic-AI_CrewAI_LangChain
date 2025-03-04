from crewai import Agent, Task, Crew
from crewai.project import  CrewBase, agent, crew, task

@CrewBase
class TeachingCrew(Crew):
    #1. Agent 
    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            role="sir_zia",
            description="sir zia is a great teacher",
            tasks=[
                self.teaching_task
            ]


        )
    #2. Task
    
           
