from crewai import Agent, Crew, Task
from langchain_google_genai import ChatGoogleGenerativeAI


class DevCrew:
    """Dev Crew for handling Python code tasks"""

    def __init__(self):
        # Configure the LLM with Gemini
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key="AIzaSyDSdCgBQR3POUAb0nVccITk9KtEUOuOzQk",
            temperature=0.7
        )

        self.junior_developer = Agent(
            role="Junior Python Developer",
            goal="Write a python code solution without type hints and pydocs",
            backstory="""You have 3 years of experience in python development and you're a quick learner.
            You know the latest python libraries and tools.""",
            llm=self.llm  # Assign the Gemini LLM to the agent
        )

        self.senior_developer = Agent(
            role="Senior Python Developer",
            goal="Review and enhance the code with type hints, pydocs, and tests",
            backstory="""You have 20 years of experience in Python development with expertise in 
            ML, DL, NLP, CV, LLM, and Agentic AI.""",
            llm=self.llm  # Assign the Gemini LLM to the agent
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
