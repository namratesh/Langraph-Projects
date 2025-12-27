from src.graph import app

if __name__ == "__main__":
    inputs = {
        "query": "What is LangGraph?",
        "original_query": "What is LangGraph?",
        "documents": [{"page_content": "doc1"}, {"page_content": "doc2"}, {"page_content": "doc3"}],
        "retry_count": 0
    }
    
    # Run the graph
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Node '{key}':")
            # print(value) # Optional: print state updates