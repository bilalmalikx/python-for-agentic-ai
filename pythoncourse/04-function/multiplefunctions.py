def analyze_query(query):
    if "weather" in query:
        return "search"
    elif "calculate" in query:
        return "math"
    else:
        return "chat"

def run_agent(query):
    task = analyze_query(query)

    if task == "search":
        return "Agent web search karega."
    elif task == "math":
        return "Agent calculation karega."
    else:
        return "Agent user se baat karega."

# Example
response = run_agent("what is the weather in Lahore?")
print(response)
