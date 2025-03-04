from crewai.flow import Flow, listen, start
from multiple_agents.crews.poem_crew.dev_crew.dev_crew import DevCrew



class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={"problem":"write a python code  for adding two numbers"}
            )
        return output.raw


def kickoff():
    dflow = DevFlow()
    flow.kickoff()
    print(flow.state.output)

if __name__ == "__main__":
    kickoff()