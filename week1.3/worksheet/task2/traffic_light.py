"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }


systime = 0
running_condition = True
state = "red"
maxtime = input()
try:
    TMax = int(maxtime)
    if TMax > 0:

        while running_condition:
            for key in states.keys():
                if (running_condition == True):
                    state = key
                    duration = states[state]
                    for count in range(duration):
                        print(f"Time {systime:03d} State {state}")
                        if systime == TMax:
                            running_condition = False
                            break
                        else:
                            systime = systime + 1
                else:
                    break

    else:
        print("Step must be greater than 0")

except ValueError:
    print("Not an integer")



    


        

                

            
            







# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14