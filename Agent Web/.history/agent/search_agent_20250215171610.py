from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

class WebSearchAgent:
    def __init__(self, temperature=0.7):
        # Initialize the language model
        self.llm = ChatOpenAI(temperature=temperature)
        
        # Initialize search tool
        self.search_tool = DuckDuckGoSearchRun()
        
        # Create the agent
        self.agent = initialize_agent(
            tools=[self.search_tool],
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def search(self, query):
        """
        Execute a search query using the agent
        """
        try:
            response = self.agent.run(query)
            return response
        except Exception as e:
            return f"An error occurred: {str(e)}" 