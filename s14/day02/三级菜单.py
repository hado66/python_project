info={
    "beijing":{"changping":{},
               "shunyi":"sdfsa",
               "daxing":"dsagafsa"},
    "hebei":{"sjz":{"hebust":"aa",
                     "hebeshida":"bb",
                     "bebeiyikeda":"cc"
                    },
             "hs":{},
             "baoding":{}},
    "guangdong":{"sz":"sdaf",
                 "hz":"aaas",
                 "gz":"sadgdsagdsfgc"}
}
a="changping" in info["beijing"]
print(a)
while True:
    for i in  info:
        print(i)
    choice=input("选择进入1层>>:")
    if choice=='b':
        break
    if choice in info:
        if choice == "b":
            break
        while True:
            for i2 in  info[choice]:
                print("\t",i2)
            choice2 = input("选择进入2层>>:")
            if choice2=='b':
                break
            if choice2 in info[choice]:
                while True:
                    for i3 in info[choice][choice2]:
                        print("\t", i3)
                    choice3=input("选择进入3层>>:")
                    if choice3=='b':
                        break
                    while  True:
                        choice3 = input("选择进入3层>>:")
                        if choice3 == 'b':
                            break
                        if choice3 in info[choice][choice2]:
                            for i4 in info[choice][choice2][choice3]:
                               print(i4)
                            choice4=input("最后一层，按b返回")



