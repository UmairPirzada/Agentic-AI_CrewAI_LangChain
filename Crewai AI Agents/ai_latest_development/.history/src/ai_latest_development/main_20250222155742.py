#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai import Crew, Process
from pathlib import Path
import yaml
import os
from dotenv import load_dotenv

# from ai_latest_development.crew import AiLatestDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

class AiLatestDevelopment:
    def __init__(self):
        load_dotenv()
        self.config_dir = Path(__file__).parent / "config"
        
    def load_config(self, filename):
        with open(self.config_dir / filename, 'r') as file:
            return yaml.safe_load(file)
            
    def crew(self):
        agents_config = self.load_config('agents.yaml')
        tasks_config = self.load_config('tasks.yaml')
        
        return Crew(
            agents=agents_config,
            tasks=tasks_config,
            process=Process.sequential
        )

def run():
    try:
        crew = AiLatestDevelopment().crew()
        result = crew.kickoff()
        print("Result:", result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

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
