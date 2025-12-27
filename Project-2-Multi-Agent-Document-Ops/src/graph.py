from langgraph.graph import StateGraph, START, END
from src.nodes import check_pii, rewrite_text, merge_final_text
from src.state import DocumentState

workflow = StateGraph(DocumentState)
workflow.add_node("analyser", check_pii)
workflow.add_node("editor", rewrite_text)
workflow.add_node("manager", merge_final_text)

#edges
workflow.add_edge(START, "analyser")
workflow.add_edge(START, "editor")

workflow.add_edge("analyser", "manager")
workflow.add_edge("editor", "manager")
app = workflow.compile()