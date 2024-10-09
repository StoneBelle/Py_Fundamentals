# Functions for mathematical operators
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": sub,
    "*": mul,
    "/": div,
}

# Function to calculate the inputs given from the user
def calculate():
    # Ask user what they would like to calculate
    num_1 = int(input("\nWhat's the first number? "))

    # Create a loop to continue calculating with same answer
    while True:
        operator = input('\n"+"   "-"   "*"   "/"\nPick an operation: ')
        num_2 = int(input("\nWhat's the second number? "))
        answer = operations[operator](num_1, num_2)
    
        print(f"{num_1} {operator} {num_2} = {answer}\n")

        # Check if user would like to continue calculating with initial calculation
        status = input('Continue calculating with {answer}? Type "Y". OR Type "N" to begin a new calculation: ').upper().replace(" ", "")
        
        if status == "Y":
            num_1 = answer
        
        elif status == "N":
            print("\nCalculation has ended. Starting a new Calculation.")
            # Call function to repeat itself (i.e. Recursion)
            calculate()


calculate()



    










