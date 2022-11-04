# Python Module Bonus assignment
# Create a python application that takes an input request of a city and displays 
# the current weather for that city. Based on the temperature returned determine if the 
# user making input should wear a coat (a temperature of 65 degrees or lower) or if they
# are safe to wear shorts ( a temperature of 66 degrees of higher).

# Points Breakdown
# 1 Point for even attempting
# 1 Point for successful API call
# 1 point for parsing the data 
# 1 point for conditional implementation ( wear a coat/ wear shorts)
# 1 point for correct output decision

import requests, json

# api key and base url provided in assignment
your_api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# promp user for city location
city_entered = input("enter your city \n")

# quantified url for api call provided in assignment
# added units=imperial to end of url to convert units to farenheight rather than kelvin
quantified_url = base_url + "appid=" + your_api_key + "&q=" + city_entered + "&units=imperial"

# make our api call using requests.get() and our quantified url
response = requests.get(quantified_url)
#print(response)

# convert api response to json format
# parse data to get required info
raw_data = response.json()
# print(raw_data)
current_weather = raw_data["main"]
# print(current_weather)
temp = current_weather["temp"] 
print("Current temperature is " + str(temp) + "F")

# implement conditional
# Should user wear a coat?
if temp <= 65:
    print("wear a coat!")
if temp > 65:
    print("wear shorts!")