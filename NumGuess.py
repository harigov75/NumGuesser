import random

print("I have chosen a number...can you guess what it is? You get 7 tries.")
print("(Pssstt...it's between 1 and 100..)")
num = random.randint(1,100)

def processFun(num):
    att=7
    while(att):
        n = int(input("Enter your guess: "))
        att-=1
        if(n>num):
            print("Nope..it's a bit lower than ",n)
        elif(n<num):
            print("Nope..it's a bit higher than ",n)
        else:
            print("Congrats! You got it in ",7-att," attempts!!")
            break
    print("Oops...sorry! The number was ",num,"...Better luck next time!")

processFun(num)

