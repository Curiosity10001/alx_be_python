#Task description; priority and time bounds
task = input ("Enter your task:")
priority = input ("Priority (high/medium/low)")
time_bound = input ("Is it time-bound? (yes/no)")

match priority :
    case "high" :
        if time_bound== "yes" : 
            print (f" {task} is a high priority task that requires immediate attention today!")
        else :
            print (f"{task} is a high priority task that requires completion as soon as possible")
    case "medium" :
        if time_bound== "yes" : 
            print (f" {task} is a medium priority task that requires immediate attention today!")
        else :
            print (f"{task} is a medium priority task that requires completion as soon as  no high priority and time bound tasks are done")
    case "low" :
        if time_bound== "yes" : 
            print (f" {task} is a low priority task that requires immediate attention today!")
        else :
            print (f"{task} is a low priority task that requires completion as soon as  no high and medium priority and time bound tasks are done")            
    