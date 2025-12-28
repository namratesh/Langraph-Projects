from src.graph import app
from langchain_core.messages import HumanMessage

def run_query(text):
    print(f"\n--- Testing Query: '{text}' ---")
    inputs = {"messages": [HumanMessage(content=text)]}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Finished: {key}")

if __name__ == "__main__":
    # Test 1: Should go to Search
    run_query("Who is the president?")
    
    # Test 2: Should go to Math
    run_query("Calculate 55 + 10 math")
    
    # Test 3: Should End (Supervisor handles it)
    run_query("Hello there")