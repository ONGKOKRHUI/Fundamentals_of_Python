'''
Task 4:
An additional file, magic_containers.csv, now provides the description of containers that behave like containers with a single compartment, but that do no increase in weight if items are stored in them. They still have a maximum capacity, though.

Magic containers
Displaying a magic container looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Bag of Holding (total weight: 40, empty weight: 40, capacity: 4910/5000)
   A normal cheese platter (weight: 1000)
   Elena's fishing count (weight: 3500)
   Tan's Tamagotchi Support Group (weight: 410)
   Pierre's funny meme collection (weight: 0)

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container. See Example 1 for a complete example.

Your program must retain the same functionality as in Task 3, which is to say that it should be possible to select at the beginning any of the containers covered so far. See Example 2.
'''
"""
This program manages a container system where users can loot items into a container, multi container or magic multi container. 
It allows for the storage and listing of items based on their weight, ensuring that the total weight 
in each container does not exceed its capacity.
"""

class Item:
    """
    Represents an item with name and weight.
    """
    def __init__(self, name, weight):
        """
        Initializes an Item with name and weight
        """
        self.name = name
        self.weight = int(weight)
        
    def __str__(self):
        """
        Returns a string representation of the Item when printed
        """
        return f"{self.name} (weight: {self.weight})"

class Container:
    """
    Represents a container that can hold items with tangible weight
    """
    def __init__(self, name, empty_weight, weight_capacity):
        """
        Initializes a Container with name, empty weight, and weight capacity
        """
        self.name = name
        self.empty_weight = int(empty_weight)
        self.weight_capacity = int(weight_capacity)
        self.capacity = 0
        self.items = []
    
    def change_capacity(self, weight):
        """
        Updates the current capacity of the container.
        """
        self.capacity = self.capacity + int(weight)
    
    def add_item(self, item):
        """
        Adds an item to the container.
        """
        self.items.append(item)
    
    def get_total(self):
        """
        Calculates the total weight of the container, including its items.
        """
        return self.empty_weight + self.capacity
    
    def loot_item(self):
        """
        Allows the user to loot an item into the container if it fits within the weight capacity
        """
        item_name = input("Enter the name of the item: ")
        
        # Iterates through the global list of item instances to find the one that matches the input name.
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                
                # Checks if the item's weight can fit into the container without exceeding its capacity.
                if chosen_item_instance.weight + self.capacity <= self.weight_capacity:
                    self.add_item(chosen_item_instance)
                    self.change_capacity(chosen_item_instance.weight)
                    print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                    main()
                else:
                    print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                    main() 
    
    def list_looted_items(self):
        """
        Lists all looted items currently stored in the container.
        """
        print(self)
        
        # Loops through all the items in the container and prints them.
        for item in self.items:
            print(f'   {item}')
        main()  # Calls the main menu again after listing items.
    
    def __str__(self):
        """
        Returns a string representation of the Container, including its total weight, empty weight, and capacity.
        """
        total = self.get_total()
        return f"{self.name} (total weight: {total}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"

class Multi_Container(Container):
    """
    Represents a multi-compartment container that can hold multiple smaller containers
    """
    def __init__(self, name, list_of_compartment_instances):
        """
        Initializes a Multi_Container with a name and a list of compartment instances
        """
        self.name = name
        self.list_of_compartment_instances = list_of_compartment_instances
    
    def loot_item(self):
        """
        Allows the user to loot an item into one of the compartments of the multi-container.
        Then checks each compartment for available capacity.
        """
        item_name = input("Enter the name of the item: ")
        
        # Iterates through the global list of item instances to find the one that matches the input name.
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                
                # Iterates through all compartments and tries to fit the item in the first compartment with enough space.
                for compartment_instance in self.list_of_compartment_instances:
                    if chosen_item_instance.weight + compartment_instance.capacity <= compartment_instance.weight_capacity:
                        compartment_instance.add_item(chosen_item_instance)
                        compartment_instance.change_capacity(chosen_item_instance.weight)
                        print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                        main()
                        return  # Returns to exit the method once the item is successfully stored.
                
                # If no compartment has enough space, print a failure message.
                print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                main()
                return
        
        # If the item is not found, prompt the user to try again.
        print(f'"{item_name}" not found. Try again.')
        chosen_container_instance.loot_item()  # Recalls the loot method to re-enter a valid item name.
    
    def list_looted_items(self):
        """
        Lists all looted items stored in each compartment of the multi-container
        """
        print(self)
        
        # Lists each compartment and its items.
        for compartment_instance in self.list_of_compartment_instances:
            print(f'   {compartment_instance}')
            for item in compartment_instance.items:
                print(f'      {item}')
        main()

    def __str__(self):
        """
        Returns a string representation of the Multi_Container, including total weights and capacities of its compartments.
        """
        # Calculates the total weight and empty weight of all compartments in the multi-container.
        total = sum(instance.get_total() for instance in self.list_of_compartment_instances)
        empty_weight = sum(instance.empty_weight for instance in self.list_of_compartment_instances)
        return f"{self.name} (total weight: {total}, empty weight: {empty_weight}, capacity: 0/0)"

class Magic_Containers(Container):
    """
    Represents a magic container with no weight but a max capacity
    """
    def __str__(self):
        """
        Returns a string representation of the Magic_Container
        """
        return f"{self.name} (total weight: {self.empty_weight}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"


with open('items.csv') as items_file:
    """
    Reads items from a CSV file and initializes Item instances
    """
    item_list = []
    item_instance_list = []
    items_file.readline()  # Skip header line
    for item in items_file:
        name, weight = item.strip().split(',')
        item_list.append((name, weight))
    item_list.sort()
    for item in item_list:      
        item_instance_list.append(Item(item[0], item[1]))

with open('containers.csv') as containers_file:
    """
    Reads containers from a CSV file and initializes Container instances
    """
    containers_file.readline()  # Skip header line
    container_list = []
    container_instance_list = []
    for container in containers_file:
        name, empty_weight, weight_capacity = container.strip().split(',')
        container_list.append((name, empty_weight, weight_capacity))
    container_list.sort()
    for container in container_list:
        container_instance_list.append(Container(container[0], container[1], container[2]))

with open('multi_containers.csv') as multi_containers_file:
    """
    Reads multi-containers from a CSV file and initializes Multi_Container instances
    """
    multi_containers_file.readline()  # Skip header line
    multi_containers_instances_list = []
    for multi_container in multi_containers_file:
        temp_list = multi_container.strip().split(',')
        name = temp_list[0].strip()
        list_of_compartment = temp_list[1:]
        list_of_compartment_instances = []
        # Matches compartments from the list of container instances.
        for compartment in list_of_compartment:
            list_of_compartment_instances.extend([Container(container[0], container[1], container[2]) for container in container_list if compartment.strip() == container[0]])
        # Creates a Multi_Container instance using the matched compartments.
        multi_containers_instances_list.append(Multi_Container(name, list_of_compartment_instances))

with open('magic_containers.csv') as Magic_Containers_file:
    """
    Reads magic-containers from a CSV file and initializes Magic_Container instances
    """
    Magic_Containers_file.readline()    # Skip header line
    Magic_Containers_instances_list=[]
    for magic_container in Magic_Containers_file:
        Magic_Containers_list=[]
        name, container_name = magic_container.strip().split(',')
        for container in container_list:
            if container_name.strip()==container[0]:
                Magic_Containers_list.append(container[1:3])
        for container in Magic_Containers_list:
            Magic_Containers_instances_list.append(Magic_Containers(name.strip(),container[0].strip(),container[1].strip()))

print(f'Initialised {len(item_list) + len(container_list) + len(multi_containers_instances_list) + len(Magic_Containers_instances_list)} items including {len(container_list) + len(multi_containers_instances_list) + len(Magic_Containers_instances_list)} containers.\n')

if __name__ == '__main__':
    def find_container():
        """
        Prompts the user to input a container name and searches for it among available containers
        """
        container_name = input('Enter the name of the container: ')
        
        # Searches the regular container list for a match with the input name.
        for container_instance in container_instance_list:
            if container_instance.name == container_name:
                global chosen_container_instance
                chosen_container_instance = container_instance
                main()  # Calls the main menu.
        # Searches the multi-container list if no regular container matches.
        for multi_container_instance in multi_containers_instances_list:
            if multi_container_instance.name == container_name:
                chosen_container_instance = multi_container_instance
                main()
        # Searches the magic-container list if no regular container matches.
        for Magic_Containers_instance in Magic_Containers_instances_list:
            if Magic_Containers_instance.name == container_name:
                chosen_container_instance = Magic_Containers_instance
                main()
        print(container_name.strip(), 'not found. Try again.')
        find_container()

    def main():
        """
        Displays the main menu for the user to choose actions: loot items, list looted items, or quit
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


