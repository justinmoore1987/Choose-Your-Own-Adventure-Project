import time,os,sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
        
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    value = input()
    return value

def clearScreen():
    os.system("clear")

#GREET USER AND PROVIDE INSTRUCTIONS.................................................
typingPrint("Greetings! And welcome to your lucky day! Today you have been chosen to be one of the few selected to win a Brand New Super Computer! Provided by one of the top competiting brands!")
typingPrint("\nAll you need to do today is answer a few questions and follow 1 simple rule in order to receive your free Super Computer!")
typingPrint("\nThe questions are simple and are meant just to verify your identity so we can make sure we are sending the gift to the correct person!")
typingPrint("\nThe one thing you must make sure to do is this, once you finish responding to the question, make sure you hit the 'ENTER' or 'RETURN' key to submit your response")
typingInput("\nNow, let us not waste any more time! Please hit 'ENTER' to continue...")

#CHECKPOINT SPOT FOR THE STORY TO RESTART..................................................
keepGoing = "yes"
while keepGoing.lower() == "yes":
   
        #5 QUESTIONS FOR THE USER.
        firstName = typingInput("\nPlease verify your First Name:  ")
        while (len(firstName) == 0):
            firstName = typingInput(f"Invalid entry, pleasae enter First Name:  ")
        
        birthDate = date_entry = typingInput("\nWhat is your Date of Birth? Please enter the date using the format MM/DD/YYYY:  ")
        while (len(birthDate) == 0):
            birthDate = typingInput("Invalid Entry, please do not leave blank. Please enter your Date of Birth, using MM/DD/YYYY:  ")
                
        addressCity = typingInput("\nIn what city do you live in:  ")
        while (len(addressCity) == 0):
            addressCity = typingInput("\nInvalid Entry, please do not leave blank! Enter the city that you live in:  ")
    
        favoriteOS = typingInput("\nWhat is your favorite Operating System, such as Windows, Linux, or Mac:  ")
        while (len(favoriteOS) == 0): 
            favoriteOS = typingInput("\nInvalis Entry, please do not leave blank. Please enter your Favorite Operating System")
    
        favoriteAntiVirus = typingInput("\nEven if you don't use one, what is your Favorite AntiVirus Software:  ")
        while (len(favoriteAntiVirus) == 0):
            favoriteAntiVirus = typingInput("\nInvalid evtry, please do not leave blank! Please enter your favorite AntiVirus Software.")
    
        #BEGINNING OF STORY
        typingPrint(f"\nGreat! That is all that we need to go ahead and get this Super Computer ready for you! Again, congratulations! ... Ugh! What a load of crap! {firstName} is such an idiot!")
        typingPrint(f"\nI am completely dumbfounded that ANYONE can think that having a {favoriteOS} system with {favoriteAntiVirus} could even come close to taking me down, the Great and Powerful Super-Virus, Rico NoVerrey! I meen come o...n...OH...SHH...")
        typingPrint(f"\nDrats! Oh well, I guess the time is now! Listen up {firstName}, I am here to destroy your system, collect your information, and sell it on the dark web!")
        typingPrint("\nRICO:  I have an eye on that Apple Vision Pro that's out now, and I am going to use it in efforts to destroy and take down the World Wide Web and rule the world!")
        typingPrint(f"\nAUNTY VIROUSE:  Not if I have anything to do with it! I am Aunty Virouse, and {firstName}, you and I are going to take down this Son-of-a-Glitch together!")
        typingPrint("\nRICO:  Well, you can sure try to take me down! I already have a TON of your informtion you will never get back! Take THAT!")

        #DECISION 1 DO YOU HAVE A BACKUP CREATED.................................................
        backup = typingInput(f"\nAUNTY:   Just wait right there! {firstName} Please tell me you have a BackUp created of all your important information, files and folders? Yes or No:  ")
        while backup.lower() != "yes" and backup.lower() != "no":
            backup = typingInput("Please type yes or no:   ")
            
        if backup == "yes":
            typingPrint(f"\nAUNTY:   Great! So now not only is it pointless for him to try and take your information but he will have to get through the encryption first!")
            typingPrint("\nIn addition to that, you will be able to restore all your information if someting like this were to actially happen! and you lost your files!")
            typingPrint(f"\nRICO:   You got lucky this time {firstName}, but I am going deeper into the system and if I cannot take your information, I might as well fry your system! Attacking from the inside, causing irreversable damage!")
            typingPrint(f"\nAUNTY:   {firstName} we're gonna need to bring out the big guns and protect everything on your computer!")
            typingPrint("\nRICO:   Ant Vinigar is it? You think you can out smart and out play the Great and Powerful Rico NoVerrey")
        
        else:
            typingPrint(f"\nRICO:   This is all way too easy {firstName}! Aaaannnddd... There! *DELETE* Bye bye important work emails, application settings and information! Oh! Pics from a vacation! See ya NEVER AGAIN!")
            typingPrint(f"\nAUNTY:   It's going to be okay, so what, you have to start fresh. Let this be a lesson learned {firstName}. And as for you Mr. NoVerrey, I have a big suprize in store for you!")
            typingPrint("\nRICO:   Listen honey, you ain't got nothing that I cannot handle. I amm already here inside the CPU and I have everything ready to light this place up like the 4th of July!")
            
            
        #DECISION 2 DO YOU HAVE AN ANTI-VIRUS INSTALLED AND MONITORING YOUR DEVICE.................................................
        malware = typingInput(f"\nAUNTY:   This is it, if we dont get him now, we wont be able to. Do you have AntiVirus Software installed on your system? Yes or no:   ")
            
        if malware == "yes":
            typingPrint(f"\nPerfect {firstName}! This better work! I am going to calibrate and prepare to take him out!")
            typingPrint("\nRICO:   You think it is just going to be that easy? You can just hit some buttons, sit back and I fade away into nothingness? Really?!")
            typingPrint("\nAUNTY:   ..........yes!")
            typingInput("PLEASE PRESS ENTER TO INITIATE VIRUS REMOVAL SEQUENCE...")
            
        else:
            typingPrint("\nRICO:   Wow! I have never seen anything more beautiful! The sparks coming from that little wire thingy, beauty at full force!")
            typingPrint(f"\nAUNTY:   No! I am so sorry {firstName}! He has beated us! Hopfully you will be able to start over with a new system! Equipped with BackUp schedules and Anti-Virus installed and ready to battle!")
            
        #ALTERNATE ENDINGS.................................................
        if backup == "yes" and malware == "yes":
            typingPrint("\nRICO:   Impossible! There is no way you, how did you, no!")
            typingPrint(f"\nAUNTY:   Take that Mr. NoVerrey! We wont ever see the likes of him around here anymore! Nice job {firstName}!")
            typingPrint(f"\nA job well done {firstName}! You have defeated Rico NoVerrey with the help of Aunty Virouse! Your system is safe from danger!")
            typingPrint("\nRico has been trapped in quarantine for research and to be deleted from all databases. You have saved the day! Well done!")
            typingPrint("\nAUNTY:   Yes! Very well done my friend! Well I am going to go to the spa and relax, I suggest you do the same! Until Next Time! Hopfully there wont be one, but, you know!")
            typingPrint("\nThank You for playing and defeating Rico NoVerrey! You have nothing to worry about with your system! Your information is safe! Sorry you didn't REALLY win a Super Computer.")
        elif backup == "no" and malware == "no":
            typingPrint("\nRICO:   I cannot believe it! The likes I am going to get for this on my new Z Profile! I am the strongest and most powerful virus to have ever existed!")
            typingPrint(f"\nAUNTY:   I am sorry to say {firstName} that this is going to be a sad goodbye. I too must fade into the digital darkness")
            typingPrint("Without a sytem to exist and protect, there is nowhere for me to go. I hope you take a message away from this! Always BackUp and install Anti-Virus on your system!")
            typingPrint("At least I heard this isnt going to hur..... OUCH! OH My GOODNESS! THE PAIN!!! UNBEARABLE!!! MY CHILDREN!!!")
            typingPrint("...ok, I dont have any children, but did I get the point across?! Goodbye my good friend.")
            typingPrint("\nThank You for playing, unfortunately you did not make a dent in Rico NoVerrey and he got your information and destroyed your system. BackUp and install Anti-Virus on your next one!")
        
        else:
            typingPrint("\nRICO:   (gasping for air) This was a tough one! A good fight I may say! But I still was able to put your information on the dark web and grow stronger!")
            typingPrint("Maybe not as strong as I would have like to be, but I will be back! I promise! And your information is MINE! MUAHAHAHA (cough-choke-gasp) Hey Auntie, wanna go on a data with me?")
            typingPrint("\nAUNTY:   Very tempting, but heck-to-the no! I would newver do that, plus I have a lopt of work to do! We need to make sure we strengthen this system and be ready for next time, just in case!")
            typingPrint("\nWell you did not completely get rid of Rico NoVerrey, but he is exhausted and is done for now. But, he will be back!")
            typingPrint("\nThank You for playing, sorry you didnt win anything, but take this as a lesson to always BackUp and have Anti-Virus installed on your system!")
            
        keepGoing = typingInput(f"\nDo you want to play again and try to take out Rico NoVerrey? Yes or No:  ")
        while keepGoing.lower() != "yes" and keepGoing.lower() != "no":
            keepGoing = typingInput(f"Please type Yes or No:  ")
