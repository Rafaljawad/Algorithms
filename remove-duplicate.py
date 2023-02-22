#	With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

list_num = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
new_list = []
for i in range(len(list_num)):
    if (list_num.count(list_num[i]) >= 1):
        if list_num[i] not in new_list:
            new_list.append(list_num[i])
    else:
        new_list.append(list_num[i])

print(new_list)