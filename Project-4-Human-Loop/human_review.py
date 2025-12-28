from src.graph import app

config = {"configurable": {"thread_id": "hitl_demo_1"}}
inputs = {
    "query": "Explain LangGraph", 
    "original_query": "Explain LangGraph",
    "documents": [],
    "retry_count": 0
}

print("--- 🏁 PHASE 1: Running until Blocked ---")
# This will run Retrieve -> Grade -> Rewrite... 
# BUT it will stop right before 'generate'
for output in app.stream(inputs, config=config):
    print(output)

print("\n--- ✋ GRAPH PAUSED ---")
print("The agent is waiting. We can inspect the state now.")

# Get current state
snapshot = app.get_state(config)
print(f"Next Node to run: {snapshot.next}")

# SIMULATE HUMAN INPUT
user_approval = input("Type 'yes' to approve, or type a new query to redirect: ")

if user_approval.lower() == "yes":
    print("--- ✅ APPROVED: Resuming ---")
    # Resume with None (just continue)
    for output in app.stream(None, config=config):
        print(output)
else:
    print(f"--- ✏️ EDITING: Changing query to '{user_approval}' ---")
    # Update state and resume
    app.update_state(config, {"query": user_approval})
    # We redirect to 'retrieve' to search for the NEW query
    # (Note: simpler logic would just edit the answer, but let's re-search)
    for output in app.stream(None, config=config):
        print(output)