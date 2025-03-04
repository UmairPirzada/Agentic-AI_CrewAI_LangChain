from langchain_core.tools import Tool
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class WebSearchAgent:
    def __init__(self, temperature=0.7):
        # Verify API key is set
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
        # Initialize the language model
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=temperature,
            convert_system_message_to_human=True
        )
        
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