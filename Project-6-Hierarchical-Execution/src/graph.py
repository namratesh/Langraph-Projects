from langgraph.graph import StateGraph, END, START
from src.state import AgentState
from src.nodes import supervisor_node, research_agent, math_agent

# 1. Init
workflow = StateGraph(AgentState)

# 2. Add Nodes
workflow.add_node("Supervisor", supervisor_node)
workflow.add_node("Search", research_agent)
workflow.add_node("Math", math_agent)

# 3. Entry
workflow.add_edge(START, "Supervisor")

# 4. The Routing Logic
def route_supervisor(state: AgentState):
    # This reads the 'next' key set by the Supervisor node
    return state["next"]

workflow.add_conditional_edges(
    "Supervisor",
    route_supervisor,
    {
        "Search": "Search",
        "Math": "Math",
        "FINISH": END
    }
)

# 5. Workers go to END (Single Turn)
workflow.add_edge("Search", END)
workflow.add_edge("Math", END)

# 6. Compile
app = workflow.compile()