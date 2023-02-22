# 3.	With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
# first way not using intersection method
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
new_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if (list1[i] in list2) and (list1[i] not in new_list):
            new_list.append(list1[i])
print(new_list)


# second-way using intersection method
def intersection_2lists(l1, l2):
    x = set(l1)
    y = set(l2)
    return list(x.intersection(y))

print(intersection_2lists(list1, list2))
