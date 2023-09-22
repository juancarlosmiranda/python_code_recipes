"""





"""

"""
Algorithm
-----------
Input the product amount
Input the client currency
Calculate the rest of money 3.1 euros
Calculate using stock of currency

Test case data
--------------------

Stock in box
---------------
10 coins of 2 euros = 20 euros
4 coins of 0.50 cents = 2 euros
10 coins of 0.20 cents == 2 euros
50 coins of 0.10 cents == 5 euros
29 in stock


Test data
------------
5 euros client
cost of product 1.9

Expected data
--------------
change for client = 3.1
1 coins 2 euros
2 coins 0.50
1 coin 0.10

"""



def calculate_currency(change_input, stock_data_values):
    change_output = 0
    total_ammount_inbox = 10 # todo change this hardcoded data
    # here calculates the number of coins
    # this could be a type of array
    # todo: to complete
    if change_input < total_ammount_inbox:
        pass
        # process transaction


    return change_output


"""
3.1 - 2 = 1.1
1.1 I canot iterate using coin=2, I select the next 1 euro, I chekc that i dont have
And after 0.50

1.1 - 0.5

3.1 MOD 0.5

client_currency DIV coin_050
integet part * value of coin = a_value


3.1/0.5 = 6.1
0.5 * 6 = 3
6 coins of 0.50

3.1 - (3.1/0.5)
3.1 -3 = 0.1  # rest after

0.1 DIV 0.1 = 1
1 coin of 0.1

"""

def calculate_currency_02(change_input):
    change_output = 0
    COIN_010 = 0.1
    COIN_020 = 0.2
    COIN_050 = 0.5
    COIN_1 = 1
    COIN_2 = 2


    result_op_2 = int(change_input / COIN_2)
    temporal_r = change_input - (result_op * COIN_2)

    # if temporal > 1 do
    if temporal_r > COIN_1:
        result_op_1 = int(change_input/COIN_1)
        temporal_r = temporal_r - (result_op * COIN_1)

    # if temporal > 0.1 do
    if temporal_r > COIN_010:
        result_op = int(change_input/COIN_010)
        temporal_r = temporal_r - (result_op  * COIN_010)

    if temporal_r > COIN_020:
        result_op_020 = int(change_input/COIN_020)
        temporal_r = temporal_r - (result_op  * COIN_020)

    if temporal_r > COIN_050:
        result_op_050 = int(change_input/COIN_050)
        temporal_r = temporal_r - (result_op  * COIN_050)

    return change_output

def show_view(stock_data_values):
    """
    Show to the user the type of coins
    :return:
    """

    for a_record in stock_data_values.keys():
        # get key and value in order to show from an array
        print(a_record)
    pass

def get_total_in_box(stock_data_values):
    sum_result = 0
    for a_key in stock_data_values.keys():
        sum_result = sum_result + (stock_data_values.get(a_key) * float(a_key)) # multi
    return sum_result

def main_f():
    print("MAIN")
    # it is an array organised by positions.
    # 0.10 | 0.20 | 0.50 | 1 euro | 2 euros
    stock_data_values_01 = [50, 10, 4, 0, 10] # todo: I am not sre to user this typer of array
    # type of coin | amount in euros
    stock_data_values = {
        "0.10":50,
        "0.20":10,
        "0.50":4,
        "1":0,
        "2":10
    }
    stock_data_multiplier = [0.1, 0.2, 0.5, 1, 2]

    # todo: enable after the user input
    product_prize = float(1.9) #float(input("Enter product prize ="))
    client_currency = float(5) #float(input("Enter client currency ="))

    # todo: case 1 check if client gives more money. In this case continues transaction
    # todo: case 2 check if client gives less money. In this case ask to client about money


    # case 1
    client_change = client_currency - product_prize
    print(f"client_change = {client_change}")
    #stock_in_box = 0 # todo: implement here a funtion to get the total stock

    stock_in_box = get_total_in_box(stock_data_values)
    print(f"stock_in_box = {stock_in_box}")
    calculate_currency_02(client_change)
    #show_view(stock_data_values)

    # todo: the change for client is less than my stock?
    if client_change < stock_in_box:
        # calculate the stock
        # show to the user the final result in type of currency
        pass
    else:
        # todo. to complete this part
        # I have not enought money to give back
        pass

    pass


if __name__ == "__main__":
    main_f()




