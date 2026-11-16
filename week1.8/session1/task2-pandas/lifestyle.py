import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(type(data)) #outputs a class 'DataFrame'
print(data)

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students

print(data.shape) #.shape gives (rows, columns)
print(data.shape[0]) #this selects the row element in the tuple

# Find the mean average GPA of the students

print(data["GPA"]) #prints out the column GPA.
print(data["GPA"].mean()) #prints out the average GPA, based on the given column

# Find the standard deviation of how much sleep students get per day

print(data["Sleep_Hours_Per_Day"])
print(data["Sleep_Hours_Per_Day"].std()) #prints out the STDEV of the given column in the data frame. 

# Find the maximum amount of study hours per day

print(data["Study_Hours_Per_Day"].max()) #prints out the max value in the given column.

# Sort the students by social hours per day ascending (lowest -> highest)

sort = data.sort_values(by="Social_Hours_Per_Day", ascending=True) #this sorts the given column
print(sort)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

hours_columns = ["Study_Hours_Per_Day", "Extracurricular_Hours_Per_Day", "Sleep_Hours_Per_Day", "Social_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"] #this selects all the columns in the dataframe.
data["Total_Hours"] = data[hours_columns].sum(axis=1)
#axis = 1 sums across columns for each row, whereas axis = 0 sums down the columns for each row. 
print(data["Total_Hours"])

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.

high_stress_students = data[data["Stress_Level"] == "High"] #filters out any low stress students using pandas's conditional statement.
low_stress_students = data[data["Stress_Level"] == "Low"] #vice versa
print(high_stress_students) #prints out, for example, the high stress students.


# Can you work out whether having a higher stress level leads to a higher GPA?

print(high_stress_students["GPA"].mean()) #calcs. the mean of both levels, to determine the gpa of both. 
print(low_stress_students["GPA"].mean())
#in this case high level stress students have, on average, a higher GPA. 