# This program is used to calculate the total number of
# questions a person can answer incorrectly on an exam
# and still acheive a passing grade.

from termcolor import colored


print(colored('''
+========================================================================+
|                         MAX WRONG CALCULATOR                           |
+========================================================================+
 ''', "magenta", attrs=['bold']))



def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(colored("\nInvalid input. Please enter a whole number.", 'red', attrs=['bold']))

# The get_integer_input function prompts the user for input and checks if the input is an integer.
# If the input value is not an integer it will continue to prompt the user until an integer is 
# provided.



print(colored(('=')*74, 'cyan', attrs=['bold']))
max_score = get_integer_input("\nWhat's the highest score you can receive on the exam: ")
min_score = get_integer_input("\nWhat's the lowest passing score you can receive on the exam: ")
total_questions = get_integer_input("\nHow many questions are on the exam: ")

# Set the variable values using the get_integer_input function.
# You can call the function for each variable that you want to check.




print()
print(colored(('=')*74, 'cyan', attrs=['bold']))
passing_percent = round((min_score/max_score) * total_questions)
max_wrong = total_questions - passing_percent

# Use the values that were provided for the min_score, max_score, and total_questions variables
# to calculate the passing_percent and max_wrong variables.

print(colored(f"\nYou can answer {max_wrong} questions incorrectly and still pass the exam.\n", 'yellow', attrs=['bold']))
print(colored("+========================================================================+", 'magenta', attrs=['bold']))
