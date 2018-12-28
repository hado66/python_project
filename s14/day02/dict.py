info={
    'a010004101':'hsx',   #字典是无序的
    'a010004102':'hsx02',  #key必须是唯一的，
    'a010004103':'hsx03',




}
print(info)
print(info["a010004101"])#查找
print(info.get("a010004103dd"))#查找
info["a010004101"]='sdfsfsagsagsg' #修改
info["a010004104"]='tanglaoshi'    #创建
b={
    'stu1':"dffr",
    "stu3":"sdagsags"
}
print(info.update(b))

info.update()


print(dict.fromkeys([1,2,3],"test"))#初始化一个字典
del info["a010004103"] #删除
print(info)
info.pop("a010004101") #删除
info.popitem()  #随机删除
print(info)
print("a010004102" in info)