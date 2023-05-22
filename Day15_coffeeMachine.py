from Files.coffeeMachine_data import menu, resources, logo

money = 0
def report(resources):
    print(f'''
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money}
''')

print(logo)
print("Welcome to Digital Coffee Machine.")

while True:
    showReport = input("Do you wanna see the report? please enter 'y' or 'n': ")
    if showReport == 'y':
        report(resources)
    flavor = input("What would you like? (espresso/latte/cappuccino): ")
    
    if flavor == 'off' or flavor == ' ':
        exit()
    if flavor == 'espresso' or flavor == 'latte' or flavor == 'cappuccino':
        
        if resources['water'] < menu[f"{flavor}"]['ingredients']['water']:
            print("Sorry, there is not enough water.")
        elif resources['coffee'] < menu[f"{flavor}"]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee.")
        elif resources['milk'] < menu[f"{flavor}"]['ingredients']['milk']:
            print("Sorry, there is not enough milk.")
        
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?(0.25): "))
            dimes = int(input("How many dimes?(0.10): "))
            nickles = int(input("How many nickles?(0.05): "))
            pennies = int(input("How many pennies?(0.01): "))
    
            totalAmount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
            if totalAmount < menu[f'{flavor}']['cost']:
                print("Sorry that's not enough money. Money refunded.")
    
            else:
                resources['water'] -= menu[f"{flavor}"]['ingredients']['water']
                resources['milk'] -= menu[f"{flavor}"]['ingredients']['milk']
                resources['coffee'] -= menu[f"{flavor}"]['ingredients']['coffee']
                money += menu[f'{flavor}']['cost']
            
                refund = totalAmount - menu[f'{flavor}']['cost']
    
                print(f"Here is ${round(refund, 2)} in change.")
                print(f"Here is your {flavor}. Enjoy!")
    else:
        exit()