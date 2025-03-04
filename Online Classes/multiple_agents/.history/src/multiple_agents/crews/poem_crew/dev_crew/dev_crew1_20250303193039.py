from crewai import Agent, Crew, Task
from crewai.project import CrewBase
from crewai.project.annotations import task, agent

@c
class DevCrew(CrewBase):
    """Dev Crew for handling Python code tasks"""

    def __init__(self):
        super().__init__()
        self.load_configurations()

    @agent
    def junior_developer(self):
        """Create a junior developer agent"""
        return Agent(
            role="Junior Python Developer",
            goal="Write a python code solution without type hints and pydocs",
            backstory="""You have 3 years of experience in python development and you're a quick learner.
            You know the latest python libraries and tools."""
        )

    @agent
    def senior_developer(self):
        """Create a senior developer agent"""
        return Agent(
            role="Senior Python Developer",
            goal="Review and enhance the code with type hints, pydocs, and tests",
            backstory="""You have 20 years of experience in Python development with expertise in 
            ML, DL, NLP, CV, LLM, and Agentic AI."""
        )

    @task
    def write_code(self):
        """Task for writing initial code"""
        return Task(
            description="Write a python code solution for adding two numbers",
            agent=self.junior_developer,
            expected_output="A working Python code solution"
        )

    @task
    def review_code(self):
        """Task for reviewing and enhancing code"""
        return Task(
            description="Review and enhance the code with type hints, pydocs, and tests",
            agent=self.senior_developer,
            expected_output="Enhanced Python code with documentation and tests"
        )

    def crew(self):
        """Create and return the development crew"""
        return Crew(
            agents=[self.junior_developer, self.senior_developer],
            tasks=[self.write_code, self.review_code],
            verbose=True
        )
