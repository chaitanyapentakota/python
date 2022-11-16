import random
name=input("enter your name:")
print(name,"please guess a number between 1 to 100")
result = "no"
min = 1
max = 100
random_num=random.randint(min,max)
while result=="no":
    print(random_num)
    print("{} - is this correct? type yes or no". format(random_num))
    result= input()
    if (result=="yes"):
        print("yes , i guessed it..!!")
    else:
        print("is it less than {} or grater than {}". format(random_num, random_num))
        lessorgreater = input()
        if(lessorgreater=="less"):
            max = random_num-1
            random_num= random.randint(min,max)
        else:
            min = random_num+1
            random_num= random.randint(min,max)        