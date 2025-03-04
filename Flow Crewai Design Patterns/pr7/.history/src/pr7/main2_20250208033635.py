from crewai.flow.flow import Flow, start, listen, router
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")
        cities = ["karachi", "islamabad", "lahore"]
        select_city = random.choice(cities)
        self.state['city'] = select_city

    @router(greeting)
    def select_city(self):
        cities = ["karachi", "islamabad", "lahore"]
        select_city = random.choice(cities)
        if select_city == "karachi":
            return 'karachi'
        elif select_city == 'islamabad':
            return 'islamabad'

        elif select_city == 'lahore':
            return 'lahore'    

    @listen(karachi)
    def karachi(self, city): 
        print ("write some fun fact about {city} city.")  


    
    @listen(islamabad)
    def islamabad(self, city): 
        print ("write some fun fact about {city} city.")   

        
    @listen(lahore)
    def lahore(self, city): 
        print ("write some fun fact about {city} city.")           


def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
