# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
# Declare a string variable, e.g., sentence = "Learning Python is fun!"
    sentence = input()
# Extract and print a substring, such as the word "Python" from the sentence.
    if 'Python' in sentence:
        print("Python")
# Convert the entire sentence to uppercase and print it.
    print(sentence.upper())
# Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
    print(sentence.replace('fun', 'awesome'))
# If the user chooses Numbers (choice == '2'):
elif choice == '2':

# Prompt the user to input two numbers, e.g., num1 and num2.
    num1 = input('Enter one number please: ')
    num2 = input('Enter second number please: ')

# Perform and print the results of addition, subtraction, multiplication, and division.
    if num2 == 0:
        print('Undefined! \nPlease try another number!')
    else:
        print(f'{num1} + {num2} = {num1 + num2}')
        print(f'{num1} - {num2} = {num1 - num2}')
        print(f'{num1} * {num2} = {num1 * num2}')
        print(f'{num1} / {num2} = {num1 / num2:.2f}')
# Handle division by zero (e.g., print an error message if num2 is zero).

# Perform a power operation, raising num1 to the power of num2, and print the result.
        powered_num = pow(num1, num2)
        print(f'{num1} To the power of {num2} = {powered_num}')
# If the user chooses Booleans (choice == '3'):
elif choice == '3':

# Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    is_python_fun = True
    is_sunny = False
# Perform and print the results of logical operations: AND, OR, NOT.
    if is_python_fun and (not is_sunny == True):
        print(f'Python is funny and its not sunny!')
# Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
    if 10 < 13:
        print('10 is less than 13!')

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':

# ### List Operations ###
# Create a list with mixed data types (e.g., numbers, strings, booleans).
    list1 = [24, 'Apple', False]
    print(list1)
# Append a new element to the list and print the updated list.
    list1.append(input())
    print(list1)
# Access and print the 4th element in the list.
    print(list1[-1])
# ### Tuple Operations ###
# Create a tuple with some string elements (e.g., fruits).

# Print the length of the tuple.

# Try to modify one element in the tuple and handle the resulting TypeError.

# ### Dictionary Operations ###
# Create a dictionary with some key-value pairs (e.g., name, age, city).

# Access and print the value for one of the keys (e.g., "age").

# Add a new key-value pair to the dictionary and print the updated dictionary.

# If the user enters an invalid choice:
else:
    pass
# Print an error message indicating an invalid selection.
