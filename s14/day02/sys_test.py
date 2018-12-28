import sys
import  os
import  login  #存在的问题，将其放在当前文件夹下报错，放在 D:\software installation address\python3.5\python\Lib文件路径下就可以正常使用



#print(sys.path) #打印环境变量
#print(sys.argv) #打印文件路径

os_res=os.system("notepad")
print(os_res)  #输出的 0和非零 是代表成功与失败  --执行命令，不保存结果
#os_peon=os.popen("dir").read()  打开文件目录，并读出来
#print("-----",os_peon)
#  os.mkdir("new_dir")  创建文件夹或者文件目录
