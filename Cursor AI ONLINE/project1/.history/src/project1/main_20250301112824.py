from crewai.flow.flow import Flow, start, listen

from dotenv import load_dotenv,  find_dotenv

from litellm

_: bool = load_dotenv(find_dotenv())


CLASS PanaFlow(Flow):

@start
def generate_topic (self):
