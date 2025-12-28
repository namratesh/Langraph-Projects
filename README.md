# 🦜🕸️ LangGraph Projects Collection

This repository contains a collection of **6 distinct projects** demonstrating various capabilities and patterns of **LangGraph**, a library for building stateful, multi-actor applications with LLMs. Each project focuses on a specific architectural pattern or feature.

## 📂 Project Index

### [1. Stateful RAG (Self-Correcting)](./Project-1-stateful-rag)
*   **Concept**: Retrieval-Augmented Generation (RAG) with a feedback loop.
*   **Key Features**:
    *   **Self-Correction**: Evaluates retrieved documents for relevance.
    *   **Query Rewriting**: If documents are irrelevant, the agent rewrites the query and retries.
    *   **Hallucination Check**: Verifies that the generated answer is grounded in the documents.

### [2. Multi-Agent Document Ops (Fan-Out/Fan-In)](./Project-2-Multi-Agent-Document-Ops)
*   **Concept**: Parallel execution of multiple specialist agents.
*   **Key Features**:
    *   **Fan-Out**: An "Analyzer" agent (checks PII) and an "Editor" agent (formats text) run simultaneously.
    *   **Fan-In**: A "Manager" agent waits for both results and aggregates them, blocking output if PII is detected.

### [3. Time Travel Debugging](./Project-3-Time-Travel-Debugging)
*   **Concept**: leveraging LangGraph's checkpointing for advanced debugging.
*   **Key Features**:
    *   **Checkpointing**: Saves the graph state after every step.
    *   **Time Travel**: Allows rewinding to a previous state in the execution history.
    *   **Forking**: Resume execution from a past state with modified inputs (e.g., changing a user query mid-flight).

### [4. Human-in-the-Loop](./Project-4-Human-Loop)
*   **Concept**: Integrating human approval and intervention into the graph.
*   **Key Features**:
    *   **Breakpoints**: The graph pauses before sensitive actions (e.g., executing a tool or generating a final answer).
    *   **State Editing**: A human can inspect the current state and modify it (e.g., editing a draft response) before approving the graph to continue.

### [5. Advanced Memory (Episodic vs. Semantic)](./Project-5-Advanced-Memory-Episodic-vs-Semantic)
*   **Concept**: Differentiating between short-term conversation context and long-term knowledge.
*   **Key Features**:
    *   **Short-term Memory**: Standard thread-based persistence for the current conversation.
    *   **Long-term Memory**: A "Profile" database that persists facts about the user across different conversation threads.

### [6. Hierarchical Execution (Supervisor)](./Project-6-Hierarchical-Execution)
*   **Concept**: Managing complex tasks with a Supervisor-Worker architecture.
*   **Key Features**:
    *   **Supervisor Node**: An LLM routing node that breaks down tasks and delegates them to specific workers.
    *   **Worker Agents**: Specialized agents (e.g., "Search", "Math") that perform sub-tasks and report back to the supervisor.
    *   **Orchestration**: The supervisor coordinates the workflow until the user's request is fully satisfied.

## 🚀 Getting Started

Each project is self-contained in its own directory. To run a project:

1.  Navigate to the project folder:
    ```bash
    cd Project-X-Name
    ```
2.  Install the dependencies (ensure you have the necessary API keys set up, e.g., `OPENAI_API_KEY`, `TAVILY_API_KEY`):
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the entry point (usually `main.py` or `graph.py`):
    ```bash
    python main.py
    ```

---
*Built with [LangGraph](https://github.com/langchain-ai/langgraph)*
