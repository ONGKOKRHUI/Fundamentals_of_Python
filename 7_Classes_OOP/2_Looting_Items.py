'''
Task 2:
After reading all items and containers, do not print them, but instead ask the user for a container to pick for the adventure. For example,

Enter the name of the container: A backpack
Main menu
Then, a menu with three options will be shown repeatedly. The program prompt of the main menu looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1. Loot item.
Upon entering 1, the program will then ask for the name of an item to loot. If the item can fit in the container given the remaining capacity, the program indicates so, as shown below.

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".

If, instead, the remaining capacity is not sufficient to store the item, the item is not looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".

If the item's name is not one of the known items, then the user is asked for the name again:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".

See example 1 for a complete example.

Consider using exceptions (including custom ones) to handle the case where a container cannot store an item.

2. List looted items.
Upon entering 2, the program will then print the container and the list of content, in the order they have been looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)

Notice how the total weight and capacity of the backpack are updated based on the contents.
'''

"""
This program manages items and containers, allowing users to loot items into containers
while keeping track of their weight and capacity.
"""

class Item:
    """
    Represents an item with a name and weight.
    """
    def __init__(self, name, weight):
        """
        Initializes an Item with a name and weight
        """
        self.name = name
        self.weight = weight
        
    def __str__(self):
        """
        Returns a string representation of the Item when printed
        """
        return f"{self.name} (weight:{self.weight})"

class Container:
    """
    Represents a container that can contain items
    """
    def __init__(self, name, empty_weight, weight_capacity):
        """
        Initializes a Container with a name, empty weight, and weight capacity.
        """
        self.name = name
        self.empty_weight = int(empty_weight)
        self.weight_capacity = int(weight_capacity)
        self.capacity = 0  # Initialise current weight of items in the container
        self.items = []    # List to store looted items
    
    def change_capacity(self, weight):
        """
        Updates the capacity of the container after adding a new item.
        """
        self.capacity = self.capacity + int(weight)
    
    def add_item(self, item):
        """
        Adds an item to the container's list of items.
        """
        self.items.append(item)
    
    def loot_item(self):
        """
        Allows the user to loot an item by its name, checking if it fits in the container.
        Prompts the user for an item name and updates the container accordingly.
        """
        item_name = input("Enter the name of the item: ")
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                # Check if adding the item exceeds weight capacity
                if int(chosen_item_instance.weight) + int(self.capacity) <= int(self.weight_capacity):
                    self.add_item(chosen_item_instance)
                    self.change_capacity(chosen_item_instance.weight)
                    print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                    main()  
                else:
                    print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                    main() 
        print(f''' "{item_name}" not found. Try again.''')
        chosen_container_instance.loot_item()  # Retry if the item was not found
    
    def list_looted_items(self):
        """
        Lists all items in the container.
        """
        print(f"{chosen_container_instance}")
        for item in self.items:
            print(f'   {item}')
        main()  
    
    def __str__(self):
        """
        Returns a string representation of the Container, including total weight and capacity details.
        """
        total = self.empty_weight + self.capacity
        return f"{self.name} (total weight: {total}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"


with open('items.csv') as items_file:
    """
    Reads item data from 'items.csv' and creates Item instances.
    """
    item_list = []
    item_instance_list = []
    items_file.readline()  # Skip header line
    for item in items_file:
        name, weight = item.strip().split(',')
        item_list.append((name, weight))
    item_list.sort()  # Sort items by name
    for item in item_list:
        item_instance_list.append(Item(item[0], item[1]))

with open('containers.csv') as containers_file:
    """
    Reads container data from 'containers.csv' and initializes Container instances.
    """
    containers_file.readline()  # Skip header line
    container_list = []
    container_instance_list = []
    for container in containers_file:
        name, empty_weight, weight_capacity = container.strip().split(',')
        container_list.append((name, empty_weight, weight_capacity))
    container_list.sort()  # Sort containers by name
    for container in container_list:
        container_instance_list.append(Container(container[0], container[1], container[2]))

print(f'Initialised {len(item_list) + len(container_list)} items including {len(container_list)} containers.\n')

if __name__ == '__main__':
    def find_container():
        """
        Prompts the user to enter a container name and finds the corresponding Container instance.
        """
        container_name = input('Enter the name of the container: ')
        for container_instance in container_instance_list:
            if container_instance.name == container_name:
                global chosen_container_instance
                chosen_container_instance = container_instance
                main()  
        print(f'''"{container_name}" not found. Try again.''')
        find_container()  # Retry if the container was not found

    def main():
        """
        Displays the main menu and handles user input for looting items or listing items.
        """
        print('==================================')
        print('Enter your choice:')
        print('1. Loot item.')
        print('2. List looted items.')
        print('0. Quit.')
        print('==================================')
        choice = input()
        if choice == '1':
            chosen_container_instance.loot_item()
        elif choice == '2':
            chosen_container_instance.list_looted_items()  
        elif choice == '0':
            quit()
        else:
            main() 
    
find_container()


