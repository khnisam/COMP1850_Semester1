
import httpx
import pandas as pd
import matplotlib.pyplot as plt

api_key="7VN4D5YQECWFML98ZQEQVR5TT"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code (should be checked)
print(response.status_code)
status = response.status_code
if status == 200:
    print(response)
else:
    print("Error: ", status)

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']
temp_max = [day["tempmax"] for day in temp_data] #parses through the keys to obtain the values for the values of temp
temp_min = [day["tempmin"] for day in temp_data]
temp_average = [day["temp"] for day in temp_data]

temp_max_c = [(temp - 32) * 5/9 for temp in temp_max] #converts each temp category into celsius
temp_average_c = [(temp - 32) * 5/9 for temp in temp_average]
temp_min_c = [(temp - 32) * 5/9 for temp in temp_min]

print(temp_data)

# use pandas to convert data to  dataframe

df = pd.DataFrame({
    "Minimum": temp_min_c,
    "Average": temp_average_c,
    "Maximum": temp_max_c,

}) #initialises the data frame

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs

df.plot()
plt.xlabel("Day")
plt.ylabel("Temperature (Celsius)")

plt.show()

# annotate the graph with axis labels

# note that temperature is in Farenheit (F)
# convert to Celcius before plotting 

# using the documentation explore other data, eg. rainfall  
