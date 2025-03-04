from crewai.flow.flow import Flow, start, listen

from dotenv import load_dotenv,  find_

CLASS PanaFlow(Flow):

@start
def generate_topic (self):
