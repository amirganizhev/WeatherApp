import pyowm

owm = pyowm.OWM('0489a7246fa2a2ee031b7a968af86b25' , language = "ru")

place = input("В каком городе хотите узнать погоду?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура в районе " + str(temp))

input()