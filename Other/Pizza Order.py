print('Hello user welcome to Pizzaorderer 2000, help to get a list of commands')
print('')
print('Please chose your pizza base (Thick, Medium, Thin)')
base = input()
print('Please chose your pizza sauce (Tomato, BBQ)')
sauce = input()
print('Please chose your first pizza topping (Chicken, Ham, Steak. Sweetcorn, Mushrooms, Onions, Pineapple')
topping_1 = input()
if topping_1 == 'pineapple':
    print('Incorrect Pleas choose another topping')
    topping_1 = input()
print('Please chose your first pizza topping (Chicken, Ham, Steak. Sweetcorn, Mushrooms, Onions, Pineapple')
topping_2 = input()
if topping_2 == 'pineapple':
    print('Incorrect Pleas choose another topping')
    topping_2 = input()

print('You have selected a ' + base + ' pizza with a ' + sauce + ' sauce, ' + topping_1 + ' and ' + topping_2)
print()
print('Please confirm your order by typing checkout, if you would like to change your order type change')
checkout = input()
if checkout == 'checkout':
    print('Thank you for placing your order, Your order has been submitted  and your pizza will be with you shortly')
else:
    print('Please chose your pizza base (Thick, Medium, Thin)')
    base = input()
    print('Please chose your pizza sauce (Tomato, BBQ)')
    sauce = input()
    print('Please chose your first pizza topping (Chicken, Ham, Steak. Sweetcorn, Mushrooms, Onions, Pineapple')
    topping_1 = input()
    if topping_1 == 'pineapple':
        print('Incorrect Pleas choose another topping')
        topping_1 = input()
    print('Please chose your first pizza topping (Chicken, Ham, Steak. Sweetcorn, Mushrooms, Onions, Pineapple')
    topping_2 = input()
    if topping_2 == 'pineapple':
        print('Incorrect Pleas choose another topping')
        topping_2 = input()
    print('You have selected a ' + base + ' pizza with a ' + sauce + ' sauce, ' + topping_1 + ' and ' + topping_2)
    print()
    print('Please confirm your order by typing checkout, if you would like to change your order type change')
    checkout = input()
    if checkout == 'checkout':
        print('Thank you for placing your order, Your order has been submitted  and your pizza will be with you shortly')
