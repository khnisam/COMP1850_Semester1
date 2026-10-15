# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

salesData = []
dateData = []
widgetData = []
widgets_sold = []
with open("sales.csv", "r") as file:
    for line in file:
        string = line.strip()
        if string == "Date,Product,Sales_Amount,Units_Sold,Region":
            continue
        else:
            data = line.strip().split(",")
            salesData.append(data[2])
            dateData.append(data[0])
            widgetData.append(data[1])
            widgets_sold.append(data[3])

sales = [int(x) for x in salesData]
units_sold = [int(x) for x in widgets_sold]
max_units_sold = max(units_sold)
indexList2 = units_sold.index(max_units_sold)
popular_widget = widgetData[indexList2]



maxSales = max(sales)
indexList = sales.index(maxSales)
maxSalesDay = dateData[indexList]

print(f"The highest sale day was {maxSalesDay}, with {maxSales} sales made.") #print the highest sale day
print(f"{popular_widget}, had {max_units_sold} units sold.")









            

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows