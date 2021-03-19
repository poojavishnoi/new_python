import art

print(art.logo)
print("Welcome to Calculator")

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    num1 = float(input("Enter the number:\n"))
    for symbol in operators:
            print(symbol)
    again = True
    while again:
        
        operation = input("What opertaion you want to do?\n")
        num2 = float(input("Enter the next number:\n"))
        calc_function = operators[operation]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}\n")

        repeat = input("Enter 'y' to continue and 'n' to start a new calculation.\n")
        if repeat == "y":
            num1 = answer
        elif repeat == "n":
            again = False
            calculator()


calculator()