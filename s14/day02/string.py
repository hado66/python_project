name="my name is {name} and i {age} years old"
print(name.count("a"))#统计a的个数
print(name.capitalize())
print(name.center(50,"-"))#打印50个字符
print(name.endswith("uan"))#判断末尾是不是 指定的字符串，返回 true
print(name.expandtabs(90))#将tab键 转化为90个空格
print(name.find("n"))#查找所在位置
print(name.format(name="wangziyuan",age=67))
print(name.format_map({'name':'aaa','age':90}))
print("简答".isalnum())# 是不是包含特殊字符，若包含，则返回 false
print("abd44d".isalpha())#是不是纯字母--返回布尔类型
print("11".isdecimal()) #是不是十进制，若是怎返回 true
print('8451'.isdigit())#判断是不是整数
print("发电房__dfdsf".isidentifier())#判断是不是一个合法的 标识符--或是不是合法的变量名--中文也可以当变量名
# 我的=545
# print(我的)   --在python3中连，中文汉字都可以当变量

print('1451521'.islower())#判断是不是小写
print("-------------")
print("SSDFSGAD".isupper())#判断是不是全 大写
print('444'.isnumeric())#判断是不是数字
print(' '.isspace())#判断是不是空格
print("My Name Is Wwangziyuan".istitle())#判断是不是标题，标题应该为每个首字母大写
print("sdff".isprintable())#判断能不能打印  如：tty file ，drive file
print('^^ '.join(['1','2','3']))
print(name.ljust(50,"*"))# 保证打印的输出长度为50，不够用* 补上
print('   asa   aa\n'.lstrip()) #从左边的空格和回车  strip空格和回车

p=str.maketrans("abcdef",'123456')#加密时使用
print("alex li".translate(p))

print('alex li'.replace('l','L',2)) #替换

print("asfdghhhfd".rfind('h'))#找最右边的值

print('sa dfs af sf'.split(' '))#按空格来分
print('1+2\n+3+4'.splitlines())#识别系统的换行

print('aSdFgHJK'.swapcase())#改变大小写
print('a d  dd  ddd dsda'.title())

print('lex li'.zfill(50))

