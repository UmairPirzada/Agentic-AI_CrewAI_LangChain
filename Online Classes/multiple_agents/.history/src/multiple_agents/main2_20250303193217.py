from crewai.flow import Flow, start
from multiple_agents.crews.poem_crew.dev_crew.dev_crew1 import DevCrew


class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        output = DevCrew().crew().kickoff()
        return output.raw


def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)


if __name__ == "__main__":
    kickoff()

