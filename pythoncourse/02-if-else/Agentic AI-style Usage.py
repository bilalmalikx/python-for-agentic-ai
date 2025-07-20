def router(state):
    if "search" in state["task"]:
        return "search_node"
    elif "math" in state["task"]:
        return "math_node"
    elif "summarize" in state["task"]:
        return "summarizer_node"
    else:
        return "default_node"
