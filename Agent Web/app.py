import streamlit as st
from agent.search_agent import WebSearchAgent
from utils.search_tools import format_search_results
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Web Search Assistant",
    page_icon="🔍",
    layout="wide"
)

def initialize_session_state():
    if "search_agent" not in st.session_state:
        st.session_state.search_agent = WebSearchAgent()
    if "search_history" not in st.session_state:
        st.session_state.search_history = []
    if "last_search_time" not in st.session_state:
        st.session_state.last_search_time = 0

def main():
    initialize_session_state()
    
    # Header
    st.title("🔍 AI Web Search Assistant")
    st.markdown("""
    Your intelligent search companion powered by AI. Ask anything!
    """)
    
    # Search interface
    search_query = st.text_input("Enter your search query:", 
                                placeholder="e.g., Find the best video for MLOps and explain its key points")
    
    if st.button("Search"):
        if search_query:
            # Check if enough time has passed since last search
            current_time = time.time()
            if current_time - st.session_state.last_search_time < 2:
                st.warning("Please wait a moment before searching again.")
            else:
                with st.spinner("Searching..."):
                    # Execute search
                    results = st.session_state.search_agent.search(search_query)
                    
                    # Update last search time
                    st.session_state.last_search_time = current_time
                    
                    # Display results
                    st.markdown("### Search Results")
                    st.markdown(format_search_results(results))
                    
                    # Add to history
                    st.session_state.search_history.append({
                        "query": search_query,
                        "results": results
                    })
    
    # Display search history
    if st.session_state.search_history:
        st.markdown("### Search History")
        for idx, item in enumerate(reversed(st.session_state.search_history)):
            with st.expander(f"Search {len(st.session_state.search_history) - idx}: {item['query'][:50]}..."):
                st.markdown(format_search_results(item['results']))

if __name__ == "__main__":
    main() 