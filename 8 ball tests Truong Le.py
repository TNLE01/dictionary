import random
import time

answers = ["Yes ", "Nah ", "Looking pretty good ","Doesn't seem likely ", "Agree ", "Disagree ", "Sure ", "More like a no "]
thinking = ["Let me think...", "Hmmm", "Lets see", "*cough cough*", "thinking..."]

name = input("Welcome to the magic 8-ball, what is your name? ")
print("Hello, %s"% name)

while True:
    magic = input("Please enter your question, or e[x]it to exit. ")
    if magic == "x":
        break
    else:
        print(random.choice(thinking))
        time.sleep(3)
        print(random.choice(answers) + name)
        again = input("Press enter to play again or e[x]it to exit. ")
        print("Ok")
        if again == "x":
            break
                      
print("Thank you for using magic 8-ball. ")
