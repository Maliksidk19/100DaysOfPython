from Files.oops_coffee_machine_data import Menu, CoffeeMaker, MoneyMachine, logo

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(logo)
print("Welcome to Digital Coffee Maker.")
while True:
    showReport = input("Do you want th report? please enter 'y' or 'n': ")
    if showReport == 'y':
        coffee_maker.report()
        money_machine.report()
    
    flavor = input("What would you like? (espresso/latte/cappuccino): ")
    
    if menu.find_drink(flavor):
        drink = menu.find_drink(flavor)
    
        if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    
    else:
        exit()