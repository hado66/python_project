age=19
#name=input("姓名：")
count=0
for i in range(3):   #   可理解为：  for range(0,3,1)
    age_input=int(input("年龄："))
    if age==age_input:
        print("您猜对了！")
        break
    elif age<age_input:
        print("您猜年龄的比实际你年龄大了")
    else:
        print("您猜的年龄比实际年龄小了")
    count+=1
    if  count==3:
        print("您的"+str(count)+"次机会已经用完了")
