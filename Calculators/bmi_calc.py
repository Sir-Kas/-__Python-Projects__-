from termcolor import colored


print(colored('''
+--------------------------------------------------------------------------------+
|                                BMI CALCULATOR                                  |
+--------------------------------------------------------------------------------+
              ''', "magenta", attrs=['bold']))

print(colored("""
# Body Mass Index (BMI) is a measure of a person’s weight relative to their height.
# BMI is a widely used indicator of body fatness and can help identify potential 
# health risks associated with being overweight or underweight. However, it should 
# be noted that BMI is not a direct measure of body fat and may not be accurate for 
# certain individuals, such as athletes or those with a high muscle mass.
              """, 'cyan', attrs=['bold']))


print(colored(('=')*82, 'yellow', attrs=['bold']))

while True:
    try:
        lb = int(input("\nEnter your weight in lbs. Round to the nearest whole number: "))
        break
    except ValueError:
        print(colored("Invalid input. Please enter a whole number: ", 'red'))


kg = 0.45359237
lb_to_kg = (round(lb * kg, 2))


while True:
    try:
        height = float(input("\nEnter your height as a decimal number: "))
        break
    except ValueError:
        print(colored("Invalid input. Please enter a decimal number: ", 'red'))


meter = 0.3048
meter_to_feet = (round(height * meter, 2))

bmi = (lb_to_kg / meter_to_feet**2)

print()
print(colored(('=')*82, 'yellow', attrs=['bold']))


if bmi < 18.5:
    print(colored(f'\nYour BMI is : {bmi}\n\nYou are under weight.', "cyan", attrs=['bold']))
elif bmi >= 18.5 and bmi < 25:
    print(colored(f'\nYour BMI is: {bmi}\n\nYou have a normal weight.', "green", attrs=['bold']))
elif bmi >= 25 and bmi < 30:
    print(colored(f'\nYour BMI is: {bmi}\n\nYou are slightly overweight.', "cyan", attrs=['bold']))
elif bmi >= 30 and bmi < 35:
    print(colored(f'\nYour BMI is: {bmi}\n\nYou are obese.', "red", attrs=['bold']))
else:
    print(colored(f'\nYour BMI is: {bmi}\n\nYou are clinically obese.', "red", attrs=['bold']))


print()
print(colored(('=')*82, 'magenta', attrs=['bold']))
