from crewai import Flow, listen, start, route

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam_0_alikum!")

    @listen(greeting)
    def select_city(self):
        cities = ["arachi", "Islamabad"]