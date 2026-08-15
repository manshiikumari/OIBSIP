import requests

print("Weather App")

api_key = input("Enter your OpenWeatherMap API key: ")
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\nWeather Information")
        print("-------------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition)
        print("Wind Speed:", wind_speed, "m/s")

    elif response.status_code == 404:
        print("City not found. Please check the city name.")

    elif response.status_code == 401:
        print("Invalid API key. Please check your API key.")

    else:
        print("Unable to get weather information.")

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")

except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")