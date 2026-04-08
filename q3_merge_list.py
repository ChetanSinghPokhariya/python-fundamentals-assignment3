lst1= list(map(int, input("Enter numbers of list1: ").split(",")))
lst2= list(map(int, input("Enter numbers of list2: ").split(",")))
list3=lst1 + lst2
list3.sort()
print(list3)