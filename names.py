import random
names = ("Ashley", "Bonnie", "Charlie", "David", "Esther", "Fiona", "George", "Harper", "Isabelle", "Jessica", "Kyle", "Leonard", "Mandy", "Natasha", "Olivia", "Penelope", "Queenie", "Richard", "Shawn", "Tasha", "Ulysses", "Vanessa", "Wyatt", "Xavier", "Yvonne", "Zelda")
scores = {}
for name in names:
    while True:
        try:
            scores[name] = int(input("What is the score for "+str(name)+"?"))
            break
        except:
            print("You should choose an integer.")
print(scores)

for i in range(50):
    print("\n")


while True:

    guess = input("Guess a name.")
    if guess in names:
        score = str(scores[guess])
        print("Your score is "+ score)
        break
    else:
        print("Your guess is wrong. Please try again.")
