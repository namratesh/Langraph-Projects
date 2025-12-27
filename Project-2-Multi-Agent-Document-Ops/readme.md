# 🚀 Project 2: Multi-Agent Document Ops

**Goal**: Demonstrate a "Fan-Out / Fan-In" architecture where multiple agents perform parallel tasks on a document before a manager merges the results.

## 📋 Project Overview
This project implements a multi-agent workflow for processing documents. It uses **LangGraph** to orchestrate independent agents that run in parallel:
1.  **Analyzer Agent**: Scans the text for PII (Personally Identifiable Information) like emails.
2.  **Editor Agent**: Polishes the text (e.g., converts to uppercase as a placeholder for complex editing).
3.  **Manager Agent**: Aggregates the results. If PII is found, it blocks the output. Otherwise, it publishes the polished text.

## 🤖 Agents & Workflow
The workflow follows a **Fan-Out / Fan-In** pattern:

1.  **Start**: The process begins with an `original_text`.
2.  **Fan-Out**:
    *   **Analyzer Node**: Checks `original_text` for PII (specifically looking for "@").
    *   **Editor Node**: Rewrites `original_text` (simulated by uppercasing).
3.  **Fan-In**:
    *   **Manager Node**: Waits for both Analyzer and Editor to finish. It checks the `pii_flags`.
        *   If **Safe**: Returns the `polished_text`.
        *   If **Unsafe**: Returns a blocked message.

## ✨ Features
*   **Parallel Execution**: Compliance checks and editing happen simultaneously for efficiency.
*   **Conditional Logic**: The final output depends on the result of the compliance check.
*   **State Management**: Uses a shared `DocumentState` to track `original_text`, `pii_flags`, `polished_text`, and `final_output`.

## 📂 Project Structure
*   `src/graph.py`: Defines the LangGraph workflow, nodes, and edges.
*   `src/nodes.py`: Contains the logic for the Analyzer, Editor, and Manager agents.
*   `src/state.py`: Defines the `DocumentState` Pydantic model.
*   `main.py`: Entry point to run the workflow and test different scenarios.

## 🚀 How to Run
Make sure you have the dependencies installed. Then run the main script:

```bash
python main.py
```

### Expected Output

**Test 1 (Safe Text):**
```
--- Testing: 'hello world' ---
...
RESULT: {'original_text': 'hello world', 'final_output': 'HELLO WORLD', ...}
```

**Test 2 (PII Detected):**
```
--- Testing: 'contact me at test@gmail.com' ---
...
RESULT: {'original_text': 'contact me at test@gmail.com', 'final_output': '⛔ BLOCKED: PII Detected', ...}
```