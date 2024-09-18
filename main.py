def select_dish(foods, selected_food):
    if selected_food <= 0:
        raise IndexError("Pick a number between 1 and 5")
    print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1
   
        selected_choice = int(input("Your order number? "))

        select_dish(foods, selected_choice - 1)
    except IndexError as error:
        print(f"{selected_choice} was entered. {error}")
        # print("Next time try entering something on the menu! Between 1 and 5")
    except ValueError as error:
        print(f"{error} was entered.")
        print("Enter a number, please.")

    
menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")