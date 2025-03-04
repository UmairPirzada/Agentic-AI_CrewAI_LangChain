from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv,  find_dotenv
from litellm import completion

_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):

    @start()
    def generate_topic (self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                
                {"role": "user",
                 "content": "Share the most trending topic for 2025"
                 }
            ],

            # max_tokens=100,
            # temperature=0.5,
      
        )
        self.state["topic"] = response['choices'][0]['message']['content']

        print(f"Step 1 Topic: {self.state['topic']}")


def kickoff();
flow = PanaFlow()
response = flow.kickoff()
print("RESPONSE", response)

if __name__ == "__main__":
    print("To test your plugin first, run the Python file directly from the command line")
    p = Plugin()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parameter = {
        "file": os.path.join(dir_path, "Example.csv")
    }
    print("\n %s" % p.read_store(parameter))
    print("\nChannel length: %s" % p.read_channel_length(0, 0))
    print("\nChannel values: %s" % p.read_channel_values(0, 0, 0, 1024))