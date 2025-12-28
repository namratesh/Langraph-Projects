from langgraph.graph import StateGraph, END, START, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from src.nodes import recall_profile, converse, save_memory

workflow = StateGraph(MessagesState)

workflow.add_node("recall", recall_profile)
workflow.add_node("converse", converse)
workflow.add_node("save", save_memory)

workflow.add_edge(START, "recall")
workflow.add_edge("recall", "converse")
workflow.add_edge("converse", "save")
workflow.add_edge("save", END)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)