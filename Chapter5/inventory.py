"""
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
"""


def displayInventory(inventoryList) -> None:
    """
    Function to take a dictionary with integers as values, display the count of the values with their associated key, and provide a total sum of all the values.
    :param inventoryList: dict
    :return: None
    """
    totalItemSum = 0
    print("Inventory:")
    for key, value in inventoryList.items():
        try:
            totalItemSum += value
            print(f"{value} {key.capitalize()}")
        except TypeError:
            print(f"0 {key}")
    print(f"Total number of items: {totalItemSum}")


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 55, 'arrow': 12}
    displayInventory(stuff)


if __name__ == '__main__':
    main()