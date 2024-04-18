'''
Problem:
    Write a program that asks the user for an integer and creates a list that consists of the factors of that integer
'''

# ESTANISLAO:
# Ask the user for an integer
num = int(input("Enter an integer: "))

# Initialize an empty list to store factors
factors = []

# Iterate through numbers from 1 to the input number
for i in range(1, num + 1):
    # Check if the current number is a factor of the input number
    if num % i == 0:
        # If it is, add it to the list of factors
        factors.append(i)

# Print the list of factors
print("Factors of", num, "are:", factors)


# SOLANO:
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
