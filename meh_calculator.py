def add(a, b):
    "Adds two numbers and returns the sum."
    return a + b

def subtract(a, b):
    "subtracts the second number from the first and return the difference."
    return a - b

def multiply(a, b):
    "multiplies two numbers and return the product."
    return a * b

def divide(a, b):
    "Divide the first number by the second and return quotient. Return None if the second number(b) is zero, preventing a crash."
    if b == 0:
        return None
    return a/b
def main():
    print("UGHHHHHH!!! I don't want to do it but I have to. Welcome to Meh-calculator or something like that...")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("What do you want to do? (+, -, *, /): ")
    except ValueError:
        print("Are you kidding me? That's not the right number, airhead. Try again next week or never. I don't want to do this.")
        return
    if operation == '+':
        result = add(num1, num2)
        print(f"Do I have to? fine. the sum is {result}. Are we done now? Now let's never do this ever again.")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"fine. It's not like I have a choice anyway. The difference is {result}. Don't expect anything else from me.")
    elif operation == '*':
        result = multiply(num1, num2)
        print(f"Are you dumb or something? Shouldn't you know this in fourth grade or something? Ugh, the product is {result}. Just whatever,")
    elif operation == '/':
        if num2 == 0:
            print("Wow. Dividing by zero. That is so dumb. com back and try again after you go back to elementary class.")
        else:
            result = divide(num1, num2)
            print(f"The quotient is {result}. Happy now? I'm too tired to do this.")
    else:
        print ("you did it wrong but whatever, I don't care.")
if __name__ == "__main__":
    main()