"""
CODE ASSIGNMENT 1
Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value
detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
+++

CODE ASSIGNMENT 2
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.
"""


def addToInventory(currentInventory, addedItems) -> dict:
    """
    Function to add items from a list to a dict with the count of number of items included in list
    :param currentInventory: The items that are in the character inventory before adding items
    :type currentInventory: dict
    :param addedItems: Items that are to be added to the character inventory
    :type addedItems: list
    :return: dict
    """
    for item in addedItems:
        currentInventory.setdefault(item, 0)
        currentInventory[item] += 1

    return currentInventory


def displayInventory(inventoryDict) -> None:
    """
    Function to take a dictionary with integers as values, display the count of the values with their associated key, and provide a total sum of all the values.
    :param inventoryDict: The items that are in the character inventory with their quantity
    :type inventoryDict: dict
    :return: None
    """
    totalItemSum = 0
    print("Inventory:")
    for key, value in inventoryDict.items():
        try:
            totalItemSum += value
            print(f"{value} {key.capitalize()}")
        except TypeError:
            print(f"0 {key}")
    print(f"Total number of items: {totalItemSum}")


def main():
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    updatedInventory = addToInventory(stuff, dragonLoot)

    print()
    displayInventory(updatedInventory)


if __name__ == '__main__':
    main()
