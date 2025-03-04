from crewai import Task, Crew, Agent
from crewai.project.crew_base import CrewBase
from crewai.project.annotations import task, agent


class DevCrew(CrewBase):
    @agent
    def junior_developer(self):
        return Agent(
            role="Junior Python Developer",
            goal="Write a python code solution without type hints and pydocs",
            backstory="""You have 3 years of experience in python development and you're a quick learner.
            You know the latest python libraries and tools."""
        )

    @agent
    def senior_developer(self):
        return Agent(
            role="Senior Python Developer",
            goal="Review and enhance the code with type hints, pydocs, and tests",
            backstory="""You have 20 years of experience in Python development with expertise in 
            ML, DL, NLP, CV, LLM, and Agentic AI."""
        )

    @task
    def write_code(self):
        return Task(
            description="Write a python code solution for adding two numbers",
            agent=self.junior_developer,
            expected_output="A working Python code solution"
        )

    @task
    def review_code(self):
        return Task(
            description="Review and enhance the code with type hints, pydocs, and tests",
            agent=self.senior_developer,
            expected_output="Enhanced Python code with documentation and tests"
        )

    def crew(self):
        return Crew(
            agents=[self.junior_developer, self.senior_developer],
            tasks=[self.write_code, self.review_code],
            verbose=True
        )
