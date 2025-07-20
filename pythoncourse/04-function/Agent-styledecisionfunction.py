def decide_action(state):
    if state == "error":
        return "handle_error"
    elif state == "done":
        return "shutdown"
    else:
        return "keep_working"

action = decide_action("error")
print("Agent will:", action)
