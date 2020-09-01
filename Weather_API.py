import json, requests


api_key = 'Your API Key'
  

base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = input("Enter city name : ") 
  

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
response.raise_for_status()
x = json.loads(response.text)  
y = x["main"] 
#change Kelvin to Celcius
current_temperature = y["temp"] - 273.15
current_pressure = y["pressure"] 
current_humidiy = y["humidity"] 
# store the value of "weather" in z
# z is now list with 0th item only. We need to extract 0th item and store in p
#p is now a new dict, to get the value of descirption we store it in s
z = x["weather"] 
p = z[0]
s = p['description']
# print following values 
print(" Temperature (in Celcius) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    s) 
