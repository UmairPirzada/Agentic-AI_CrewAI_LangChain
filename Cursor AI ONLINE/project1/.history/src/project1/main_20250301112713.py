from crewai.flow.flow import Flow, start, listen

from dotenv import load_dotenv,  find_dotenv

_:

CLASS PanaFlow(Flow):

@start
def generate_topic (self):
