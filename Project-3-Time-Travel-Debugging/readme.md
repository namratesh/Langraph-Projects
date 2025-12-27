# 🕰️ Project 3: Time Travel Debugging

**Goal**: Demonstrate **time travel** workflows using LangGraph's checkpointing capabilities. This project allows you to "time travel" to past states, inspect them, and even fork execution by updating the state.

## 📋 Project Overview
This project showcases how to use **MemorySaver** to persist the state of a graph at each step. This enables powerful debugging and interactive features:
*   **Checkpointing**: Automatically save the state after every node execution.
*   **Time Travel**: Rewind to a previous step in the graph's history.
*   **Forking**: Resume execution from a past state, potentially modifying the state (e.g., changing a user query) to explore a different path.

## 🖼️ Workflows
The project demonstrates two main workflows:

### Standard Flow
![Workflow](workflow.png)

### Time Travel / Intervention Flow
![Workflow 2](workflow2.png)

## ✨ Features
1.  **State Persistence**: Uses `MemorySaver` to store execution history.
2.  **History Inspection**: Inspect past snapshots of the graph state.
3.  **Intervention**: Manually update the state at a specific checkpoint and resume execution from there.

## 📂 Project Structure
*   `src/graph.py`: Defines the graph and enables `MemorySaver`.
*   `time_travel.py`: The main script demonstrating the "time travel" capability. It runs the graph, rewinds to a checkpoint, edits the query, and forks the execution.
*   `debug.py`: A script to run the graph and inspect the history and state snapshots.

## 🚀 How to Run

### 1. Run the Time Travel Demo
This script runs the graph naturally, pauses, finds a checkpoint, modifies the query, and resumes execution on a new branch.

```bash
python time_travel.py
```

### 2. Run the Debugger
This script runs the graph and then prints out the history of checkpoints for inspection.

```bash
python debug.py
```

## 📝 Example Output (`time_travel.py`)

```
--- 🎬 RUN 1: Original Timeline ---
...
---CHECK RELEVANCE---
-> Found irrelevant docs, filtering them out.
...
--- ⚡ INTERVENING: Changing Query ---
--- 🎬 RUN 2: New Timeline (Query: 'LangGraph is Awesome') ---
...
Node: rewrite_query
   -> Query in State: LangGraph is Awesome (refined)
...
```
