from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class WebSearchAgent:
    def __init__(self, temperature=0.7):
        # Verify API key is set
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
            
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

# Test the agent if run directly
if __name__ == "__main__":
    agent = WebSearchAgent()
    result = agent.search("What is LangChain?")
    print(result) 