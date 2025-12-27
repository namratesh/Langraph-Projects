from src.state import DocumentState
from typing import Dict, Any, List

# --- Node 1: Analyzer ---
async def check_pii(state: DocumentState) -> Dict[str, Any]:
    print("--- 🔍 Checking PII ---")
    
    # Use ['key'] to read
    if "@" in state.original_text:
        print("   -> PII Detected")
        # Use string "key" to write
        return {"pii_flags": ["email"]} 
    else:
        print("   -> No PII")
        return {"pii_flags": []}

# --- Node 2: Editor ---
async def rewrite_text(state: DocumentState) -> Dict[str, Any]:
    print("--- ✍️ Rewriting Text ---")
    
    if state.original_text:
        print("   -> Text Rewritten")
        return {"polished_text": state.original_text.upper()}
    
    print("   -> Text Not Rewritten")
    return {"polished_text": "ERROR"}

# --- Node 3: Manager ---
async def merge_final_text(state: DocumentState) -> Dict[str, Any]:
    print("--- 👩‍💼 Merging Final Text ---")
    
    # 1. READ inputs
    # We use .get() to avoid errors if keys don't exist yet
    pii = state.pii_flags
    polished = state.polished_text

    # 2. ENFORCE Compliance
    if pii:
        print("   -> ⛔ BLOCKED due to PII")
        return {"final_output": "BLOCKED: PII Detected"}
    
    # 3. Publish
    print("   -> ✅ Published")
    return {"final_output": polished}