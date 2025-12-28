from src.state import AgentState
from typing import Dict, Any, List
from langchain_core.messages import SystemMessage
import re

def supervisor_node(state: AgentState) -> Dict[str, Any]:
    print(f'Running supervisor agent for query: {state['original_query']}')
    query = state['original_query'].lower()
    if any(word in query for word in ["refund", "money"]) :
        print("   -> Routing to BILLING")
        return {
        "next_agent" : "Billing"
    }
    elif any(word in query for word in ["how", "what", "where", "when", "why", "who"]) :
        print("   -> Routing to TECH")
        return {
        "next_agent" : "Tech"
    }
    else:
        print("   -> Routing to FINISH")
        return {
        "next_agent" : "Finish"
    }

def billing_node(state: AgentState) -> Dict[str, Any]:
    print(f'Running billing agent for query: {state['original_query']}')
    query = state['original_query'].lower()
    amounts = re.findall(r'\d+', query)
    if amounts:
        amount = float(amounts[0])
    else:
        amount =0.0
    print(f'Total amount deducted: {amount}')
    if amount > 50:
        print('Amount is greater than $50, Flagging for human review')
        return {
            "refund_amount" :amount,
            "refund_approved" :False,
            "messages": [SystemMessage(content=f"Refund request of ${amount} requires manager approval.")]

        }
    else:
        print("   -> Auto-Approving refund.")
        return {
            "refund_amount": amount,
            "refund_approved": True,
            "messages": [SystemMessage(content=f"Refund of ${amount} processed successfully.")]
        }
            

def tech_support_node(state: AgentState) -> Dict[str, Any]:
    print("--- 🛠️ TECH AGENT: Searching Manuals ---")
    
    # Mock RAG response
    return {
        "messages": [SystemMessage(content="To fix the error, try restarting your router and clearing the cache.")]
    }