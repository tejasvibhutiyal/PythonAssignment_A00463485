"""
@author: Tejasvi Bhutiyal
"""
import re
def stack(our_list, operation, new_element=0):
    """
    Perform 'add' or 'remove' operations on a list to simulate a stack behavior.

    Args:
    our_list (list): The list on which operations are performed.
    operation (str): The operation to perform - 'add' or 'remove'.
    new_element (int, optional): The element to add to the stack. Defaults to 0.

    Returns:
    list: The modified list after performing the stack operation.
    """

    # Compile regex patterns for 'add' and 'remove' operations
    pattern_add = re.compile(r'\b[aA][dD][dD]\b')
    pattern_remove = pattern = re.compile(r'\b[rR][eE][mM][oO][vV][eE]\b')

    # Check for 'add' operation and insert new element
    if(pattern_add.findall(operation)):
        our_list.insert(new_element,0)
        
    # Check for 'remove' operation and pop the first element
    elif(pattern_remove.findall(operation) and len(our_list)>0):
        our_list.pop(0)
    else:
        print("There is no element in stack")
    
    return our_list


def queue(our_list, operation, new_element=0):
    """
    Perform 'add' or 'remove' operations on a list to simulate a queue behavior.

    Args:
    our_list (list): The list on which operations are performed.
    operation (str): The operation to perform - 'add' or 'remove'.
    new_element (int, optional): The element to add to the queue. Defaults to 0.

    Returns:
    list: The modified list after performing the queue operation.
    """

    # Compile regex patterns for 'add' and 'remove' operations
    pattern_add = re.compile(r'\b[aA][dD][dD]\b')
    pattern_remove = pattern = re.compile(r'\b[rR][eE][mM][oO][vV][eE]\b')

    # Check for 'add' operation and insert new element
    if(pattern_add.findall(operation)):
        our_list.append(new_element)

    # Check for 'remove' operation and pop the first element
    elif(pattern_remove.findall(operation) and len(our_list)>0):
        our_list.pop(0)
    else:
        print("There is no element in queue")
    return our_list

new_list= [1,2,3,4]
print("Adding new element to the stack")
new_list = stack(new_list,'add',0)
print(new_list)
print("Remove an element from stack")
new_list = stack(new_list, 'remove')
print(new_list)
print("Adding new element to the queue")
new_list= queue(new_list, 'add', 5)
print(new_list)
print("Removing an element from the queue")
new_list = queue(new_list, 'remove')
print(new_list)



