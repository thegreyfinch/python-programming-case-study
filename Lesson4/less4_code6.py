Write a program that asks the user for an integer and creates a list that consists of the factors of that integer

# Function to find factors of a given number
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Ask the user for an integer
try:
    num = int(input("Enter an integer: "))
    if num < 1:
        print("Please enter a positive integer.")
    else:
        # Find factors of the given integer
        factors = find_factors(num)
        
        # Print the list of factors
        print("Factors of", num, "are:", factors)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
