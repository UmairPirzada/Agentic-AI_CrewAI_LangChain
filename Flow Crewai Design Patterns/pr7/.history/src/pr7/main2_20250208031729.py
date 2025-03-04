from crewai.flow.flow import Flow, start, listen, router
from litellm import completion

API_KEY = "AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M"

# from crewai.flow.flow import Flow, start, listen, router
# from litellm import completion

# Replace with your actual API Key
API_KEY = "your-api-key-here"

class CityRoutingFlow(Flow):

    @start()
    def greeting(self):
        """ Initial greeting before classification """
        print("Assalam-o-Alaikum! Let's explore fun facts about a city.")

    @router(greeting)
    def classify_city(self):
        """ Uses an LLM to classify which city to route to. """
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"role": "user", "content": "Pick a random city from Karachi, Islamabad, or Lahore."}]
        )
        
        selected_city = response["choices"][0]["message"]["content"].strip().lower()

        city_routes = {
            "karachi": self.karachi_facts,
            "islamabad": self.islamabad_facts,
            "lahore": self.lahore_facts
        }

        return city_routes.get(selected_city, self.default_response)

    @listen
    def karachi_facts(self):
        """ Handler for Karachi facts """
        print("Karachi is the financial hub of Pakistan and home to the country's largest port.")

    @listen
    def islamabad_facts(self):
        """ Handler for Islamabad facts """
        print("Islamabad is Pakistan's capital, known for its scenic beauty and modern infrastructure.")

    @listen
    def lahore_facts(self):
        """ Handler for Lahore facts """
        print("Lahore is famous for its historical sites, vibrant culture, and amazing food.")

    @listen
    def default_response(self):
        """ Handles cases where classification fails """
        print("Sorry, I couldn't determine the city. Please try again.")

def kickoff():
    """ Starts the City Routing Workflow """
    obj = CityRoutingFlow()
    obj.kickoff()

def plot():
    """ Generates a visualization of the workflow """
    obj = CityRoutingFlow()
    obj.plot()
