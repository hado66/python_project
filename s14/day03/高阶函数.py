def add(a,b,f):
    return f(a)+b

res =add(-2,3,abs)
print(res)


'''递归的要求'''
#明确的结束条件
#问题规模每递归异常都应该比上一次问题规模有所减少
#执行效率低

#  把一个函数当做实参传给另外一个函数
#返回值中包含函数名