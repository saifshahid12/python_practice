    # the game function() in programme let a user play a game and return the score as 
    # an integer .you need to read a file hi_score.txt which is either blank or contain
    # the previous hi_score, you need to write a programme to update a hi_score whenever 
    # the game func() break the high score:

import random

def game():
    print("you are playing the game ..")
    score= random.randint(1,62)

    # fetch the high score:

    with open("highscore.txt") as f:   
        highscore=f.read()
        if (highscore!=""):
            highscore=int(highscore)

        else:
            highscore=0
            print(f"your score{score}")
        if (score>highscore):
            with open ("highscoe.txt","w") as f:
                f.write(str(score))

        return score
game()