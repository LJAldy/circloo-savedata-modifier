original_list = [1, 2, 3]
copied_list = original_list.copy()

# Modify the copied_list
copied_list.append(4)

print(original_list)  # Output: [1, 2, 3]
print(copied_list)   # Output: [1, 2, 3, 4]
