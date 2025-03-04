from crewai.flow.flow import Flow, start, listen, router
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")

    @router(greeting)
    def select_city(self):
        cities = ["karachi", "islamabad", "lahore"]
        selected_city = random.choice(cities)

        if selected_city == "karachi":
            return self.karachi
        elif selected_city == "islamabad":
            return self.islamabad
        elif selected_city == "lahore":
            return self.lahore

    @listen
    def karachi(self, city): 
        print(f"Write some fun fact about {city} city.")  

    @listen
    def islamabad(self, city): 
        print(f"Write some fun fact about {city} city.")   

    @listen
    def lahore(self, city): 
        print(f"Write some fun fact about {city} city.")           

def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
