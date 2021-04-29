# Alvin, Li

prod_list = [['iphone', 1000], ['ipad', 500], ['airpod', 800], ['book', 80], ['toy', 120]]

salary = input("Input your salary:")
good_cost = 0
cart_list = []
prod_cost =0

if salary.isdigit() and int(salary) > 0:
    while True:
        print("-------Your balance is: %s ----------" %salary)
        print('Total cost is ', good_cost)
        for x, y in enumerate(prod_list):
            print(x, y)

        order_list = input('Which good you want to buy, "q" quite>>>:')

        if order_list.isdigit() and len(prod_list) >= int(order_list) >= 0:
            good_cost += prod_list[int(order_list)][1]
            prod_cost = prod_list[int(order_list)][1]
            salary = int(salary) - int(prod_cost)
            if salary >= 0:
                cart_list.append(prod_list[int(order_list)])
                print("You have order:", cart_list, "\n")
            elif salary < 0:
                print("Your Money is not enough. Please re-order again.")
                break
        elif order_list == "q":
            if int(salary) >= 0 :
                print("Have a nice shopping. You have bought: ", cart_list)
                print("Your balance is: ", salary)
                break
            else:
                print("Type wrong, close shopping")
                print("Your balance is: ", int(salary) + int(good_cost))
                break
        else:
            print("No choose good")
else:
    print("Type wrong, please try again")
