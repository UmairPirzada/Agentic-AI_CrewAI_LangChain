from crewai.flow.flow import Flow, start, listen, route
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")

    @listen(greeting)
    def select_city(self):
        cities = ["Karachi", "Islamabad", "Lahore"]
        select_city = random.choice(cities)
        print(select_city)


def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
