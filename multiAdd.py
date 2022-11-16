def multiple_add(input_array):
    return sum(input_array)

if __name__ == '__main__':
    # input_numbers = [2,5,6,8,9,100]
    input_numbers = list(map(int,input("Enter numbers saperated by space in between: ").split()))
    print(multiple_add(input_array=input_numbers))