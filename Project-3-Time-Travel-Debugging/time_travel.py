from src.graph import app

# 1. Setup the session
config = {"configurable": {"thread_id": "time_travel_demo_1"}}

# 2. Run initial bad path (Force a failure/retry)
print("--- 🎬 RUN 1: Original Timeline ---")
initial_input = {
    "query": "Impossible Query", 
    "original_query": "Impossible Query",
    "documents": [],
    "retry_count": 0
}
# Run strictly until the end
list(app.stream(initial_input, config=config))


# 3. Browse History to find the "Before Rewrite" moment
# We look for the snapshot where the next step was going to be 'rewrite_query'
print("\n--- ⏳ SEARCHING FOR CHECKPOINT ---")
all_states = list(app.get_state_history(config))

# In your logs, the state *before* rewrite has retry_count=0
target_state = None
for state in all_states:
    # We want the moment where we just finished 'grade_documents' 
    # and were about to retry.
    if state.values['retry_count'] == 0 and state.next == ('rewrite_query',):
        target_state = state
        break

if not target_state:
    print("❌ Could not find the specific checkpoint. Check your logic.")
    exit()

print(f"-> Found Checkpoint ID: {target_state.config['configurable']['checkpoint_id']}")


# 4. ALTER REALITY (The Fork)
# We update the state at that specific past moment.
# This creates a NEW branch in the history tree.
print("\n--- ⚡ INTERVENING: Changing Query ---")
new_query = "LangGraph is Awesome"


new_config = app.update_state(
    target_state.config,
    {"query": new_query} 
)

# 5. RESUME EXECUTION
# Notice inputs=None. It resumes from the saved point.
print(f"--- 🎬 RUN 2: New Timeline (Query: '{new_query}') ---")
for output in app.stream(None, config=new_config):
    for key, value in output.items():
        print(f"Node: {key}")
        # Verify the agent is using the NEW query
        if "query" in value:
            print(f"   -> Query in State: {value['query']}")