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
            config=self.agent_config["sir_zia"],
 #2. Task
    @task
    def describe_topic(self) -> Task:
        return Task(
            config=self.task_config["describe_topic"]
        )        
    
#3. Crew
    @crew
    def teaching_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            
        )        
