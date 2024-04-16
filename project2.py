import random 
randNum=random.randint(1,100)
userGuess=None
guesses=0
# print(randNum)



while(userGuess!=randNum):
    userGuess=int(input("enter your number:"))
    guesses+=1
    if(userGuess==randNum):
        print("you guessed it right")
    else:
        if(userGuess>randNum):
         print("you guessed it wrong! pls enter smaller number")
        else:
         print("you guessed it wrong! pls enter enter greater number")
        
print(f"you guessed the number in {guesses} gusses")

with open("hiscore.txt","r")as f:
   hiscore=int(f.read())

if(guesses<hiscore):
   print("you have just broken the high score!!")
   with open("hiscore.txt","w")as f:
      f.write(str(guesses))