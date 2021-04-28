# Alvin, Li

import copy

order_list = [['iphone',1000],['ipad',500],['airpod',800],['book',80],['toy',120]]
order_total = int(len(order_list))
#print(order_total)

total_cost =0
total_order = []

good = False
salary = input("input your salary:")

calc_list = copy.deepcopy(order_list)

while good != "q":
    print("Your balance is "+ salary)
    for a in range(1,2):
        for b in order_list:
            print(a, b)
            calc_list[(a-1)][0] = a
            a += 1
    #print(calc_list)

    if good is False:
        print('Your cart is empty')
    else:
        total_order.append(order_list[int(good)-1])
        print("Your have order: ",total_order )

    good = input("Which one you want to buy? Or press 'q' exit shopping:")
    if good != "q":
        price = calc_list[int(good)-1][1]
        total_cost += price
        #print(total_cost)
    elif good == 'q':
        remain_cost = int(salary) - total_cost
        print("Shopping close")

        if remain_cost >= 0:
            print("Your balance is:",remain_cost,".Have a nice shopping")
        else:
            print("Money is not enough, return goods, close shopping")
        break

    continue


