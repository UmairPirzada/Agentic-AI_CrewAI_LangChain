def format_search_results(results):
    """
    Format search results for better display
    """
    if isinstance(results, str):
        return results
    
    formatted_results = ""
    for idx, result in enumerate(results, 1):
        formatted_results += f"### Result {idx}\n{result}\n\n"
    
    return formatted_results 