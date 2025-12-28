from typing import Annotated, TypedDict, List, Union, Dict, Any
from langgraph.graph import END, StateGraph, START
from langgraph.checkpoint.memory import MemorySaver
from src.nodes import supervisor_node, tech_support_node, billing_node
from src.state import AgentState
from langchain_core.messages import SystemMessage

def execute_refund_node(state: AgentState):
    print("--- EXEC: Refund processed! ---")
    return {"messages": [SystemMessage(content="Refund Confirmed.")]}

def manager_approval_node(state: AgentState):
    # This node runs AFTER the human resumes the graph
    print("--- MANAGER: Approval Logged. ---")
    return {"refund_approved": True}

builder = StateGraph(AgentState)
#nodes
builder.add_node("SuperVisor", supervisor_node)
builder.add_node("Tech", tech_support_node)
builder.add_node("Billing", billing_node)
builder.add_node("Manager", manager_approval_node)
builder.add_node("Execute_Refund", execute_refund_node)

#edges
builder.add_edge(START, "SuperVisor")
def route_supervisor(state: AgentState):
    return state["next_agent"]
builder.add_conditional_edges("SuperVisor", route_supervisor, {
    "Tech": "Tech",
    "Billing": "Billing",
    "Finish": END
})
builder.add_edge("Tech", END)

def route_billing(state: AgentState):
    # Check the flag set by the Billing Node
    if state["refund_approved"] == False:
        return "Manager" 
    else:
        return "Execute" # Auto-approve

builder.add_conditional_edges(
    "Billing",
    route_billing,
    {
        "Manager": "Manager",
        "Execute": "Execute_Refund"
    }
)
builder.add_edge("Manager", "Execute_Refund")
builder.add_edge("Execute_Refund", END)
memory_saver = MemorySaver()

app = builder.compile(checkpointer=memory_saver,
interrupt_before = ['Manager'])
