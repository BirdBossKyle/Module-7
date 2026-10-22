# Kyle Hartley
# IT-140 Project Two: Wasteland Run
# A text-based post-apocalyptic survival adventure game.

def show_instructions():
    """Display the game story and available commands."""
    print("\n" + "=" * 50)
    print("WASTELAND RUN")
    print("Search the ruins for seven supplies and defeat the Raider Leader.")
    print("Commands: north, south, east, west, get item, quit")
    print("To collect an item, enter 'get item' and then type its name.")
    print("=" * 50)


def show_status(current_room, inventory, rooms):
    """Display the player's location, inventory, and any item in the room."""
    print("\n" + "-" * 50)
    print(f"You are in: {current_room}")
    print(f"Inventory: {inventory}")

    room_item = rooms[current_room].get("item")
    if room_item is not None:
        print(f"You see: {room_item}")
    elif current_room == "Command Bunker":
        print("The Raider Leader is here!")
    else:
        print("There are no supplies left to collect in this room.")

    print("-" * 50)


def get_item(current_room, inventory, rooms):
    """Let the player collect the current room's item, if one is available."""
    room_item = rooms[current_room].get("item")

    if current_room in ("Survivor Shelter", "Command Bunker") or room_item is None:
        print("There is no item to collect in this room.")
        return

    print(f"This room has: {room_item}")
    item_command = input("Enter the item name to collect it, or enter 'back': ")
    item_command = item_command.strip().lower()

    if item_command == room_item.lower():
        inventory.append(room_item)
        rooms[current_room]["item"] = None
        print(f"You collected {room_item}.")
        print(f"You have collected {len(inventory)} of 7 items.")
    elif item_command == "back":
        print("You did not collect an item.")
    else:
        print("That item is not in this room. Nothing was added to your inventory.")


def main():
    """Run the main game loop until the player quits, wins, or loses."""
    # Each room lists its valid exits and its item, if it has one.
    rooms = {
        "Survivor Shelter": {
            "north": "Abandoned Store",
            "east": "Clinic",
            "item": None,
        },
        "Abandoned Store": {
            "south": "Survivor Shelter",
            "east": "Radio Tower",
            "item": "Canned Food",
        },
        "Clinic": {
            "west": "Survivor Shelter",
            "east": "Gas Station",
            "item": "Medical Kit",
        },
        "Radio Tower": {
            "west": "Abandoned Store",
            "east": "Ruined School",
            "item": "Radio Battery",
        },
        "Gas Station": {
            "west": "Clinic",
            "east": "Water Plant",
            "item": "Fuel Can",
        },
        "Ruined School": {
            "west": "Radio Tower",
            "east": "Highway Checkpoint",
            "item": "Map",
        },
        "Water Plant": {
            "west": "Gas Station",
            "east": "Command Bunker",
            "item": "Water Filter",
        },
        "Highway Checkpoint": {
            "west": "Ruined School",
            "item": "Protective Gear",
        },
        "Command Bunker": {
            "west": "Water Plant",
            "item": None,
        },
    }

    current_room = "Survivor Shelter"
    inventory = []
    required_item_count = 7
    game_is_running = True

    show_instructions()

    while game_is_running:
        show_status(current_room, inventory, rooms)
        command = input(
            "Enter your move (north, south, east, west, get item, or quit): "
        )
        command = command.strip().lower()

        if command == "quit":
            print("You leave the wasteland. Game ended.")
            game_is_running = False

        elif command == "get item":
            get_item(current_room, inventory, rooms)

        elif command in ("north", "south", "east", "west"):
            next_room = rooms[current_room].get(command)

            if next_room is None:
                print("You cannot go that way from this room.")
            else:
                current_room = next_room
                print(f"You moved to {current_room}.")

                # Entering the villain's room ends the game immediately.
                if current_room == "Command Bunker":
                    if len(inventory) == required_item_count:
                        print(
                            "\nCongratulations! You collected all seven supplies "
                            "and defeated the Raider Leader. You win!"
                        )
                    else:
                        print(
                            "\nThe Raider Leader catches you before you collected "
                            "all seven supplies. You lose."
                        )
                    print("Thanks for playing Wasteland Run.")
                    game_is_running = False

        else:
            print(
                "Invalid command. Enter north, south, east, west, "
                "get item, or quit."
            )

    print("Game over.")


if __name__ == "__main__":
    main()
