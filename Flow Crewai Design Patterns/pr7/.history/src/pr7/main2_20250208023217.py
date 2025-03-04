from crewai import Flow, listen, start, route

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalikum 0 alikum")