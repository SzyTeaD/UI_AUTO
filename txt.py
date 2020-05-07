list1 = [1,4,3,5]
list2 = [3,4,5]
list = list1 + list2
list3 = []
for i in list:
    print(i)
    for j in range(len(list)):
        if i<j:
            i = list[j]
            list3.append(i)
            print(list3)