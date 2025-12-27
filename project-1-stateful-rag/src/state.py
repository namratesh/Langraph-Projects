from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class AgentState(BaseModel):
    query: str
    original_query: str
    documents: List[Dict[str, Any]]
    relevance_score: Optional[List[float]] = None 
    final_answer: Optional[str] = None
    retry_count: int = 0