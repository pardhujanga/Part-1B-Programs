# KitKat, a solo drinking game
import random

print("In this game, we both count along the natural numbers. If the number is a multiple of 3, say Kit instead")
print("Similarly, if it's a multiple of 5, then say Kat. The capitals shouldn't be used. You start by entering 1")
print("The game is designed such that the computer will randomly make a mistake sometimes to let you win.")
count = 0
a = 3
b = 5

while True:
    player_answer = str(input())
    reply = ""

    count += 1

    if (count%a == 0 and player_answer != "kit") or (count%b == 0 and player_answer != "kat") or ((count%a == 0 and count%b == 0) and player_answer != "kitkat"):
        print("That was wrong. You lose!")
        break
    elif (count%a != 0 and player_answer == "kit") or (count%b != 0 and player_answer == "kat") or ((count%a != 0 and count%b != 0) and player_answer == "kitkat"):
        print("That was wrong. You lose!")
        break


    count += 1

    Computer_mistake_list = [0,0,0,0,1]
    error = random.choice(Computer_mistake_list)
    noisy_count = count + error

    if (noisy_count%a == 0):
        reply += "kit"
    if (noisy_count%b == 0):
        reply += "kat"
    if (noisy_count%a != 0 and noisy_count%b != 0):
        reply = noisy_count
    print(reply)    
    if error == 1:
        print("I made a mistake. You Win!")
        break














