# Task description; priority and time bounds
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task that requires completion as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a medium priority task that should be done after all high priority time-bound tasks.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that requires attention today, but only after higher priorities.")
        else:
            print(f"Reminder: {task} is a low priority task to be done when no high or medium priority time-bound tasks remain.")
