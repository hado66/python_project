salary=int(input("please input you salary:"))
list=[
    ["IPhone",5800],
    ["Mac pro",12000],
    ["Starbuck",31],
    ["Alex python",81],
    ["Bile",88],
    ["a",200],
    ["b",300],
    ["c",400]
 ]
account=salary
current_list=[]
while account>0:
    for index,i in enumerate(list) :
        # print(list.index(i)+1,i)
        print(index+1,i)
    print("Your current account :",str(account))
    elect=input("please you elect want buy:")
    if elect>='1' and elect<=str(len(list)):
        elect=int(elect)
        per_price=list[elect-1][1]
        if account-per_price>0:
            current_list.extend(list[elect-1])
            print("------------------------------------------")
            print("you had possession :"+str(current_list))
            account=account-per_price
    elif elect=="q":
        print("you had possession :" + str(current_list))
        break

    else:
         print("您的输入有误")
