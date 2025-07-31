nested_list = []
print("Enter 3 sub-lists with 2 numbers each:")
for i in range(3):
    sub_list = []
    for j in range(2):
        value = int(input(f"Enter value {j+1} for sub-list {i+1}: "))
        sub_list.append(value)
    nested_list.append(sub_list)

print("\nNested List:", nested_list)
print("First element of first sub-list:", nested_list[0][0])
length = len(nested_list)
print("Length of Nested List:", length)

list1 = input("\nEnter elements of first list (space separated): ").split()
list2 = input("Enter elements of second list (space separated): ").split()
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

num = int(input("\nEnter a number to check membership in first list: "))
print(f"Is {num} in list1?", num in list1)

print("\nIterating through list1:")
for item in list1:
    print(item)

print("\nElement at index 0 of list1:", list1[0])
print("Element at last index of list2:", list2[-1])
print("\nSlicing list1 from index 1 to 3:", list1[1:4])
print("Slicing list2 last two elements:", list2[-2:])
