import keyboard
import time
import random

to_type = ["Hi Siya", "This is your computer speaking", "You have a virus :)", "I will go away if you go outside and yell \"YOUR MOM\"", "Look behind you", "You're super duper weird", "Your mom", "did you know that your mom"]

count = 0
while True:
	time.sleep(25)
	keyboard.write(" ")
	keyboard.write(to_type[random.randint(0, len(to_type))])
