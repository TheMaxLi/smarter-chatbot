# this is a more advanced chat bot that responds
# based on your answers
# computer science 10


import random
response = ""

good_response = ["Awesome!, me too", "That's great, let's go somewhere", "Cool! I'm glad"]
bad_response = ["Well that's alright, let's make it better!", "It's okay, let's do something fun!", "I'll make it better, just you watch"]

print ("how was your day? ")
response = input()
if response == "good" or response == "Good":
    print(random.choice(good_response))
if response == "bad" or response == "Bad":
    print(random.choice(bad_response))

good_food = ["Im glad, me too","Can I try?","sounds good!!"]
bad_food = ["That sucks then","let me try","i'll give you my food"]

print ("how is the food?" )
response = input()
if response == "good" or response == "Good":
    print(random.choice(good_food))
if response == "bad" or response == "Bad":
    print(random.choice(bad_food))

good_day = ["you better have!","im glads!","woooO!!!!"]
bad_day = ["bruh","oh well i tried","wow"]

print ("how was today after that experience?")
response = input()
if response == "good" or response == "Good":
    print(random.choice(good_day))
if response == "bad" or response == "Bad":
    print(random.choice(bad_day))