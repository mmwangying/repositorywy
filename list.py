#Filename: list.py
#Function: Delete the duplicate value
def deleteDuplicate(list):
    if len(list) == 0:
        return list
    new_list = []
    for value in list:
        if new_list.count(value) == 0:
            new_list.append(value)
    return new_list

print deleteDuplicate([1,1,2,1,3,4,2,4])