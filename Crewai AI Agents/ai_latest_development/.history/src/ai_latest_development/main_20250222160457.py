#!/usr/bin/env python
import warnings
from crewai import Crew, Process, Agent, Task
from pathlib import Path
import yaml
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

class AiLatestDevelopment:
    def __init__(self):
        load_dotenv()
        self.config_dir = Path(__file__).parent / "config"
        
        # Get API key from environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
            
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=api_key,
            temperature=0.7,
            convert_system_message_to_human=True
        )
        
    def create_agents(self):
        with open(self.config_dir / 'agents.yaml', 'r') as file:
            agents_config = yaml.safe_load(file)
            
        agents = {}
        for name, config in agents_config.items():
            agents[name] = Agent(
                role=config['role'],
                goal=config['goal'],
                backstory=config['backstory'],
                verbose=config['verbose'],
                llm=self.llm,
                allow_delegation=True
            )
        return agents
            
    def create_tasks(self, agents):
        with open(self.config_dir / 'tasks.yaml', 'r') as file:
            tasks_config = yaml.safe_load(file)
            
        tasks = []
        for name, config in tasks_config.items():
            tasks.append(
                Task(
                    description=config['description'],
                    agent=agents[config['agent']],
                    expected_output=config['expected_output']
                )
            )
        return tasks

    def crew(self):
        agents = self.create_agents()
        tasks = self.create_tasks(agents)
        
        return Crew(
            agents=list(agents.values()),
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

def run():
    try:
        crew = AiLatestDevelopment().crew()
        result = crew.kickoff()
        print("\nFinal Result:", result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run()


    # try:
        # AiLatestDevelopment().crew().kickoff(inputs=inputs)       
    # except Exception as e:
    #     raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiLatestDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AiLatestDevelopment().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiLatestDevelopment().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
