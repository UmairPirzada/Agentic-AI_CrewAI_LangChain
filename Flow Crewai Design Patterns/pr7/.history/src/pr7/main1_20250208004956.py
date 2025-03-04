from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = "AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M"

class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        result = completion(
            model ="gemini/gemini-1.5-flash",
            api_key = API_KEY,
            messages = [{"content":"Return any random city name."}]
        )
        print(result["choices"][])

# API_KEY = AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M
# gemini-1.5-flash
# AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M