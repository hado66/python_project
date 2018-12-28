list_1=[1,2,2,3,4,4,5,6,7,8,8,9]
list_2=[1,2,4,44,466,6,9,6,6,6456464,8855]
print(list_1)
print(set(list_1),type(set(list_1)))   #集合也是无序的

list_1=set( list_1)
list_2=set(list_2)
print('---------------')
print(list_1)
print(list_2)
print(list_1.intersection(list_2))   #intersection  交叉  交集
print('a',list_1 & list_2)

print(list_2.union(list_1))  #union  联合  并集
print(list_2 | list_1)

# 差集
print(list_1.difference(list_2)) #list_1有,而 list_2 中没有
list_3=set([1,2]) # in list 1  but not in  list2

print(list_1 - list_2) #
#子集
print(list_3.issubset(list_2))

#父集
print(list_2.issuperset(list_3))

#对称差集
print(list_1.symmetric_difference(list_2))# 去除同样的

print('-----------------------------------------')
list_3=set([0,1,2])
list_4=set([66,6,6])
print(list_3.isdisjoint(list_4)) #isdisjoint 没有交集