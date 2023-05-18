# -*- coding: utf-8 -*-
lst1 = [1,2,3,4,5,6]
print(lst1)

tup1 = (1,3,4,6,7,8)
print(tup1)

set1 = {1,2,3,4,5,6}
print(set1)

dict1 = {1:"SHRINIT"}
print(dict1)

list1 = ["Physics", "Chemistry", 1997, 2000]
list2 = [1,2,3,4,5,6]
list3 = ["a","b","c","d"]

print(list1[0:3])
print(list2[4])
print(list3[-3:-1])

print(len(list1))
print(max(list2))
print(min(list2))
print(list1.pop())
list1.append(2033)
print(list1)
list3.reverse()
print(list3)


dict2 = {'a':"Shrinit", 'b':"Sandhan", 'c':"Sagar", 'd':"200"}
print(dict2['a'])