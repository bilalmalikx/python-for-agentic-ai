status = "in_progress"
attempts = 0

while status != "done" and attempts < 3:
    print("Agent is working...")
    attempts += 1
    if attempts == 2:
        status = "done"
