from crewai.flow.flow import Flow, start, listen, router
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")

    @router(greeting)
    def select_city(self):
        cities = ["karachi", "islamabad", "lahore"]
        select_city = random.choice(cities)
        print(select_city)
        return select_city

    @listen(select_city)
    def karachi(self, city): 
        print ("write some fun fact about {city} city.")  


    
    @listen(karachi)
    def islamabad(self, city): 
        print ("write some fun fact about {city} city.")   

        
    @listen(islamabad)
    def islamabad(self, city): 
        print ("write some fun fact about {city} city.")           


def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
