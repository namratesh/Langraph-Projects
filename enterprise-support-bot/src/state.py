from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    original_query: str
    next_agent : str
    #billing fields
    refund_amount : Optional[float] = None
    refund_approved : bool = False
    #longe term memory
    user_info : Optional[Dict[str, Any]] = []
    #RAG Fields
    retervied_docs :List[Dict[str, Any]] = []
    