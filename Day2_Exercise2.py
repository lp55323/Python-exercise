china = {
    '辽宁省':{
        '大连市':['甘井子区','中山区'],
        '沈阳市':['沈河区','沈北区']
    },
    '吉林省':{
        '长春市':['南关区','九台区'],
        '四平市':['梨树县','双辽县']
    },
    '黑龙江省':{
        '哈尔滨市':['道里区','道外区'],
        '伊春市':['嘉荫县','农场区']
    }
}

while True:
    for i in china:
        print(i)
    shengfen = input('你想去哪个省，e退出游览>>>:')
    if shengfen in china:
        while True:
            for i2 in china[shengfen]:
                print("\t",i2)
            city = input('你想去哪个城市，b返回上一级省份，e退出游览>>:')
            if city in china[shengfen]:
                while True:
                    for i3 in china[shengfen][city]:
                        print(i3)
                    print('到达目的地'.center(15,"-"))
                    goon = input('b返回上一级城市，e退出游览：')
                    if goon == 'b':
                        break
                    elif goon == 'e':
                        exit()
                    else:
                        exit()
            elif city == "b":
                break
            elif city == 'e':
                exit()
    elif shengfen == 'e':
        break

