from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = "AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M"

class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"role": "user", "content": "Return any random city name."}]
        )
        city = result["choices"][0]["message"]["content"]
        print(city)
        return city
        # print(result["choices"][0]["message"]["content"])
        

    @listen(generate_random_city)
    def generate_fun_fact(self,city_name)
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"role": "user", "content": f"write some fun fact about {city_name} city."}]
        )
        fun_fact = result["choices"][0]["message"]["content"]
        print(fun_fact)
        # return fun_fact
        state["fun_fact"] = 

def kickoff():
    obj = CityFunFact()
    obj.kickoff()      
