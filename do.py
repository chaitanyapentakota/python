def power(x):
    num = [1,2,3,4,5,6,7,8,9]
    num2 = []
    for n in num:
        num2.append(x**n)
    return(num2)
print(power(int(input())))
