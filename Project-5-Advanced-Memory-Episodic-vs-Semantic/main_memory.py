from src.graph import app

def run_chat(user_input, thread_id):
    print(f"\n--- 🏁 STARTING THREAD: {thread_id} ---")
    
    # Define the config for this specific conversation
    config = {"configurable": {"thread_id": thread_id}}
    
    # Correct Input Format: List of message dictionaries
    inputs = {
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    
    # Run the graph
    # We use .stream to see the nodes executing
    for output in app.stream(inputs, config=config):
        for key, value in output.items():
            print(f"Node '{key}' finished.")
            # Optional: Print response if available
            if "messages" in value and value["messages"]:
                last_msg = value["messages"][-1]
                # Handle both dict and object formats for safety
                content = last_msg.content if hasattr(last_msg, "content") else last_msg["content"]
                print(f"   -> Output: {content}")

if __name__ == "__main__":
    # --- TEST 1: TEACHING (Thread A) ---
    # User says their name. Agent should save it to 'profile_db'.
    run_chat("My name is Namratesh", "thread_A_session_1")

    print("\n\n" + "="*30 + "\n\n")

    # --- TEST 2: RECALLING (Thread B) ---
    # New conversation (New Thread ID). 
    # The Agent has NO chat history, but it should fetch facts from 'profile_db'.
    run_chat("Hello, who am I?", "thread_B_session_99")