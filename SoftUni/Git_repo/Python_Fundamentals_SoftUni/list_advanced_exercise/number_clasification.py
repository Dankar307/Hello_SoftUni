def isPositive(numbers):
    return ', '.join([num for num in numbers if int(num) >= 0])



def isNegative(numbers):
    return ", ".join([num for num in numbers if int(num) < 0])



def isEven(numbers):
     return ", ".join([num for num in numbers if int(num) % 2 == 0])



def isOdd(numbers):
    return ", ".join([num for num in numbers if int(num) % 2 != 0])



numbers_list = input().split(", ")




print(f"Positive: {isPositive(numbers_list)}")
print(f"Negative: {isNegative(numbers_list)}")
print(f"Even: {isEven(numbers_list)}")
print(f"Odd: {isOdd(numbers_list)}")

