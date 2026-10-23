# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

with open("student_data.csv", "r") as infile:
    for line in infile:
        if line == "ID,Name,Mathematics,Science,History\n":
            continue
        else:
            string = line.strip().split(",")
            average = (int(string[2]) + int(string[3]) + int(string[4]))/3
            formatAverage = (f"{average:.2f}")
            name = string[1]
            with open("report.txt", "a") as outfile:
                outfile.write(f"Name: {name} | Average Grade: {formatAverage}\n")







# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
