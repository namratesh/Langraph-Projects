from typing import Dict, Any
from src.state import AgentState

def retrieve(state: AgentState) -> Dict[str, Any]:
    print(f"---RETRIEVE---")
    # Simulate fetching docs based on current query
    # In a real app, this calls the Vector DB
    return {"documents": state.documents}

def grade_documents(state: AgentState) -> Dict[str, Any]:
    print(f"---CHECK RELEVANCE---")
    
    # SIMULATION:
    # If the retry count is 0, simulate "Bad Docs" to force a loop.
    # If the retry count is > 0, simulate "Success" to exit the loop.
    if state.retry_count == 0:
        print("-> Found irrelevant docs, filtering them out.")
        return {"documents": []} # Empty list triggers the rewrite
    else:
        print("-> Docs are good now.")
        return {"documents": state.documents} # Keep docs

def rewrite_query(state: AgentState) -> Dict[str, Any]:
    print(f"---REWRITE QUERY---")
    
    current_count = state.retry_count
    new_count = current_count + 1
    
    # Update query to simulate improvement
    new_query = f"{state.query} (refined)"
    
    print(f"-> Incrementing retry count to: {new_count}")
    return {
        "query": new_query, 
        "retry_count": new_count
    }

def generate(state: AgentState) -> Dict[str, Any]:
    print(f"---GENERATE---")
    return {"final_answer": "This is the final generated answer."}