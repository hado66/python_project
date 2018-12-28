import  sys,time
# data=open("yesterday",encoding='utf-8').read()
f=open('yesterday','r',encoding='utf-8')   #内存对象 ， （包括文件名，文件的大小，文件的起始位置，）文件句柄， 即为文件对象   --第一步直接打开文件，
print(f.readlines()) #将f的文件中的内容读取出来，变成一个列表。
data=f.read()
print(data)
print('-------------------')
f.close()
'''
f2=open('yesterday2', mode='w',encoding="utf-8")    #往文件中写内容，但在写的过程中，会先创建一个文件
f2.write("sadgasgsagsdagsdgdsg\n")
f2.write("sadgasgsagsdsdafgsagfdsafsdagsagsdgdsg\n")
f2.write("吾问无为谓无无sadgasgdsffsdgfdsafgsgsaaaaaaaaaaaaaaaaaadssagsdagsdgdsg\n")'''

# for index,line in enumerate(data)
f=open('yesterday','r',encoding='utf-8')   #这种方法不常用
for index,line in enumerate(f.readlines()):
    if index==9:
        print("==================")
        continue
    print(line.strip())
f.close()
print('=============++++')
f=open('yesterday','r',encoding='utf-8')
count=0
for line in f:  #一行一行的读，并且内存中只保存一行  #效率最高
    if count==10:
        print('5555%%%%%%%%%%%%%%%%55555')
        count+=1
        continue
    print(line)
    count+=1
f.close()


f=open('yesterday','r',encoding='utf-8')
f.tell()   #找到文件句柄指针所在的位置，
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(0)  #指定文件句柄，回某个位置
print(f.readline())
print(f.tell())
print(f.encoding)
#   f.errors   做异常处理来用的
print(f.fileno())  #python在操作系统中的编号
print(f.name) #打印名字
print(f.isatty())  #与一些终端进行交互、

print(f.flush())  #在内存中，刷到硬盘
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)
print("\n")
f.close()
'''
f=open('yesterday','w',encoding='utf-8')
f.seek(10)
f.truncate(50)   #如果不带参数就是清空   截取  '''
f=open("yesterday",'r+',encoding='utf-8')   #读 --写
print(f.readline())
print(f.tell())
f.write("ddddggasgdag")  #真能追加到最后面