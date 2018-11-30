# ----------------------------------------------------------------
#       Names: Claire, Iver, Maura, Selah
#    Filename: riddles.py
#        Date: 11.30.2018
#
# Description: Presents user with a riddle. The user has 3 tries
#              to answer the riddle. 
# ----------------------------------------------------------------




import random

def riddle():


    complete_riddle = {'riddle':'answer'}

    riddles = {"What word begins and ends in E but only has one letter?" : "envelope",
               "I’m tall when I’m young and I’m short when I’m old. What am I?" : "candle",
               "What has hands but can’t clap?" : "clock",
               "What starts with the letter T, is full of T and ends with the letter T?" : "teapot",
               "What goes up but never goes down?" : "age",
               "What has one eye but cannot see?" : "needle",
               "The more you take, the more you leave behind, what am I?" : "footprints",
               "What is so delicate that saying its name breaks it?" : "silcence",
               "Where there is light is the only place I can live. Yet if light shines on me I die." : "shadow"}

    riddle = random.choice(list(riddles.keys()))
    answer = riddles[riddle]

    print ("Riddle Rules: You have 3 tries to solve this riddle, all solutions are one word, enter answers in lowercase")
    print()
    print ("Here is your riddle: ", riddle)
    print()
    user_answer = input("Your answer: ")

    counter = 0
    while user_answer: 
        if user_answer == answer:
            print ("You may continue...")
            break
        elif user_answer != answer and counter < 2:
            print("Wrong Answer, try again.")
            user_answer = input("Your answer: ")
            counter += 1
        elif user_answer != answer and counter >= 2:
            print("Wrong answer and you are out of tries...")
            break
            #what happens if the person can't answer the riddle?
            #player takes damage 


def main():
    riddle()

if __name__=="__main__":
    main()
        
