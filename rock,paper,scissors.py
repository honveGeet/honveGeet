import random

p = int(input("Choose what hand you want to play. Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
print("You chose: ")
if p==0:
    print("ROCK")
elif p==1:
    print("PAPER")
else:
    print("SCISSORS")

hands = [0,1,2]
c = int(random.choice(hands))

print("The computer chose: ")
if c==0:
    print("ROCK")
elif c==1:
    print("PAPER")
else:
    print("SCISSORS")

if (p==0 and c==2) or (p==1 and c==0) or (p==2 and c==1):
    print("You win!")
elif p==c:
    print("Tie!")
else:
    print("You lose..")