import decorator
# import functools
# # res=filter(lambda n:n>5,range(10))  过滤
# # for i in res:
# #     print(i)
# res =map(lambda n:n*n,range(10))  #对传入的值，进行处理
# for i in res:
#     print(i)
# print("--")
# res =functools.reduce(lambda x,y:x+y,range(10))
# print(res)
# sum,i=0,0
# while i<9:
#     i=i+1
#     sum=sum+i
# print(sum)
print(globals())#获取这个.py文件的全局变量

a=[1,2,3,4,5,6]
b=["a","b","c","d","e"]
for i in zip(a,b):    #zip拉链
    print(i)