from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DevCrew:
    """Dev Crew"""
    
    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            role="Junior Python Developer",
            goal="write a python code Solution without python type hints and pydocs for this problem: '{problem}'",
            backstory="you are a junior python developer with 1 year of experience",
            
        )
        
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            role="Senior Python Developer",
            goal="Review the python code Solution without python type hints and pydocs for this problem: '{problem}'",
            backstory="you are a senior python developer with 10 years of experience",
        )
        
        
    @task
    def write_code(self) -> Task:
        return Task(
            description="Write a python code Solution without python type hints and pydocs for this problem: '{problem}'",
            expected_output="python code Solution without python type hints and pydocs for this problem: '{problem}'",
            agent=self.junior_python_developer,
        )
    @task
    def review_code(self) -> Task:
        return Task(
            description="Review the python code Solution without python type hints and pydocs for this problem: '{problem}'",
            expected_output="Review the python code Solution without python type hints and pydocs for this problem: '{problem}'",
            agent=self.senior_python_developer,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
