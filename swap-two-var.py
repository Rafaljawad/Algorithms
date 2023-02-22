#Write a Python program to swap two variables without temp variable ?
def swap(num1, num2):
    print(f"input number1 before swapping is {num1} and number2 is {num2}")
    [num1, num2] = [num2, num1]
    return f"after swapping number 1 is: {num1} and number2 is {num2}"
print(swap(3, 4))



#or
def swap(num1, num2):
    print(f"input number1 before swapping is {num1} and number2 is {num2}")
    num1, num2 = num2, num1
    return f"after swapping number 1 is: {num1} and number2 is {num2}"
print(swap(3, 4))
