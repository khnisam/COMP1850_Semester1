"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)
   # httpx object, get() method, returns a response object

print(response.status_code)

if response.status_code == 200: #checks the status code, syntax .status_code obtains code. 

    print(f"{response.json()}\n")      # response object, json() method

else:
    print("Error:", response.status_code) #if code isn't 200 then print error. 
