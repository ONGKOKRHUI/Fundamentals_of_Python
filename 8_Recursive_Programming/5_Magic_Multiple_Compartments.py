'''
Task 5:
An additional file, magic_multi_containers.csv, now provides the description of containers that behave like containers with multiple compartments, and, like the other magic containers, do no increase in weight if items are stored in them. Each compartment still has a maximum capacity.

Magic containers with multiple compartments
Displaying a magic container looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Professor Farnsworth's Lab Coat (total weight: 0, empty weight: 0, capacity: 0/0)
   A small pocket (total weight: 100, empty weight: 0, capacity: 100/100)
      Pierre's daily cheese wheel (weight: 100)
      Gabe's Steam game library (weight: 0)
      Robbie's final drop of sanity (weight: 0)
   A medium pocket (total weight: 186, empty weight: 0, capacity: 186/200)
      Paul's only frontal lobe (weight: 9)
      Robbie's shower thoughts (weight: 150)
      Crimpy's destroyed cat toys (weight: 27)
   A small pocket (total weight: 27, empty weight: 0, capacity: 27/100)
      Crimpy's destroyed cat toys (weight: 27)
==================================

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container with multiple compartments, which is that it is computed and displayed at the compartment level. See Example 1 for a complete example.

Your program must retain the same functionality as in Task 4, which is to say that it should be possible to select at the beginning any of the containers covered so far. See Example 2.
'''

"""
This program allows user to loot items into different types of containers and list the items stored in each container.
"""

class Item:
    """
    Represents an item that can be looted into different type of containers.
    """
    def __init__(self,name, weight):
        """
        A function to initializes an item object with the given name and weight.
        """
        self.name = name
        self.weight = weight
        
    def __str__(self):
        """
        A function to returns a string representation of the item
        """
        return f"{self.name} (weight:{self.weight})"

class Container:
    """
    Represents a container that can store items based on its capacity
    """
    def __init__(self, name, empty_weight, weight_capacity):
        """
        A function that initialises a container object with the given name, empty_weight and weight capacity.
        """
        self.name = name
        self.empty_weight = empty_weight
        self.weight_capacity = weight_capacity
        self.capacity = 0
        self.items = []
    
    def change_capacity(self,weight):
        """
        A function that update the container capacity by adding the items weight
        """
        self.capacity = int(self.capacity)+ int(weight)
    
    def add_item(self,item):
        """
        A fucntion that adds an item to the list of the container
        """
        self.items.append(item)
    
    def get_total(self):
        """
        A function that find the total weight of the container by adding its empty weight and occupied capacity.
        """
        return int(self.empty_weight) + int(self.capacity)
    
    def loot_item(self):
        """
        A function that prompts the user to input an item name in order to loot the item into the container.
        """
        item_name = input("Enter the name of the item: ")
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                # Checking if the item's weight, combined with the current capacity, exceeds the container's limit
                if int(chosen_item_instance.weight) + int(self.capacity) <= int(self.weight_capacity):
                    self.add_item(chosen_item_instance)
                    self.change_capacity(chosen_item_instance.weight)
                    print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                    main() 
                else:
                    print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                    main()
    
    def list_looted_items(self):
        """
        A function that list out the container's details and items stored inside the container.
        """
        print(self)
        for item in self.items:
            print(f'   {item}')
        main()
    
    def __str__(self):
        """
        A function that returns a string representation of the container.
        """
        total = str(self.get_total())
        self.capacity = str(self.capacity)
        return f"{self.name} (total weight: {total.strip()}, empty weight:{self.empty_weight}, capacity: {self.capacity.strip()}/{self.weight_capacity.strip()})"

class Multi_Container(Container):
    """
    Represents a container with multiple compartments where each of the compartments can store items.
    """
    def __init__(self, name, list_of_compartment_instances):
        """
        A function that initialises a Multi_Container object with the given name and list of compartments.
        """
        self.name = name
        self.list_of_compartment_instances = list_of_compartment_instances
    
    def loot_item(self):
        """
        A function that prompts the user to input an item name in order to loot the item into the compartment with sufficient capacity.
        """
        item_name = input("Enter the name of the item: ")
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                # Loop through compartments to find the one that can store the item
                for compartment_instance in self.list_of_compartment_instances:
                    #check if the item can be stored in the compartment
                    if int(chosen_item_instance.weight) + int(compartment_instance.capacity) <= int(compartment_instance.weight_capacity):
                        compartment_instance.add_item(chosen_item_instance)
                        compartment_instance.change_capacity(chosen_item_instance.weight)
                        print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                        main()
                print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                main()
        print(f''' "{item_name}" not found. Try again.''')
        chosen_container_instance.loot_item()
    
    def list_looted_items(self):
        """
        A function that list out all the details of the multi-compartment container and the items that are stored in each compartment.
        """
        print(self)
        for compartment_instance in self.list_of_compartment_instances:
            print(f'   {compartment_instance}')
            for item in compartment_instance.items:
                print(f'      {item}')
        main()

    def __str__(self):
        """
        A function that returns a string representation of the container with multi compartment.
        """
        total = sum(instance.get_total() for instance in self.list_of_compartment_instances)
        empty_weight = sum(int(instance.empty_weight) for instance in self.list_of_compartment_instances)
        return f"{self.name} (total weight: {total}, empty weight: {empty_weight}, capacity: 0/0)"
    

class Magic_Containers:
    """
    Represents a magic container that can store items.
    """
    def __init__(self,name,empty_weight,weight_capacity):
        """
        A function that initialises a Magic_Container object with the given name, empty weight and weight capacity.
        """
        self.name = name
        self.empty_weight = empty_weight
        self.weight_capacity = weight_capacity
        self.capacity=0
        self.items=[]
    
    def add_item(self,item):
        """
        A function that adds an item into the magic container.
        """
        self.items.append(item)

    def change_capacity(self,weight):
        """
        A function that updates the current weight capacity of the magic container.
        """
        self.capacity += int(weight)

    def loot_item(self):
        """
        A function that prompts the user to input an item name in order to loot the item into the magic container.
        """
        item_name = input("Enter the name of the item: ")
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                # check if the chosen item can be stored in the container condition
                if int(chosen_item_instance.weight) + int(self.capacity) <= int(self.weight_capacity):
                    self.add_item(chosen_item_instance)
                    self.change_capacity(chosen_item_instance.weight)
                    print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                    main()
                else:
                    print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                    main()

    def list_looted_items(self):
        """
        A function that lists out all the details of the magic container and the items stored inside the magic container.
        """
        print(self)
        for item in self.items:
            print(f'   {item}')
        main()

    def __str__(self):
        """
        A function that returns a string representation of the magic container.
        """
        return f"{self.name} (total weight: {self.empty_weight}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"

class Magic_Multi_Container(Multi_Container):
    """
    Represents a magic container with multiple compartments.
    """
    def __init__(self, magic_multi_container, empty_weight,magic_multi_list_of_compartment_instances ) -> None:
        """
        A function that initialises a Magic_Multi_Containers object with the given name and list of compartments.
        """
        super().__init__(name,list_of_compartment_instances)  #inherit from Parent Container
        self.magic_multi_container = magic_multi_container
        self.empty_weight = empty_weight 
        self.magic_multi_list_of_compartment_instances = magic_multi_list_of_compartment_instances

    def loot_item(self):
        """
        A function that prompts user to input an item name in order to loot an item into the compartment of the magic_multi_container
        """
        item_name = input("Enter the name of the item: ")
        for item_instance in item_instance_list:
            if item_instance.name == item_name:
                chosen_item_instance = item_instance
                for compartment_instance in self.magic_multi_list_of_compartment_instances:
                    #check if the chosen item can be stored in the compartment
                    if int(chosen_item_instance.weight) + int(compartment_instance.capacity) <= int(compartment_instance.weight_capacity):
                        compartment_instance.add_item(chosen_item_instance)
                        compartment_instance.change_capacity(chosen_item_instance.weight)
                        print(f'''Success! Item "{item_instance.name}" stored in container "{self.name}".''')
                        main()
                print(f'''Failure! Item "{item_instance.name}" NOT stored in container "{self.name}".''')
                main()
        print(f''' "{item_name}" not found. Try again.''')
        chosen_container_instance.loot_item()

    def list_looted_items(self):
        """
        A function that lists out all items stored in each compartment of the magic multi-container.
        """
        print(self)
        for compartment_instance in self.magic_multi_list_of_compartment_instances:
            print(f'   {compartment_instance}')
            for item in compartment_instance.items:
                print(f'      {item}')
        main()

    def __str__(self):
        """
        A function that returns a string representation of the magic_multi_container.
        """
        return f"{self.name} (total weight: {self.empty_weight}, empty weight: {self.empty_weight}, capacity: 0/0)"
        


with open('items.csv') as items_file:
    """
    Reads items from CSV file and initializes Item instances.
    """
    item_list = []
    item_instance_list = []
    items_file.readline()  #skipping the headline
    for item in items_file:
        name, weight = item.strip().split(',')
        item_list.append((name, weight))
    item_list.sort()
    for item in item_list:
        item_instance_list.append(Item(item[0],item[1]))


with open('containers.csv') as containers_file:
    """
    Reads containers from CSV file and initializes Container instances.
    """
    containers_file.readline()  #skipping the headline
    container_list = []
    container_instance_list = []
    for container in containers_file:
        name, empty_weight, weight_capacity = container.strip().split(',')
        container_list.append((name, empty_weight, weight_capacity))
    container_list.sort()
    for container in container_list:
        container_instance_list.append(Container(container[0],container[1], container[2]))

with open('multi_containers.csv') as multi_containers_file:
    """
    Reads multi_containers from CSV file and initializes Multi_Container instances.
    """
    multi_containers_file.readline()    #skipping the headline
    multi_containers_instances_list =[]
    for multi_container in multi_containers_file:
        temp_list = multi_container.strip().split(',')
        name = temp_list[0].strip()
        list_of_compartment = temp_list[1:]
        list_of_compartment_instances = []
        for compartment in list_of_compartment:
            list_of_compartment_instances.extend([Container(container[0], container[1], container[2]) for container in container_list if compartment.strip() == container[0]])
        
        multi_containers_instances_list.append(Multi_Container(name,list_of_compartment_instances))

with open('magic_containers.csv') as Magic_Containers_file:
    """
    Reads magic_containers from CSV file and initializes Magic_Container instances.
    """
    Magic_Containers_file.readline()    #skipping the headline
    Magic_Containers_instances_list=[]
    for magic_container in Magic_Containers_file:
        Magic_Containers_list=[]
        name, container_name = magic_container.strip().split(',')
        for container in container_list:
            if container_name.strip()==container[0]:
                Magic_Containers_list.append(container[1:3])

        for container in Magic_Containers_list:
            Magic_Containers_instances_list.append(Magic_Containers(name.strip(),container[0].strip(),container[1].strip()))



with open('magic_multi_containers.csv') as magic_multi_containers_file:
    """
    Reads magic_multi_containers from CSV file and initializes Magic_Multi_Container instances.
    """
    magic_multi_containers_file.readline()  #skipping the headline
    magic_multi_containers_instances_list=[]
    for magic_multi_container in magic_multi_containers_file:
        name,container_name = magic_multi_container.strip().split(',')
        for container in multi_containers_instances_list:
            
            if container.name==container_name.strip():
                empty_weight = sum(int(instance.empty_weight) for instance in container.list_of_compartment_instances)
                magic_multi_list_of_compartment_instances = container.list_of_compartment_instances
                magic_multi_containers_instances_list.append(Magic_Multi_Container(name, empty_weight, magic_multi_list_of_compartment_instances))

       



print(f'Initialised {len(item_list)+len(container_list)+len(multi_containers_instances_list)+len(Magic_Containers_instances_list)+len(magic_multi_containers_instances_list)} items including {len(container_list)+len(multi_containers_instances_list)+len(Magic_Containers_instances_list)+len(magic_multi_containers_instances_list)} containers.\n')

if __name__ == '__main__':
    def find_container():
        """
        A function that prompts the user to input a container name.
        """
        container_name=  input('Enter the name of the container: ')
        for container_instance in container_instance_list:
            if container_instance.name == container_name:
                global chosen_container_instance
                chosen_container_instance = container_instance
                main()
        for multi_container_instance in multi_containers_instances_list:
            if multi_container_instance.name == container_name:
                chosen_container_instance = multi_container_instance
                main()
        for Magic_Containers_instance in Magic_Containers_instances_list:
            if Magic_Containers_instance.name == container_name:
                chosen_container_instance = Magic_Containers_instance
                main()
        for magic_multi_containers_instance in magic_multi_containers_instances_list:
            if magic_multi_containers_instance.name == container_name:
                chosen_container_instance = magic_multi_containers_instance
                main()
        print(container_name.strip() , 'not found. Try again.')
        find_container()

    def main():
        """
        A function that displays the main menu for the user to choose actions: loot items, list looted items, or quit.
        """
        print('==================================')
        print('Enter your choice:')
        print('1. Loot item.')
        print('2. List looted items.')
        print('0. Quit.')
        print('==================================')
        choice  = input()
        if choice == '1':
            chosen_container_instance.loot_item()   
        elif choice == '2':
            chosen_container_instance.list_looted_items()
        elif choice == '0':
            quit()
        else:
            main() # recursive request if input is not relevant


find_container()







