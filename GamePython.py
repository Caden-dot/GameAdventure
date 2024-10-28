def main():
    """
    Main game loop where players you can purchase items,
    explore, look at the shop sign, or quitting the game.
    """
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

