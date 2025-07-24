#install an external module and use it to perform an operation of your choice
#step 1: open terminal , pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("i can speak what you write ?")
engine.runAndWait()

#it will speak what we write in "engine.say"