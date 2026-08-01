import cowsay
import pyttsx3

engine = pyttsx3.init()

message  = "I love you Muskan very much. I want to be with you forever"

cowsay.cow(message)
engine.say(message)
engine.runAndWait()