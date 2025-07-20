def decide_next_step(step_count):
    if step_count >= 3:
        return "done"
    return "continue"

step = 0

while True:
    print("Agent planning...")
    status = decide_next_step(step)
    if status == "done":
        print("Agent ne kaam complete kar liya.")
        break
    step += 1
