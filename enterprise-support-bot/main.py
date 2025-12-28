from src.graph import app
from langchain_core.messages import HumanMessage

def run_chat(text: str, thread_id: str):
    print(f"\n\n{'='*50}")
    print(f"🚀 SCENARIO: '{text}' (Thread: {thread_id})")
    print(f"{'='*50}")

    config = {"configurable": {"thread_id": thread_id}}
    
    # 1. Start the Graph
    inputs = {"messages": [HumanMessage(content=text)], "original_query": text}
    
    # Run until completion OR interrupt
    for event in app.stream(inputs, config=config):
        for node, values in event.items():
            print(f"✅ Finished Node: {node}")
            # Optional: Print specific output to debug
            if "next_agent" in values:
                print(f"   -> Supervisor Routed to: {values['next_agent']}")
            if "refund_amount" in values:
                print(f"   -> Billing Amount: ${values['refund_amount']}")

    # 2. Check if we are Paused (Human-in-the-Loop)
    snapshot = app.get_state(config)
    
    if snapshot.next:
        print(f"\n✋ PAUSED at Node: {snapshot.next}")
        print("   -> Reason: High Value Refund detected.")
        
        # 3. Simulate Human Manager Approval
        user_input = input("   -> 👮 MANAGER: Approve refund? (type 'yes'): ")
        
        if user_input.lower() == "yes":
            print("\n▶️ RESUMING Graph...")
            
            # Resume with None (Proceed to Manager Node)
            for event in app.stream(None, config=config):
                for node, values in event.items():
                    print(f"✅ Finished Node: {node}")
        else:
            print("❌ Refund Rejected by Manager.")

if __name__ == "__main__":
    # --- SCENARIO A: Tech Support (Simple) ---
    run_chat("How do I fix error 505?", "thread_tech_1")
    
    # --- SCENARIO B: Low Refund (Auto-Approve) ---
    run_chat("Refund me $10 please.", "thread_bill_low")
    
    # --- SCENARIO C: High Refund (HitL Trigger) ---
    run_chat("I need a refund of $900 immediately.", "thread_bill_high")