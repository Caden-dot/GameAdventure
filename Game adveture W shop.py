import random

# print welcome function
def print_welcome(name: str, width: int = 20):
   
    message = f"Hello, {name}!"
    print(f"'{message:^{width}}'")

# print shop menu function
def print_shop_menu(item1, item2, item3):
    
    print(f"Welcome to the shop! Here are your options:")
    print(f"1. {item1} - 50 gold coins")
    print(f"2. {item2} - 100 gold coins")
    print(f"3. {item3} - 150 gold coins")
    print()

# print shop sign function
def print_shop_sign(item1, price1, item2, price2):
   
    border = "+" + "-" * 30 + "+"
    print(border)
    print("| Shop Items                |")
    print(border)
    print(f"| {item1:<12} ${price1:>7.2f} |")
    print(f"| {item2:<12} ${price2:>7.2f} |")
    print(border)
    print()

# purchase item function
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
   
    max_quantity = int(startingMoney // itemPrice)
    quantity_purchased = min(quantityToPurchase, max_quantity)
    remaining_money = startingMoney - (quantity_purchased * itemPrice)
    return quantity_purchased, remaining_money

# new random monster function
def new_random_monster():
   
    monster_names = ['Goblin', 'Giant Spider', 'Shrek']
    name = random.choice(monster_names)
    if name == 'Goblin':
        health = random.randint(10, 20)
        power = random.randint(5, 10)
        money = round(random.uniform(5, 15), 2)
        description = "In the distance you spot a lone goblin It notices you and rushes at you quickly with a sword"
    elif name == 'Giant Spider':
        health = random.randint(100, 200)
        power = random.randint(30, 50)
        money = round(random.uniform(200, 1500), 2)
        description = "You are exploring a giant cave and stumble across a giant spider this spider has a giant web with the remains adventurers before you; you could be rich"
    elif name == 'Shrek':
        health = random.randint(30, 50)
        power = random.randint(15, 25)
        money = round(random.uniform(10, 50), 2)
        description = "A huge ogre blocks your path and says You are in my swamp A donkey comes out from behind him with a suit of donkey armor ready to fight you."
    return {'name': name, 'description': description, 'health': health, 'power': power, 'money': money}

# game main function
def main():
  
    player_name = input("Enter your name: ")
    print_welcome(player_name)

    player_money = 50.0  # starting money
    playing = True
    while playing:
        print("\nYou have ${:.2f}.".format(player_money))
        print("What would you like to do?")
        print("1. Purchase an item")
        print("2. Explore")
        print("3. Quit")
        print("4. Shop Sign")
        choice = input("Enter your choice (1, 2, 3, 4): ")
        if choice == '1':
            item_price = float(input("\nEnter price of item to purchase: "))
            quantity = int(input("Enter quantity to purchase: "))
            num_purchased, player_money = purchase_item(item_price, player_money, quantity)
            print(f"\nYou purchased {num_purchased} item(s). You have ${player_money:.2f} left.")
        elif choice == '2':
            print("\nYou are about to encounter a monster")
            monster = new_random_monster()
            print(f"\nA {monster['name']} appears!")
            print(f"Description: {monster['description']}")
            print(f"Health: {monster['health']}, Power: {monster['power']}, Money: ${monster['money']:.2f}")
            fight_choice = input("\nDo you want to fight the monster? (yes/no): ")
            if fight_choice == 'yes':
                print(f"\nYou fight with the {monster['name']}!")
                if random.random() > 0.5:  # 50% chance of winning
                    print(f"You defeated the {monster['name']} and gained ${monster['money']:.2f}!")
                    player_money += monster['money']
                else:
                    print(f"The {monster['name']} defeated you! You escaped.")
            else:
                print(f"\nYou were scared and didn't fight the {monster['name']}.")
        elif choice == '3':
            print("\nGoodbye")
            playing = False
        elif choice == '4':
            # shop sign
            print_shop_sign("Sword", 50.0, "Shield", 75.0)
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
