import matplotlib.pyplot as plt
import threading
import time
class TextFiles:
    #a class that will extract the text from all .txt files that work with this program, and do various sorts of actions with the texts

    #a function that will extract all text files and add them into a list
    def extractAllTextFiles(self):
        #extract the text from GodOfWar.txt
        with open("GodOfWar.txt") as file:
            GodOfWar = file.read()
        #extract DarkSouls.txt
        with open("DarkSouls.txt") as file:
            DarkSouls = file.read()
        #extract ArkhamBatman.txt
        with open("ArkhamBatman.txt") as file:
            ArkhamBatman = file.read()
        #extract Zombies.txt
        with open("Zombies.txt") as file:
            Zombies = file.read()
        #return all the variables that contain the text of each topic to it by means of a list
        allTextFiles = []
        allTextFiles.append(GodOfWar)
        allTextFiles.append(DarkSouls)
        allTextFiles.append(ArkhamBatman)
        allTextFiles.append(Zombies)
        return allTextFiles

class LineGraph:
    #a class that will plot a line graph according to the wpm and accuracy of each attempt
    def __init__(self, adjustedWPMList, accuracy, wpm, firstPlayThrough): #PASS IN A LIST INSTEAD OF A SINGLE VARIABLE!!!!!!!!!!
        #initialize a list that will contain the accuracy paramater of every class attempt
        self.adjustedWPMList = adjustedWPMList
        self.AWPM = round(wpm * (accuracy/100))
        self.adjustedWPMList.append(self.AWPM)#added the AWPM to the list, meaning it is the wpm * accuracy
        self.accuracy = accuracy
        self.wpm = wpm
        self.firstPlayThrough = firstPlayThrough
    def plotGraph(self):
        #if this isn't the players first play through, ask if they want to see a line graph of their progress
        if(self.firstPlayThrough == False):
            #state user accuracy
            wantToPlotGraph = input("\n-You typed at " + str(round(self.wpm)) + " wpm with " + (str(self.accuracy)) + "% accuracy. \n-That is " + str(self.AWPM) + " wpm if you take accuracy into account. This is also known as adjusted words per minute(AWPM). \n-Would you like to see a graph of your improvement since you've started?(y/n) ")
            #ask the user if they want to see their improvement since start
            if(wantToPlotGraph == "y"):
                #define the numbers for x and y values
                x_values = []
                y_values = []
                for i in range(len(self.adjustedWPMList)):
                    #x value is the index(i + 1)
                    x_value = i + 1
                    x_values.append(x_value)
                    #y value is the element by the index
                    y_value = self.adjustedWPMList[i]
                    y_values.append(y_value)

                #plot line graph
                fig,ax = plt.subplots()
                ax.plot(x_values, y_values, linewidth=4)
                #plot scatter points as well
                ax.scatter(x_values, y_values)
                #set the chart title and label axes
                ax.set_title("Typing Game Results", fontsize=24)
                ax.set_xlabel("Attempt #",fontsize=14)
                ax.set_ylabel("Adjusted Words Per Minute(AWPM)", fontsize=14)
                #set the range for each axis
                ax.axis([0, (len(x_values) + 1), 0, 100])
                plt.show()
        else:
            print("\n-You typed at " + str(round(self.wpm)) + " wpm with " + (str(self.accuracy)) + "% accuracy. \n-That is " + str(self.AWPM) + " wpm if you take accuracy into account. This is also known as adjusted words per minute(AWPM).")
        #ask the user if they want to play another game
        playAnotherGame = input("\nWould you like to play again?(y/n) ")
        if(playAnotherGame == "y"):
            playAgain = True
        else:
            playAgain = False
        #return the list to enter as a parameter the next time an object is created
        return self.adjustedWPMList, playAgain

#this class will be used to have a timer run while allowing the user to type
class timerAndTextWork:
    def __init__(self, boolean):
        #initialize attributes
        self.boolean = boolean

    def timer(self):
        #start a timer to find how long it took the user to type in the entire text
        timeItTook = 0
        while (self.boolean == False): #while the boolean that was initialized earlier stays false
            time.sleep(1)
            timeItTook += 1
        return timeItTook

    #this function below will collect the text the user wrote and how long it took
    def typing(self):
        #at the same time as the timer function is called, start the game, by prompting the user to start typing
        typingInput = input("GO!: \n")
        self.boolean = True
        return typingInput
