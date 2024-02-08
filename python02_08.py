import mymath
import random
# if __name__=="__main__":
#     n = int(input("Input n: "))
#     r = int(input("Input r: "))
#     print(f"{n}C{r} = {mymath.nCr(n,r)}")
#

answer=random.randint(1,100)
chance=7
count=1

while chance!=0:
    guess_number=int(input("Input guess number:"))
    if guess_number==answer:
        print(f"You Win.Answer is {answer}")
        print(f"you got it.you use {count}chance")
        break
    elif guess_number>answer:
        chance=chance-1
        count+=1
        print(f"guess number is lower. chance:{chance}")
    else:
        chance = chance - 1
        count+=1
        print(f"guess number is higher. chance:{chance}")
else:
    print(f"Game Over. answer is {answer}")
