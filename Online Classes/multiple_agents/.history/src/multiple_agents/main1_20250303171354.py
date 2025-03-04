from crewai.flow import Flow, listen, start
from multiple_agents.crews.poem_crew.dev_crew.dev_crew import DevCrew



class DevFlow(Flow):
    @start()
    def start_flow(self):
        print("Starting flow")
        self.state.problem = "Write a python code to solve the problem"


