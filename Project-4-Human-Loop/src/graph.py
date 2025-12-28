from langgraph.graph import StateGraph, END, START
from src.state import AgentState
from src.nodes import retrieve, grade_documents, rewrite_query, generate
from typing import Dict, Any
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
workflow = StateGraph(AgentState)
#nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents) 
workflow.add_node("rewrite_query", rewrite_query)
workflow.add_node("generate", generate)
#edges
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
#conditional edge
def decide_to_generate(state: AgentState) -> Dict[str, Any]:
    if state.retry_count >= 3:
        return "end_max_retries"
    elif state.needs_rewrite:
        return "rewrite"
    else:
        return "generate"
workflow.add_conditional_edges("grade_documents", decide_to_generate, {
        "rewrite": "rewrite_query",   
        "generate": "generate",       
        "end_max_retries": END        
    })

workflow.add_edge("rewrite_query", "retrieve") 
workflow.add_edge("generate", END)




app = workflow.compile(checkpointer=memory, interrupt_before=["generate"])