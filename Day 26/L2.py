#dictionary comprahension
#new_dict = {new_key : new value for (key, value) in dict.items() if test}


#to count no of letters in words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list = sentence.split()
word_count = {
    key:len(key) for key in list
}

print(word_count)


#converting temp using farahnite
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    key : (value * (9/5)) + 32 for (key, value) in weather_c.items()
}

print(weather_f)


