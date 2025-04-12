# 1. Create an empty list called my_list
my_list = []
print(my_list)

# 2. Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# 3. Insert the value 15 at the second position
my_list.insert(1, 15)
print(my_list)

# 4. Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# 5. Remove the last element from my_list
my_list.pop()
print(my_list)

# 6. Sort my_list in ascending order
my_list.sort()
print(my_list)

# 7. Find and print the index of value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")