my_list=[1,2,3,'apple','banana','grep']

print(my_list[5])
print("length",len(my_list))
my_list.append(4)
print(my_list)
my_list.remove(my_list[3])
print(my_list)
print("list 1 to 3",my_list[1:4])
newList=my_list + my_list[1:4]
print("new concated List",newList)
mylist=[1,5,9,6,4,7,9,3,2,5,8,4,61,8,6,9,5,6,3,1,1,2,4]
print("unsorted list",mylist)
mylist.sort()
print("sorted list:",mylist)
present='banana'in my_list
print("is present element",present)