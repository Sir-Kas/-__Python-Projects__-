from termcolor import colored

print(colored('''
+-------------------------------------------------+
|                 TIP CALCULATOR                  |
+-------------------------------------------------+
 ''', "magenta",attrs=['bold']))

print(colored(('=')*51, 'cyan', attrs=['bold']))

total = float(input("\nHow much is the bill? "))
tip = int(input("\nWhat percentage of the bill would you like to leave for a tip? "))
people = int(input("\nHow many people are on the bill? "))


divided_total = (round(total/people, 2))

calculated_tip = (round(total * (tip/100), 2))
tip_per_person = (round(calculated_tip/people, 2))

grand_total = (round(total + calculated_tip, 2))
cost_per_person = (round(grand_total/people, 2))

print()
print(colored(('=')*51, 'magenta', attrs=['bold']))

if people == 1:
    print(colored(f"\n{tip}% of ${total} = ${calculated_tip}\n", 'cyan', attrs=['bold']))
    print(colored(f"===================================================",'magenta', attrs=['bold'] ))
    print(colored(f"\nThe total cost with a {tip}% included is: ${grand_total}\n" , 'cyan', attrs=['bold']))
    print(colored("+-------------------------------------------------+",'magenta', attrs=['bold'] ))

else:
    print(colored(f"\n${total} divided by {people} = ${divided_total} per person\n\n", 'cyan', attrs=['bold'])) 
    print(colored(f"{tip}% of ${total} = ${calculated_tip}\n\n", 'cyan', attrs=['bold']))
    print(colored(f"${calculated_tip} divded by {people} = ${tip_per_person} per person\n\n", 'cyan', attrs=['bold']))
    print(colored(f"${divided_total} plus ${tip_per_person} = ${cost_per_person}\n\n"))
    print(colored(f"===================================================",'magenta', attrs=['bold'] ))

    print(colored(f"\nEach person will pay: ${cost_per_person}\n", 'yellow', attrs=['bold']))
    print(colored("+-------------------------------------------------+",'magenta', attrs=['bold'] ))
