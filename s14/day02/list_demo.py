import copy
names=['a',"b",'c','d',"e","f"]
print(names)
print(names[2])
print(names[0],names[2])
print(names[1:4])  #顾头不顾尾 ----- 切片
print(names[-1])  #取出最后一个位置
print(names[-3:-1]) #永远要 --从左往右数
print(names[-3:])  #一直取到最后的一个位置
print(names[0:3])
print(names[:3])  #切片
names.append("G")  #append 追加 到最后
print(names)

names.insert(1,"test") # 定点插入
print(names)

names[1]='test02' #修改
print(names)

# names.remove("test02") # 法一， delete
# print(names)

# del names[1]
# print(names)
# names.pop(1)  #删除
print(names)
names.sort() #排序
print(names)
print(names.index("b")) #索引 --所在位置
names.reverse() #倒叙
print(names)
# names.remove("f")#移除
del names[3] #删除指定位置
print(names)
print("----------")
print(names)
names2=names.copy() # 和names2=name[]一样 ，浅copy，在第一层互相不妨碍

names2.remove("f")
names.append("ddddd")
names2.pop(1)
print(names2)
print(names)

names3=copy.deepcopy(names) #深copy

#元组    和list一样，就是不能修改，功能少
print("----元组------")
names=("j","h","g","c","e","g")
print(names.index("h"))
print(names.index("g"))