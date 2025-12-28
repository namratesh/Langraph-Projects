from typing import Dict, Any, Literal
from src.state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage

# --- THE WORKERS ---

def research_agent(state: AgentState) -> Dict[str, Any]:
    print("--- 🕵️ RESEARCHER: Looking up info... ---")
    # Simulate work
    last_message = state["messages"][-1].content
    result = f"Search Results for '{last_message}': It is a tech topic."
    
    return {
        "messages": [SystemMessage(content=result)]
    }

def math_agent(state: AgentState) -> Dict[str, Any]:
    print("--- 🧮 MATH ANALYST: Calculating... ---")
    # Simulate work
    return {
        "messages": [SystemMessage(content="The calculated answer is 42.")]
    }

# --- THE BOSS (Supervisor) ---

def supervisor_node(state: AgentState) -> Dict[str, Any]:
    print("--- 👨‍✈️ SUPERVISOR: Deciding who acts next... ---")
    
    last_user_msg = state["messages"][-1].content.lower()
    
    # Simple Router Logic (In prod, use an LLM here)
    if "calculate" in last_user_msg or "math" in last_user_msg:
        next_node = "Math"
    elif "search" in last_user_msg or "who" in last_user_msg:
        next_node = "Search"
    else:
        next_node = "FINISH"
        
    print(f"   -> Routing to: {next_node}")
    return {"next": next_node}