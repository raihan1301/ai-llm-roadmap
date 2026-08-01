emoticon = "raihan"

def main():

    global emoticon   #this will call the top emoticon
    say("Is anyone there?")
    emoticon = "no one"
    say("did you see anyone?")

def say(phrase):
    print(phrase + " "+ emoticon)

main()