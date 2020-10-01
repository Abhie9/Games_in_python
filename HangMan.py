import random   #import library to select the random value from the list of predefined words
''' Declarations'''
DefinedWords=["perhaps","vigorous","prognosis"]     #predefined Word.
blanks=[]       #define List to Print the Dashes
WrongGuess=[]   #list to store the wrong guess
SameLetter=[]   #list to store indexes of the same occurance of the value
attempts = 1    #variable for wrong attempts


Question = random.choice(DefinedWords)  #Storing random element from DefineWords[] into Question variable
length=(len(Question))  #we are storing the length of the question into length variable
chances = round(length/2)   #Counting Chances that user have
'''For Demo Purpose Only'''
print(Question)
# for i in Question:
#     print(i, end=" ")
# print()
'''Print the blanks and inform the letters alnong with chances'''
print("_-*_-*_-*_-*-_You have ",chances," chances to guess ",length," letter word!_-*-_*-_*-_*-_*-_\nGood luck with your guess work! 👍🏽")
for i in range(1,length+1):     #append the dashes into blanks[] with the range of the word
    blanks.append("_")
print()
for i in blanks:    #print the dashes from blanks[] with the range of the word
    print(i,end=" ")
print()

'''Real Game starts here'''

while attempts <= chances:  #loop until the chances are over
    if '_' not in blanks:   #checks complition of the word
        print("🥳Good Job!🥳")
        break
    userIn = input("Guess the word: \n")[0]     #takes input from user and stores first character.
    if userIn not in WrongGuess and userIn not in blanks:
        for i in range(len(Question)):      #Store correct indexes int SameLetter[]
            if Question[i] == userIn:       #Checks input exists in the word
                SameLetter.append(i)    
        if len(SameLetter) > 0:         #checks letter is right
            print("🎆Good Guess Keep Guessing!🎆")
            for i in Question:      #to change the dash with correct letter
                if (i == userIn):   #compares the element
                    for j in SameLetter:    #for same right letters
                        blanks.insert(j,userIn)     #replacing the value
                        blanks.pop(j+1)             #remove the dash    
                        SameLetter.pop(0)           #remove the index value from SameLetter[]
            print(blanks)                           #printing the remaining blanks
        else:
            WrongGuess.append(userIn)               #stores worng guess into WrongGuess[]
            print("better luck Next time!")
            print("you Wrong guesses are ",WrongGuess)
            attempts+=1           #increments wrong attempts
    else:
            print("Hey! You already guessed the letter \"",userIn,"\"!!!")
print("You Guessed it right. The Right Answer is :",end="")
for i in Question:
    print(i, end="")
print()