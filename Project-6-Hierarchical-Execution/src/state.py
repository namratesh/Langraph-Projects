from typing import Annotated, TypedDict, List, Literal, Union
from langgraph.graph import MessagesState
import operator

# We extend the standard MessagesState
class AgentState(MessagesState):
    # The 'next' field will store the name of the node to route to
    # It can be 'Search', 'Math', or 'FINISH'
    next: str