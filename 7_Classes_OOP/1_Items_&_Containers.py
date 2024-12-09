'''
Task 1:
Write a program that reads items and containers from files items.csv and containers.csv, and prints the list of items.

For this and following tasks, do not create files or write into existing files.

As in previous assignments, you are allowed to use any standard Python feature and module. In particular, sorted can be useful here.

We recomend you read all tasks to plan the design of your program so as to minimise the refactoring effort from task to task.

Items
An item has:

a name, and

a weight.

We recommend you create a class to represent items.

Containers
A container has: 

a name,

an empty weight, i.e. their weight when they are empty, and

a weight capacity, i.e. the maximum combined weight that the container can hold.

- Two copies of the same item or container can exist. If two items or containers have the same name, then they have the same characteristics (e.g. weight).
- Throughout the assignment, all weights and weight-related measures (i.e. weight capacities) are non-negative integers.

We recommend you create a class to represent containers.
'''

"""
This program defines two classes, Item and Container, to represent items and containers 
then reads out all items and instances and print their details.
"""

class Item:
    """
    Represents an item with a name and weight.
    """
    
    def __init__(self, name, weight):
        """
        Initializes Item with a name and weight.
        """
        self.name = name
        self.weight = int(weight)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the Item when printed
        """
        return f"{self.name} (weight: {self.weight})"

class Container:
    """
    Represents a container that holds items with an empty weight and weight capacity.
    """

    def __init__(self, name, empty_weight, weight_capacity):
        """
        Initializes a Container with a name, empty weight, and weight capacity.
        """
        self.name = name
        self.empty_weight = int(empty_weight)
        self.weight_capacity = int(weight_capacity)
        self.capacity = 0  # Initialize current capacity to zero
    
    def change_capacity(self, weight):
        """
        Updates the current capacity of the Container by adding a weight.
        """
        self.capacity += int(weight)  # Increase the current capacity by the given weight
    
    def __str__(self):
        """
        Returns a string representation of the Container when printed
        """
        total = self.empty_weight + self.capacity  # Calculate total weight
        return f"{self.name} (total weight: {total}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"



with open('items.csv') as items_file:
    """
    Reads item data from 'items.csv' and creates Item instances.
    """
    item_list = []
    item_instance_list = []
    items_file.readline()  # Skip header line
    for item in items_file:
        name, weight = item.strip().split(',')  # Split each line into name and weight
        item_list.append((name, weight))
    item_list.sort()  # Sort items by name
    for item in item_list:
        item_instance_list.append(Item(item[0], item[1]))  # Create Item instances

with open('containers.csv') as containers_file:
    """
    Reads container data from 'containers.csv' and initializes Container instances.
    """
    containers_file.readline()  # Skip header line
    container_list = []
    container_instance_list = []
    for container in containers_file:
        name, empty_weight, weight_capacity = container.strip().split(',')  # Split into 3 components
        container_list.append((name, empty_weight, weight_capacity))
    container_list.sort()  # Sort containers by name
    for container in container_list:
        container_instance_list.append(Container(container[0], container[1], container[2]))  # Create Container instances

print(f'Initialised {len(item_list) + len(container_list)} items including {len(container_list)} containers.\n')

print("Items:")
for item in item_instance_list:
    print(item)
print() 
print("Containers:")
for container in container_instance_list:
    print(container)
print()


