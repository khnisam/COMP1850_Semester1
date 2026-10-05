"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")
try:
    place = int(destination)
    print("That is not a valid place.")
except ValueError:
    distance_miles_input = input("How many miles will you travel? ")
    try:
        distanceMiles = float(distance_miles_input)
        if distanceMiles > 0:
            time_hours_input = input("How many hours will the journey take? ")
            try:
                timeHours = int(time_hours_input)
                if timeHours > 0:
                    speed = distanceMiles/timeHours
                    print(f"Your average speed will be: {speed:.2f} mph.\n")
                    print(f"Your Destination will be: {destination}.")
                else:
                    print("Numerical value out of range.")
            except ValueError:
                print("That is not a number")
    except ValueError:
        print("That is not a valid number")






# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
