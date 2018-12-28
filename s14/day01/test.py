count =0
i=1
for a in range(0,3) :
    continue_confirm = input("do you want to keep gussing ...  Y/N:")
    if continue_confirm == 'Y':
        i += 1
        print("i: " ,i)
        count = 0
    elif continue_confirm=='N':
        print("您的" + str(count * i) + "次机会已经用完了")
    else:
        continue
