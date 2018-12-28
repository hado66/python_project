# -*- coding: UTF-8 -*-
#!/bin/python
import subprocess
print("请输入您想要的操作代号")
print("a.查看当前的ls")
print("b.代表pwd")
while True:
    # in_put=raw_input("请输入：")
    in_put = input("请输入：")



    class RunCmd(object):
        def cmd_run(self, cmd):
            self.cmd = cmd
            subprocess.call(self.cmd, shell=True)

    #Sample usage
    a = RunCmd()
    if in_put=='a':
            a.cmd_run('ls')
    elif in_put=='b':
            a.cmd_run('pwd')
    elif in_put=="exit":
        break
    # a=raw_input("sdaasgag:")
    print(a)