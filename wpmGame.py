from wpmGameClasses import LineGraph
from wpmGameClasses import TextFiles
from wpmGameClasses import timerAndTextWork
import time
import random
import concurrent.futures

#this function below will collect the text the user wrote and how long it took
def textWork(textFile):
    print("\n" + textFile)
    #start a countdown
    print("Game starting in: ")
    counter = 5
    print(counter)
    while counter != 1:
        time.sleep(1)
        counter -= 1
        print(counter)
    stoppedTyping = False
    start = timerAndTextWork(stoppedTyping)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(start.timer)
        f2 = executor.submit(start.typing)
        typingInput = f2.result()
        timeItTook = f1.result()
    #after enter is pressed, meaning the user is done typing, make the stoppedTyping variable true, to stop the timer
    start.stoppedTyping = True
    #return the input that the user entered
    return typingInput, timeItTook

#this function will display the accuracy of the attempt to the user and will ask them if
#they want to see a line graph plot of their attempts, which will show their progress over multiple rounds of the game(this option will only be available after the first play through of the game)
def showAccuracyAndLineGraph(text, object, list, firstPlayThrough):
    userInput, time = textWork(text)
    #break down userInput text and text into a list
    userText = userInput.split()
    text = text.split()
    #compare the items in the list and mark the percent of words gotten correctly
    words = len(text)
    correctWords = 0
    for i in range(len(userText)):
        #if two words at the same index match up, add a point to correctWords
        if(text[i] == userText[i]):
            correctWords += 1
    #create LineGraph object
    accuracyPercentage = round((correctWords/words) * 100)
    #calculate the wpm the user typed(words/minutes) and add it to the plotGraph function as a parameter
    minutes = time / 60
    userTextWords = len(userText)
    wpm = userTextWords / minutes
    object = LineGraph(adjustedWPMList, accuracyPercentage, wpm, firstPlayThrough)
    #only call the plotGraph function if firstPlayThrough variable is false
    list, playAgain = object.plotGraph()
    #start another round or end program depending playAgain variable value
    return playAgain

adjustedWPMList = [] # the list that will be used in the creation of LineGraph objects, must create this list outside of while loop so data doesn't get wiped every time the loop restarts
#throw the entire code which starts and finishes a round of the game in a while loop, in case user wants to play more than one round
firstPlayThrough = True
playAgain = True
while playAgain:
    #determine which text to use, use a while loop until user input is valid
    while True:
        #use a try except block in case user enter anything other than a number
        try:
            userDecision = int(input("\nChoose a topic in our list of popular video game franchises, or type in '5' and a randomn one will be chosen: \n\t1.God of War \n\t2.Dark Souls \n\t3.Batman: Arkham \n\t4.Call Of Duty Zombies \nWhich one would you like? "))
        except ValueError:
            print("Invalid input(must be a number between 1-4). Please try again.")
        else:
            if(userDecision > 0 and userDecision <= 5):
                break
            else:
                print("Invalid input(must be a number between 1-4). Please try again.")
                continue
    #call class and get the text files
    text = TextFiles()
    allTextFiles = text.extractAllTextFiles()
    GodOfWar = allTextFiles[0]
    DarkSouls = allTextFiles[1]
    ArkhamBatman = allTextFiles[2]
    Zombies = allTextFiles[3]
    #depending on which option the user chose, call the showAccuracyAndLineGraph function and input the correct parameters
    if(userDecision == 1):
        playAgain = showAccuracyAndLineGraph(GodOfWar, object, adjustedWPMList, firstPlayThrough)
    elif(userDecision == 2):
        playAgain = showAccuracyAndLineGraph(DarkSouls, object, adjustedWPMList, firstPlayThrough)
    elif(userDecision == 3):
        playAgain = showAccuracyAndLineGraph(ArkhamBatman, object, adjustedWPMList, firstPlayThrough)
    elif(userDecision == 4):
        playAgain = showAccuracyAndLineGraph(Zombies, object, adjustedWPMList, firstPlayThrough)
    else:
        #input a random value from the allTextFiles list into the showAccuracyAndLineGraph function
        playAgain = showAccuracyAndLineGraph(random.choice(allTextFiles), object, adjustedWPMList, firstPlayThrough)
    #if the program has gotten here, one entire round of the game has been played, so turn the firstPlayThrough variable to False
    firstPlayThrough = False
