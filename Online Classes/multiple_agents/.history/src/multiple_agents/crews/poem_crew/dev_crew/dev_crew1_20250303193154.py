from crewai import Agent, Crew, Task


class DevCrew:
    """Dev Crew for handling Python code tasks"""

    def __init__(self):
        self.junior_developer = Agent(
            role="Junior Python Developer",
            goal="Write a python code solution without type hints and pydocs",
            backstory="""You have 3 years of experience in python development and you're a quick learner.
            You know the latest python libraries and tools."""
        )

        self.senior_developer = Agent(
            role="Senior Python Developer",
            goal="Review and enhance the code with type hints, pydocs, and tests",
            backstory="""You have 20 years of experience in Python development with expertise in 
            ML, DL, NLP, CV, LLM, and Agentic AI."""
        )

        self.write_code_task = Task(
            description="Write a python code solution for adding two numbers",
            agent=self.junior_developer,
            expected_output="A working Python code solution"
        )

        self.review_code_task = Task(
            description="Review and enhance the code with type hints, pydocs, and tests",
            agent=self.senior_developer,
            expected_output="Enhanced Python code with documentation and tests"
        )

    def crew(self):
        """Create and return the development crew"""
        return Crew(
            agents=[self.junior_developer, self.senior_developer],
            tasks=[self.write_code_task, self.review_code_task],
            verbose=True
        )
