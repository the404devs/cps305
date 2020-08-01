# CPS305 Lab 1
# 09/10/19 - Owen Goodwin
# I'm just assuming y'all want this stuff documented

import random # Needed to grab a random index value, which we use to grab a random letter from the alphabet
import matplotlib.pyplot as plt # Needed to plot a graph, as per the requirements of this assignment

#Function to generate a random string of length targetLength, consisting of random characters from alpha
def generate(targetLength, alphaLen, alpha):
    out = ""# Will be filled with our resulting string soon
    for x in range(0, targetLength):# Ye olde for loop, will repeat until we've grabbed enough chars to fill our string
        x = random.randrange(alphaLen)# Take a random number, corresponding to the index of a letter in our alphabet
        out+=alpha[x]# Add that random letter to our output string
    return out# Spit out our random string, so we can do all sorts of fun things with it

#Function to calculate the "score" of a random string -> a percentage of how close it is to the target string
def calcScore(string, target):
    sum = 0# We're gonna add up the number of correct chars we've got so far, and we need a place to store that sum
    for i in range(len(target)):# Now, we loop through each char of the target string...
        if string[i]==target[i]:# ... and we check if we've got that character in our random string. If so, add one to our sum...
            sum+=1
        else:# ... and if not, then stop. Nothing beyond this point in our string is correct. (well, technically it could, but that's just more work...)
            break
    return float((sum/len(target))*100.0)# Some quick maths to determine the percentage of correct characters. Note the floating point rep, because we love decimals
            
    
# Function to put an infinite amount of monkeys out of their infinite jobs... How cruel...
# The deal is, we're gonna put random letters together until it matches a preset target string. But you already knew that.
def monkeyTypist():
    target = "the most hopelessly stupid man is he who is not aware he is wise"# Our target string. Bonus points if you recognize the quote.
    lenS = len(target)# The length of our target, representing how many random chars to generate. This will decrease as we find more correct ones.
    alphabet = "abcdefghijklmnopqrstuvwxyz "# The alphabet. This is where we get our letters from.
    lenA = len(alphabet)# The length of the aforementioned alphabet
    epoch = 0#More of a counter than an epoch, but I digress. Used to tell when to spit out a score (every 100 iterations)
    elist = list()#elist and slist are lists. We fill them with the epoch and score values we plot on our graph later
    slist = list()
    bestScore=0.0#The best score, representing how close we've gotten to matching the target string so far
    correctChars = ""#Will be used to store the characters in our target that are in the correct place
    print("String | Score | Iteration")
    while bestScore < 100.0: #Don't stop until the job is done
        rand = generate(lenS, lenA, alphabet)#Generate a random string
        newStr = correctChars+rand#Prepend the characters that are already in the right place to the random string
        newScore = calcScore(newStr, target)#Calculate the score of this latest string
        if newScore > bestScore:#If the score is better than the best we have, then we have a new best string
            x=len(correctChars)#Grab the current number of correct characters. We need this in a bit.
            correctChars = ""#Empty out our basket of characters, we need some new ones.
            for i in range(len(target)):#A for loop to determine which characters in our string are correct.
                if newStr[i]==target[i]:
                    correctChars+=newStr[i]                    
                else:
                    break
            y=len(correctChars)#Grab the number of correct characters we have now.
            lenS-=(y-x)#Decrease the length of our random strings by the number of new random characters we've picked up. 
                       #(Last # of new chars - Current # of new chars)
            bestScore = newScore#Update the best score
            elist.append(epoch)#Make note of the iteration we're on and the score we obtained.
            slist.append(bestScore)
            
        if epoch%100==0:#Triggers on every 100th iteration
            print(newStr+" | "+str(float(bestScore))+" | "+str(epoch))#Print out info regarding our progress so far              
        if bestScore==100:#Best score is 100%! That means we've won!
            print(newStr+" | "+str(float(bestScore))+" | "+str(epoch))#Print one last time 
            elist.append(epoch)#One last log of our iteration and score
            slist.append(bestScore)
            break#End this madness
        epoch = epoch+1#Increase our epoch value, and do it all over again
    #Plotting our graph
    plt.plot(elist,slist, "r+")#The data to plot (r+ means red + marks)
    plt.xlabel("Iteration")#Labels for the x- and y-axis
    plt.ylabel("Score of best string")
