from crewai import Flow, listen, start, route
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")

    @listen(greeting)
    def select_city(self):
        cities = ["Karachi", "Islamabad", "Lahore"]
        select_city = random.choice()