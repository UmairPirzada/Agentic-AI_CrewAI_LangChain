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
        
        if  self.state == "karachi":
            return 'karachi'
        elif  self.state == 'islamabad':
            return 'islamabad'

        else  
            return 'lahore'    

    @listen('karachi')
    def f1(self, city): 
        print ("write some fun fact about {self.state["city"]} city.")  


    
    @listen('islamabad')
    def f2(self, city): 
        print ("write some fun fact about {city} city.")   

        
    @listen('lahore')
    def f3(self, city): 
        print ("write some fun fact about {city} city.")           


def kickoff():
    obj = RouteFlow()
    obj.kickoff()   

def plot():
    obj = RouteFlow()
    obj.plot()   
