from langchain_core.tools import Tool
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai as genai
import time
from duckduckgo_search import DDGS

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class CustomDuckDuckGoSearchRun(DuckDuckGoSearchRun):
    def __init__(self, max_retries=3):
        super().__init__()
        self.max_retries = max_retries
    
    def _run(self, query: str) -> str:
        for attempt in range(self.max_retries):
            try:
                with DDGS() as ddgs:
                    results = list(ddgs.text(query, max_results=5))
                    if results:
                        return "\n\n".join(
                            f"Result {i+1}:\n{result['body']}"
                            for i, result in enumerate(results)
                        )
                    return "No results found."
            except Exception as e:
                if attempt == self.max_retries - 1:
                    return f"Search failed after {self.max_retries} attempts. Error: {str(e)}"
                time.sleep(2 ** attempt)  # Exponential backoff
        return "Search failed."

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
        
        # Initialize search tool with retry mechanism
        self.search_tool = CustomDuckDuckGoSearchRun(max_retries=3)
        
        # Create the agent
        self.agent = initialize_agent(
            tools=[self.search_tool],
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )
    
    def search(self, query):
        """
        Execute a search query using the agent
        """
        try:
            # Add a small delay before each search to avoid rate limiting
            time.sleep(1)
            response = self.agent.run(query)
            return response
        except Exception as e:
            error_msg = str(e)
            if "RateLimit" in error_msg:
                return "Search rate limit reached. Please try again in a few moments."
            return f"An error occurred: {error_msg}"

# Test the agent if run directly
if __name__ == "__main__":
    agent = WebSearchAgent()
    result = agent.search("What is LangChain?")
    print(result) 