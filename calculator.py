def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Addition:", add(x,y))
    print("Subtraction:", subtract(x,y))
    print("Multiplication:", multiply(x,y))
    print("Division:", divide(x,y))
main()