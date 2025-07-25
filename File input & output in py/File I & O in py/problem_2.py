'''the game() function in a program lets a user play a game and return the score as an integer.
 you need to read a file 'Hi-score.txt' which is either blank or contain the previous Hi-score ,
 you need to write a program to update the hi-score whenever the game()function breaks the hi-score    
 '''
import random
def game():
    print("you are playing a game...")
    score=random.randint(1,99)
    # fetch the hiscore

    with open("hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
         hiscore = int(hiscore)
        else:
           hiscore=0
    print(f"your score: {score}")
    if(score>hiscore):
    #    write this hiscore to the file
        with open("hi-score.txt" , "w") as f:
            f.write(str(score))
    return score
game()
    

