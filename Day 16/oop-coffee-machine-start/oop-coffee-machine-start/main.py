from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def cost(drint):
    if drint == "latte":
        return 2.5
    elif drint == "espresso":
        return 1.5
    else:
        return 3

objmenu = Menu()
objcofeemaker = CoffeeMaker()
objmoneymachine = MoneyMachine()


power = True
while power == True:
    print(objmenu.get_items())
    inp = input("what do you like to have?")
    print(cost(inp))
    if inp == "off":
        print("Turning off")
        power = False
    if inp == "report":
        print(objcofeemaker.report())
    else:
        if objcofeemaker.is_resource_sufficient(inp):
            print("enter coins")
            quarters = int(input("enter no of quarters"))
            dimes = int(input("enter no of dimes"))
            nickles = int(input("enter no of nickles"))
            pennies = int(input("enter no of pennies"))
            totalamount = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
            #if objmoneymachine.make_payment(objmenu,cost(inp)):
                

                



    