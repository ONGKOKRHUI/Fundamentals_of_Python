'''
Task 6:
Expand your program so that:

Containers can be looted and stored just like other items.

When looting and storing an item (including containers), it is placed in the first possible container:

if it can be stored in the current container, it is,

otherwise, containers (and other containers within) placed in the current container are tested in the order in which they were stored to determine if the item can be stored there, and

any container inside the current container is tested before any container at the same level as the current container.

Items more than one level inside a container affect the weight of all containers containing this item (but a magic container will also affect this). This means that if item X is put in non-magic container B, itself inside non-magic container A, then the weight of X both applies to A and B, and they both must have enough capacity. However, if B is magic, then the weight of X only applies to B. See Examples 1 and 2.

This type of recursive search is called a preorder depth-first search.
'''

"""
This program allows users to store items (or containers) into various types of containers. 
These include regular containers, multi-containers, magic containers, and magic multi-containers
It also lists all items (and containers) stored in a container
"""
import copy 

class Items: 
    """
    Represents an item that can be looted into containers.
    """
    def __init__(self, name, weight):
        """
        Initializes an Item object with the specified name and weight.
        """
        self.name = name
        self.weight = int(weight)
        self.indentation = 0

    def indent(self, looted_object):
        """
        A method to track the number of indentations when stored in other containers
        """
        self.indentation = looted_object.indentation + 1   

    def __str__(self):
        """
        Returns a string representation of the Item.
        """
        output = "   " * self.indentation + f"{self.name} (weight: {self.weight})"
        return output

class Containers:
    """
    Represents a container that can store items or other type of containers
    """
    def __init__(self, name, weight, weight_capacity):
        """
        Initializes a Container object with the specified name, empty weight, and weight capacity.
        """
        self.name = name
        self.weight = int(weight)
        self.empty_weight = int(weight)
        self.capacity = 0
        self.weight_capacity = int(weight_capacity)
        self.indentation = 0        #initialise indentation level to 0
        self.list_of_items = []
        for item in self.list_of_items: 
            item.indentation = self.indentation + 1 
       
    def store(self, item): 
        """
        A method to adds an item to the container's list_of_item
        """
        self.list_of_items.append(item)
    
    def change_weight(self):
        """
        A method to update the container's total weight and capacity by recalculating based on the items stored
        """
        updated_weight = 0
        for item in self.list_of_items:
            updated_weight += item.weight 
        updated_weight += self.empty_weight
        self.capacity, self.weight = updated_weight - self.empty_weight, updated_weight

    def indent(self, looted_object):
        """
        A method to update the indentation (nesting level) of the container when it is stored inside another container.
        """
        self.indentation = looted_object.indentation + 1 
        for item in self.list_of_items:
            item.indentation = self.indentation + 1  

    def __str__(self):
        """
        Returns a string representation of the container, including its name, total weight, empty weight, and current capacity.
        """
        output = "   " * self.indentation + f"{self.name} (total weight: {self.weight}, empty weight: {self.empty_weight}, capacity: {self.capacity}/{self.weight_capacity})"
        for item in self.list_of_items:
            output = output + f"\n{item}"
        return output

class Multi(Containers):
    """
    Represents a multi compartment container that can store items or any other type of containers
    """
    def __init__(self, name, list_of_compartments):
        """
        A function to initialize the container with the given name and list_of_compartments.
        """
        self.name = name
        self.weight = 0
        self.capacity = 0
        self.weight_capacity = 0
        self.indentation = 0
        self.list_of_items = list_of_compartments
        for item in self.list_of_items:
            self.weight += item.weight
            item.indentation = self.indentation + 1 
        self.empty_weight = self.weight

    def change_weight(self):
        """
        A function updates the container's total weight and capacity by recalculating based on the items stored
        """
        updated_weight = 0
        for item in self.list_of_items:
            updated_weight += item.weight 
        self.weight = updated_weight
    
    def store(self, item):
        """
        A function to store an item inside the container but muted as it is a multi compartment container
        """
        pass
  

class Magic(Containers):
    """
    Represents a magic container that can store items or other containers
    """
    def store(self, item):
        """
        A function to add an item to the container's list_of_item and adjusts its weight and capacity.
        """
        self.list_of_items.append(item)
    
    def change_weight(self):
        """
        A function to update the container's total weight and capacity by recalculating based on the items stored
        """
        updated_weight = 0
        for item in self.list_of_items:
            updated_weight += item.weight 
        self.capacity = updated_weight

class MagicMulti(Multi):
    """
    Representing a magic container with multi compartment that can store items or containers
    """
    def __init__(self, name, list_of_compartments):
        """
        A function to initialise a magic multi container with name and list_of_compartments
        """
        super().__init__(name, list_of_compartments) #inheriting the __init__ function from Multi class
    
    def change_weight(self):
        """
        A function updates the container's total weight and capacity by recalculating based on the items stored but it is not used as the container is a magic multi compartment container
        """
        pass
        
def extract_file(file_name):
    """
    A function to extract each line in file given into lists for each type of containers
    """
    extracted_file = []
    with open(file_name) as file:
        file.readline() # exclude the header
        for row in file:
            line = row.strip().split(',')
            extracted_file.append(line)
        extracted_file.sort() 
    return extracted_file

# lists that store the information for different types of containers and items
item_list = extract_file('items.csv')
container_list = extract_file('containers.csv')
multi_container_list = extract_file('multi_containers.csv')
magic_container_list = extract_file('magic_containers.csv')
magic_multi_container_list = extract_file('magic_multi_containers.csv')


def get_container_names(original_list):
    """
    A function to get the names of the container given and return it in a list
    """
    names_list = []
    for row in original_list:
        names_list.append(row[0])
    names_list.sort()
    return names_list


# lists that contain the names for each of the type of containers
item_names =get_container_names(item_list)
container_names = get_container_names(container_list)
multi_container_names = get_container_names(multi_container_list)
magic_container_names = get_container_names(magic_container_list)
magic_multi_container_names = get_container_names(magic_multi_container_list)

# Update the multi_container_list with the modified multi_container
for multi_container in multi_container_list: 
    compartments = multi_container[1:]
    updated_multi_container = []
    updated_multi_container.append(multi_container[0])
    for compartment in compartments:
        for container in container_list:
            if container[0].strip() == compartment.strip():
                updated_compartment = []
                updated_compartment.append(compartment.strip())
                for row in container[1:]:
                    updated_compartment.append(row.strip())
                
        updated_multi_container.append(updated_compartment)
    indx = multi_container_list.index(multi_container)
    multi_container_list[indx] = updated_multi_container

# Update the magic_container_list with the modified magic_container
for magic_container in magic_container_list: 
    for container in container_list:
        if container[0] == magic_container[1].strip():
            updated_magic_container = []
            updated_magic_container.append(magic_container[0].strip())
            for row in container[1:]:
                updated_magic_container.append(row.strip())
            indx = magic_container_list.index(magic_container)
            magic_container_list[indx] = updated_magic_container

# Update the magic_multi_container_list with the modified magic_multi_container
for magic_multi_container in magic_multi_container_list: 
    for multi_container in multi_container_list:
        if multi_container[0] == magic_multi_container[1].strip():
            updated_magic_multi_container = copy.deepcopy(multi_container)
            updated_magic_multi_container[0] = magic_multi_container[0]
    indx = magic_multi_container_list.index(magic_multi_container)
    magic_multi_container_list[indx] = updated_magic_multi_container


def convert_to_instances(container):
    """
    A function to convert the given container into an instance based on different classes
    """
    if container in container_names: 
        copied_container = copy.deepcopy(container_list[container_names.index(container)])
        chosen_container = Containers(copied_container[0], copied_container[1], copied_container[2])

    elif container in multi_container_names:
        copied_container = copy.deepcopy(multi_container_list[multi_container_names.index(container)])
        compartment_list = []
        for compartment in copied_container[1:]:
            compartment_list.append(Containers(compartment[0], compartment[1], compartment[2]))
        chosen_container = Multi(copied_container[0],compartment_list)

    elif container in magic_container_names:
        copied_container = copy.deepcopy(magic_container_list[magic_container_names.index(container)])
        chosen_container = Magic(copied_container[0], copied_container[1], copied_container[2])

    elif container in magic_multi_container_names: 
        copied_container = copy.deepcopy(magic_multi_container_list[magic_multi_container_names.index(container)])
        compartment_list = []
        for compartment in copied_container[1:]:
            
            compartment_list.append(Containers(compartment[0], compartment[1], compartment[2]))
        chosen_container = MagicMulti(copied_container[0],compartment_list)
    
        
    
    return chosen_container



def find_compartment(input_item, chosen_container):
    """
    A function to find a suitable compartment to store items and different types of containers 
    by recursively looping through compartments and the compartments of looted multi compartment containers
    until a container (a compartment) with sufficient empty capacity is found
    """
    failure_message = f'Failure! Item "{input_item.name}" NOT stored in container "{input_container}".'
    success_message = f'Success! Item "{input_item.name}" stored in container "{input_container}".'
    
    #The main block of code to loot the item. This block is satisfied only when the chosen container is a single normal container 
    #(or a compartment) with sufficient extra capacity
    if  (chosen_container.weight_capacity > 0) and (input_item.weight + chosen_container.capacity) <= chosen_container.weight_capacity: 
        input_item.indent(chosen_container) #increase indentation according to the container it is looted into
        chosen_container.store(input_item)
        chosen_container.change_weight()
        return success_message
        
    #This block of code tests if the chosen container is a multi container
    elif chosen_container.weight_capacity == 0: 
        #if the container is a multi container, check the compartments 
        for compartment in chosen_container.list_of_items:
            if find_compartment(input_item, compartment) == success_message:
                return success_message
        return failure_message
    
    #if the container has one compartment, find from magic aand magic multi container names list
    else:  
        for compartment in chosen_container.list_of_items:
            if compartment.name in (magic_container_names + magic_multi_container_names):
                if find_compartment(input_item, compartment) == success_message:
                    return success_message
            else: 
                continue 
        return failure_message 

if __name__ == '__main__':
    print(f"Initialised {len(item_names + container_names + multi_container_names + magic_container_names + magic_multi_container_names)} items including {len(container_names) + len(multi_container_names) + len(magic_container_names) + len(magic_multi_container_names)} containers.\n")
    
    def find_container():
        """
        A function to prompt the user to input the name of a container and check if it exists.
        """
        global input_container
        input_container = input('Enter the name of the container: ')
        # to check if the input container exists
        if input_container not in (container_names + multi_container_names + magic_container_names + magic_multi_container_names):
            print(f'"{input_container}" not found. Try again.')
            find_container()
        else: # convert the input container into an instance
            global chosen_container
            chosen_container = convert_to_instances(input_container)
            main()

    def main():
        """
        A function to provide the user with a menu to interact with the container system.
        """
        #display the menu for user to choose
        print('==================================')
        print('Enter your choice:')
        print('1. Loot item.')
        print('2. List looted items.')
        print('0. Quit.')
        print('==================================')

        choice = int(input())
        if choice == 1:
            input_item = input('Enter the name of the item: ')
            # check if input item exists
            if input_item not in (item_names + container_names + multi_container_names + magic_container_names + magic_multi_container_names): #check if obj exists first
                print(f'Failure! Item "{input_item}" NOT stored in container "{input_container}".')
            else:
                if input_item in item_names:
                    # create instance for the item
                    item = item_list[item_names.index(input_item)]
                    input_item = Items(item[0], item[1])
                else:
                    # convert the container into instance
                    input_item = convert_to_instances(input_item)
                print(find_compartment(input_item, chosen_container))
                chosen_container.change_weight()
            main()
        elif choice == 2:
            # list looted items
            print(chosen_container)
            main()
        elif choice == 0:
            quit()
        else:
            main()

    find_container()





