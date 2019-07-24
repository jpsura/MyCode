#!/usr/bin/env python3

round = 0 #integer round initiated to 0
while(True): #sets the loop condition
    round = round + 1 #increases round count each time
    print('Finish the movie title, "Monty Python\'s The Life of_____"')
    answer = input() #Collects the data from user
    if (answer == 'Brian'): #Logic to check answer
        print('correct')
        break  # provides the loop exit
    elif(round==3): #logic to not reach more than 3 rounds
        print("sorry the anser was Brian")
        break #provides loop exit
    else: #if the answer was wrong and the round is not 3 yet
        print("sorry try again")

