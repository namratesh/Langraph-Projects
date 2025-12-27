from src.graph import app

# 1. Define the Configuration (The Session ID)
config = {"configurable": {"thread_id": "debugging_session_1"}}

# 2. Initial Input
inputs = {
    "query": "What is LangGraph?",
    "original_query": "What is LangGraph?",
    "documents": [],
    "retry_count": 0
}

# 3. Run the Graph
print("--- RUN 1: Normal Execution ---")
for output in app.stream(inputs, config=config):
    for key, value in output.items():
        print(f"Finished Node: {key}")

# 4. INSPECT MEMORY (Time Travel Prep)
print("\n--- INSPECTING STATE ---")
snapshot = app.get_state(config)
print(f"Current State at End: {snapshot.values['retry_count']}")

# 5. VIEW HISTORY
print("\n--- BROWSING HISTORY ---")
# This lists all the snapshots saved in this thread
for state in app.get_state_history(config):
    # print(state.values)
    if state.values:
        print(f"Step Config: {state.config}")
        print(f" - Retry Count: {state.values['retry_count']}")
        print("---")