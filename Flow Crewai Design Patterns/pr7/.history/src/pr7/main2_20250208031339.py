from crewai.flow.flow import Flow, start, listen, router
from litellm import completion

API_KEY = "your-api-key-here"

class CityRoutingFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam-o-Alaikum! Let's explore fun facts about a city.")

    @router(greeting)
    def classify_city(self):
        """ Uses an LLM to classify which city should be routed. """
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"role": "user", "content": "Pick a random city from Karachi, Islamabad, or Lahore."}]
        )
        
        selected_city = response["choices"][0]["message"]["content"].strip().lower()

        if "karachi" in selected_city:
            return self.karachi_facts
        elif "islamabad" in selected_city:
            return self.islamabad_facts
        elif "lahore" in selected_city:
            return self.lahore_facts
        else:
            print("Unknown city. Defaulting to Karachi.")
            return self.karachi_facts

    @listen
    def karachi_facts(self, city):
        print(f"Karachi is the financial hub of Pakistan and home to the largest port in the country.")

    @listen
    def islamabad_facts(self, city):
        print(f"Islamabad is Pakistan's capital, known for its scenic beauty and modern infrastructure.")

    @listen
    def lahore_facts(self, city):
        print(f"Lahore is famous for its historical sites, vibrant culture, and amazing food.")

def kickoff():
    obj = CityRoutingFlow()
    obj.kickoff()   

def plot():
    obj = CityRoutingFlow()
    obj.plot()   
