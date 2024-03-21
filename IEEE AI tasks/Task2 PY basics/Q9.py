def comm(set1, set2):
    common_elements = set1.intersection(set2)
    return common_elements
set1 = set(input("Enter elements for set1 separated by space: ").split())
set2 = set(input("Enter elements for set2 separated by space: ").split())
common_elements = comm(set1, set2)
print("Common Elements:", common_elements)
