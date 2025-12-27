from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class DocumentState(BaseModel):
    original_text:str
    pii_flags: Optional[List[str]] = None
    polished_text: Optional[str]    = None
    final_output: Optional[str] = None
