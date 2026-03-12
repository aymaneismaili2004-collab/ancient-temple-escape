from .data import rooms

inventory = []
current_room = "Entrance"
player_health = 100
max_health = 100
potions = 1
score = 0
turns = 0
counter_mode = False
game_running = True


def show_instructions():
    print("""
Ancient Temple Escape
=====================

Commands:
go [direction]
get [item]
attack
heal
counter
status
inventory
map
help
quit
""")


def show_map():
    print("""
Temple Map
==========

          [Treasure Room]
                |
[Entrance] -> [Dark Chamber] -> [Shadow Corridor]
     |                                 |
     v                                 v
[Sacred Room] ------------------> [Exit Gate]
""")


def show_status():
    print("---------------------------")
    print("Location:", current_room)
    print("Health:", player_health, "/", max_health)
    print("Potions:", potions)
    print("Score:", score)
    print("Turns:", turns)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])

    if "enemy" in rooms[current_room]:
        enemy = rooms[current_room]["enemy"]
        print("Enemy:", enemy["name"], "| HP:", enemy["health"], "| Attack:", enemy["attack"])

    print("---------------------------")


def show_room_intro():
    print()
    print("You entered:", current_room)

    if current_room == "Entrance":
        print("A cold wind blows through the temple entrance.")
    elif current_room == "Dark Chamber":
        print("The chamber is silent, but danger is near.")
    elif current_room == "Sacred Room":
        print("Ancient symbols glow faintly on the walls.")
    elif current_room == "Shadow Corridor":
        print("The corridor is dark and filled with cursed energy.")
    elif current_room == "Treasure Room":
        print("A hidden room of forgotten treasures lies before you.")
    elif current_room == "Exit Gate":
        print("The final gate stands before you. One last enemy blocks the path.")


def enemy_attack():
    global player_health, counter_mode

    if "enemy" not in rooms[current_room]:
        return

    enemy = rooms[current_room]["enemy"]
    damage = enemy["attack"]

    if counter_mode:
        reflected = damage // 2
        reduced = damage // 2
        player_health -= reduced
        enemy["health"] -= reflected
        print(f"You countered the attack. You took {reduced} damage and reflected {reflected} damage.")
        counter_mode = False
    else:
        player_health -= damage
        print(f"{enemy['name']} attacked you for {damage} damage.")


def check_enemy_defeat():
    global score

    if "enemy" in rooms[current_room]:
        enemy = rooms[current_room]["enemy"]

        if enemy["health"] <= 0:
            print(f"You defeated {enemy['name']}.")
            del rooms[current_room]["enemy"]
            score += 15


def check_win():
    required_items = {"ancient_relic", "healing_scroll", "golden_idol"}

    return (
        current_room == "Exit Gate"
        and "enemy" not in rooms[current_room]
        and required_items.issubset(set(inventory))
    )


def check_loss():
    return player_health <= 0


def process_go(direction):
    global current_room

    if "enemy" in rooms[current_room]:
        print("You cannot leave while an enemy is blocking your way.")
        return

    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        show_room_intro()
    else:
        print("You can't go that way.")


def process_get(item_name):
    global score, potions

    if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
        inventory.append(item_name)
        print(item_name, "obtained.")
        del rooms[current_room]["item"]
        score += 5

        if item_name == "healing_scroll":
            potions += 1
            print("The healing scroll grants you one extra potion.")
    else:
        print("Can't get", item_name)


def process_attack():
    if "enemy" not in rooms[current_room]:
        print("There is no enemy here.")
        return

    enemy = rooms[current_room]["enemy"]
    damage = 15
    enemy["health"] -= damage
    print(f"You attacked {enemy['name']} for {damage} damage.")
    check_enemy_defeat()

    if "enemy" in rooms[current_room]:
        enemy_attack()


def process_heal():
    global player_health, potions

    if potions <= 0:
        print("You have no potions left.")
        return

    heal_amount = 20
    player_health += heal_amount

    if player_health > max_health:
        player_health = max_health

    potions -= 1
    print(f"You healed for {heal_amount} HP.")

    if "enemy" in rooms[current_room]:
        enemy_attack()


def process_counter():
    global counter_mode

    if "enemy" not in rooms[current_room]:
        print("There is no enemy here.")
        return

    counter_mode = True
    print("You prepare to counter the next attack.")
    enemy_attack()
    check_enemy_defeat()


def process_command(move):
    global game_running

    if move.startswith("go "):
        direction = move.split(" ", 1)[1]
        process_go(direction)

    elif move.startswith("get "):
        item_name = move.split(" ", 1)[1]
        process_get(item_name)

    elif move == "attack":
        process_attack()

    elif move == "heal":
        process_heal()

    elif move == "counter":
        process_counter()

   elif move == "status":
    print("Status is displayed automatically each turn.")

    elif move == "inventory":
        print("Inventory:", inventory)

    elif move == "map":
        show_map()

    elif move == "help":
        show_instructions()

    elif move == "quit":
        print("You abandoned the temple expedition.")
        game_running = False

    else:
        print("Invalid command. Type 'help' to see the command list.")


def play_game():
    global turns, game_running

    show_instructions()
    show_room_intro()

    while game_running:
        show_status()

        move = input("> ").strip().lower()

        if move == "":
            continue

        turns += 1
        process_command(move)

        if not game_running:
            break

        if check_loss():
            print("You were defeated... GAME OVER.")
            print("Final score:", score)
            print("Total turns:", turns)
            break

        if check_win():
            print("You defeated the final boss and escaped the temple with all sacred items.")
            print("YOU WIN.")
            print("Final score:", score)
            print("Total turns:", turns)
            break