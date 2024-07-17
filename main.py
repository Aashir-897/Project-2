import random
n = random.randint(1,100)
a = -1
guesses = 1
while a != n:

    a = int(input("Enter the number: "))
    if a>n:
        print("lower number please")
        guesses += 1

    elif a<n:
        print("Higher number please")
        guesses +=1

print(f"Youhave the correct number{n} in {guesses} attempt")
