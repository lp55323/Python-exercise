fileopen = open('user.txt',mode='r', encoding=None)
users = fileopen.read()
lockopen = open('lock.txt')
locker = lockopen.read()

print(fileopen.read())

for a in range(1,4):
    user = input("input username:")
    if user not in users:
        print('user not exist, please register')
        break
    elif user in locker:
        print('user is locked')
        break
    password = input("input password:")
    if user == "zhangsan" and password == "123":
        print("Welcome, login success")
        break
    else:
        print('try again, error time:', a)
    a += 1
    if a == 4:
        print(user, "is locked")
        lockuser = open('lock.txt','a')
        lockuser.write('{0}\n'.format(user))
