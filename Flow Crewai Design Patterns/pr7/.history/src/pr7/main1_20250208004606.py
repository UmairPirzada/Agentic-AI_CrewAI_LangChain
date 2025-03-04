from crewai.flow.flow import Flow, start, listen
from litellm import completion

class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        result = completion

API_KEY = AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M
# gemini-1.5-flash
# AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M