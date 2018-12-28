age=19
#name=input("姓名：")
count=0
i=1
while count<3:
    age_input=int(input("年龄："))
    if age==age_input:
        print("您猜对了！")
        break
    elif age<age_input:
        print("您猜年龄的比实际你年龄大了")
    else:
        print("您猜的年龄比实际年龄小了")
    count+=1
    if count==3:
        continue_confirm=input("do you want to keep gussing ...  Y/N:")
        if continue_confirm=='Y':
            i+=1
            count=0
        elif continue_confirm=='N':
            print("您的" + str(count * i) + "次机会已经用完了")
 #   else:
  #      continue

#else:
  #  print("您的"+str(count)+"次机会已经用完了")
  #"""elif continue_confirm!='Y'or continue_confirm!='N':
  #          print("您的输入有误！")
  #         continue"""