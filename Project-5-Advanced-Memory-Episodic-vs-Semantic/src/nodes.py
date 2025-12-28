from typing import Dict, Any, List
from langgraph.graph import MessagesState
from src.memory_store import profile_db  # Import our DB

# Note: We use 'MessagesState' which is a built-in TypedDict for chat
# It has a key 'messages': List[BaseMessage]

def recall_profile(state: MessagesState) -> Dict[str, Any]:
    # 1. Get User ID (In prod, this comes from config)
    user_id = "user_123" 
    
    # 2. Fetch from Long-Term Memory
    facts = profile_db.get_facts(user_id)
    
    if facts:
        print(f"--- 🧠 RECALLING: Found {len(facts)} facts about user ---")
        # We inject these facts into the context as a System Message
        system_msg = f"User Profile: {', '.join(facts)}"
        # We perform a trick: Prepend this to messages (conceptually)
        # For this node, we just print it to prove we have it.
        return {"messages": []} # No state change for now, just side effect
    else:
        print("--- 🧠 RECALLING: New User (No facts) ---")
        return {"messages": []}

def converse(state: MessagesState) -> Dict[str, Any]:
    # Extract the last user message
    last_msg = state["messages"][-1].content
    print(f"--- 🗣️ CONVERSING: User said '{last_msg}' ---")
    
    # Simple keyword detection for memory
    # In real life, an LLM decides this
    response = "I processed that."
    
    if "my name is" in last_msg.lower():
        # Trigger memory save logic
        return {"messages": [{"role": "assistant", "content": "Nice to meet you! I'll remember that."}]}
    
    return {"messages": [{"role": "assistant", "content": response}]}

def save_memory(state: MessagesState) -> Dict[str, Any]:
    # Check if we need to save anything
    last_user_msg = state["messages"][-2].content # -1 is AI response, -2 is User
    
    if "my name is" in last_user_msg.lower():
        name = last_user_msg.split("is")[-1].strip()
        user_id = "user_123"
        
        print(f"--- 📝 MEMORY AGENT: Saving '{name}' to DB ---")
        profile_db.save_fact(user_id, f"Name is {name}")
        
    return {"messages": []}