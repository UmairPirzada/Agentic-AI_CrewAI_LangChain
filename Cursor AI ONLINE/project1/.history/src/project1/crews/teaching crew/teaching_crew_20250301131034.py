from crewai import Agent, Task, Crew
from crewai.project import  CrewBase, agent, crew, task

@CrewBase
class TeachingCrew(Crew):
    agent_config ="config/agent.yaml"
    task_config = "config/task.yaml"
    
    #1. Agent 
    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            c
            
            ]


        )
    #2. Task
    
           
