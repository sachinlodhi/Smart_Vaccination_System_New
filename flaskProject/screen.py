# Module for the for displaying current token number
# Use this one

import time
from os import system
import pyfiglet
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 120)
def show_token():
    file = open("temp.txt", "r")
    token = file.read()
    file.close()
    res = pyfiglet.figlet_format(f"Token No : {str(int(token) )}")
    print(res)
    # engine.say(f"Token Number {str(int(token))} Please Reach at counter.")
    engine.runAndWait()
    time.sleep(1)
    system("cls")

while True:
    show_token()


