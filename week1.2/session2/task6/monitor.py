# Week 1.2, Session 2: Task 6
menuCondition = True

while menuCondition == True:
    temperature = input("Enter the machine's temperature. ")
    pressure = input("Enter the machine's pressure. ")
    operationalStatus = input("Is the machine still operating? 1 for yes, 0 for no. ")
    try:
        machineTemp = int(temperature)
        machinePres = int(pressure)
        status = int(operationalStatus)
        tempStatus = "Default"
        presStatus = "Default"  
        if status == 1:
            if (machineTemp > 80):
                print("The machine's temperature is too high, please turn it off.")
                tempStatus = "High"
            elif (machineTemp <= 80) and (machineTemp >= 50):
                print("The machine is operating within normal conditions.")
                tempStatus = "Normal"
            elif (machineTemp < 50):
                print("The machine temperature is low, no action required.")
                tempStatus = "Low"
        elif status == 0: 
            if (machineTemp > 80):
                print("The machine's temperature is too high, please continue to keep it inactive.")
                tempStatus = "High"
            elif ((machineTemp <= 80) and (machineTemp >= 50)):
                print("The machine is operating within normal conditions and it is advised to begin running the machine.")
                tempStatus = "Normal"
            elif (machineTemp < 50):
                print("The machine temperature is low, no action required. It is safe to turn on. ")
                tempStatus = "Low"
        else:
            print("That is not a valid machine state. Please enter the values again.")

        if status == 1:
            if (machinePres > 100):
                print("The machine's pressure is too high, please turn it off and it will require maintenance.")
                presStatus = "High"
            elif (machinePres <= 100) and (machineTemp >= 70):
                print("The machine is operating within normal pressure conditions.")
                presStatus = "Normal" 
            elif (machinePres < 70):
                print("The machine pressure is low, no action required.")
                presStatus = "Low" 
        elif status == 0: 
            if (machinePres > 100):
                print("The machine's pressure is too high, please turn it off and it will require maintenance.")
                presStatus = "High" 
            elif ((machinePres <= 100) and (machineTemp >= 70)):
                print("The machine is operating within normal pressure conditions.")
                presStatus = "Normal" 
            elif (machinePres < 70):
                print("The machine pressure is low, no action required.")
                presStatus = "Low"
        else:
            print("That is not a valid machine state. Please enter the values again.")

        if status == 1:
            if (tempStatus == "High") or (presStatus == "High"):
                print("The machine is running at unsafe conditions, please shut it down. ")
            elif ((tempStatus == "Normal") or (tempStatus == "Low")) and ((presStatus == "Normal") or (presStatus == "Low")):
                print("Everything is running normally,")
        elif status == 0:
            print("The machine is not turned on yet, no action is required. ")
        else:
            print("Not a valid machine state.")
    except ValueError:
            print("Certain values that you have entered are not a numerical value. Please enter a valid set of numbers.")


    