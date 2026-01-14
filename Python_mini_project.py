import random
# Number guessing
n=random.randint(1,100)
a=-1
guesses=1
# for comparing the number with user input
while(a!=n):
    a=int(input("guess the number: "))
    if(a>n):
        print("lower number please")
        guesses+=1
    elif(a<n):
        print("higher number please")
        guesses+=1
#finlly when user guesses the number
print(f"you have guessed the number {n} correctly in {guesses} attempts")