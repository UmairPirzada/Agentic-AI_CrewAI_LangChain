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

    @listen(karachi)
    def karachi1(self, city): 
        print ("write some fun fact about {city} city.")  


    
    @listen(islamabad)
    def islamabad1(self, city): 
        print ("write some fun fact about {city} city.")   

        
    @listen(lahore)
    def lahore1(self, city): 
        print ("write some fun fact about {city} city.")           


def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
