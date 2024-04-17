Problem:
Write a program that asks the user for an integer and creates a list that consists of the factors of that integer

SOURCE CODE
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


