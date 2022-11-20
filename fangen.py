#Are you a true Modern Family fan ? Take this quiz and find out!

print("So you say you're a modern family superfan? Well let's see about that!")
fav_char= str(input("Okay, who is your favorite character?  \n"))
if fav_char == "gloria" or fav_char == "Gloria" :
    print("Okay, lets see it you can answer the next question")
    exHus = input("Okay, what's her ex-husband's name?  \n")
    if exHus == "Javier Delgado" or exHus == "javier delgado" or exHus == "Javier" or exHus == "javier":
        print("correct!")
    else:
        print("ha! you're a fake fan !!!")
    known_for = input("Oh,Please. You guessed that one correctly. In one word, what is she known for?  \n")
    if known_for == "fashion" or known_for == "Fashion" :
        print("correct!")
    else:  
        print("You're a fake fan!")
elif fav_char == "Jay" or fav_char == "jay" or fav_char == "Jay Pritchett" or fav_char == "jay pritchett":
    print("Hmm, welldone")
    dog = input("So what is his dog's name?")
    if dog == "Stella" or "stella" :
        print("Yes!! You're a true fan") 
    else:
        print("Ha! you're a fake fan !!!")  
    child = input("And what's his first child's name?  \n")
    if child == "Claire" or child == "Claire Pritchett" or child == "Claire Dunphey" or child == "Claire Pritchett Dunphey" or child ==  "Claire Pritchett-Dunphey" :
        print("Yes!! welldone !!!")
    else:
        print("Ha! You're a fake fan!")
elif fav_char == "Cam" or fav_char == "Cameron" or fav_char == "Cameron Tucker Pritchett" or fav_char == "Cameron Tucker-Pritchett" : 
    work = input("What does he do before retirement  \n?")
    if work == "music" or work == "music teacher" or work == "He was a music teacher":
        print("Correct!")
    else:
        print("Ha! you're a fake fan ! ")
    marry = input("And who is he married to?")
    if marry == "mitch" or marry == "Mitch" or marry == "Mitchell Pritchett" or marry == "Mitchell Pritchett-Tucker" :
        print("yes! you got that right!")
    else:
        print("Ha! you're a fake fan !")
    father = str(input("And he is a father to who?"))
    if father == "Lily" or father == "lily" :
        print("Correct!")
    else:
        print("Ha! you're a fake fan!")
elif fav_char == "Phil" or fav_char == "Phil Dunphey" :
    wife= input ("Who is he married to?  \n")
    if wife == "Claire"  or "Claire Dunphey" : 
        print("Correct, you're a true fan!")
    else:
        print("Wrong !! It's Claire, Dummy!")
elif fav_char == "Phil" or fav_char == "Phil Dunphey" :
    college = input("what was he known for in college?   \n")
    if college == "Cheerleading" or college == "He was a Cheerleader":
        print("Correct!")
    else:
        print("Ha! you're a fake fan!")
elif fav_char == "Mitchel Tucker Pritchett" or fav_char == "mitch" or fav_char == "Mitch" or fav_char == "Mitchell"  :
    job = input("What does he do?")
    if job == "Lawyer" or job == "lawyer" or job == "Attorney"  or job == "attorney" or job == "he is a lawyer" : 
        print("Correct!")
    else:
        print("you're wrong, loser!")
else: 
    print("That's not a major character, Ha! you're a fake fan!!!")