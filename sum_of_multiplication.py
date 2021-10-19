"""
Task #1: transform the list to multiply each element on sum of the list
1. find the sum of the list
2. multiply each element on sum of the list
"""
import pandas as p

# Option 1
sample_list = [1, 2, 3, 4, 5, 6]
list_sum = 0
transformed_list = []
for i in range(0, len(sample_list)):
    list_sum = list_sum + sample_list[i]
print(list_sum)

for i in sample_list:
    transformed_list.append(i * list_sum)

print(f"This is option #1 for the transformed list: {transformed_list}")

# Option 2
s = p.Series(sample_list)
new_list = (s * list_sum).tolist()
print(f"\nThis is option #2 for the transformed list: {new_list}. \nIt was created by using pandas package")


# Option 3
def transformed_list():
    list_sum = sum(sample_list)
    transformed_list = []
    for i in sample_list:
        transformed_list.append(i * list_sum)
    print(f"\nThis is option #3 for the transformed list: {transformed_list}")


transformed_list()
