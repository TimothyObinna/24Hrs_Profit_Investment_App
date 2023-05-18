

import time
import datetime

investment_amount = 1000 # initial investment amount


while True:
    my_time = datetime.datetime.now()
    profit_amount = investment_amount * 0.1 # Where 0.1 represents 10% 
    investment_amount = investment_amount + profit_amount
    print(f"Daily Investment amount = {investment_amount:.2f}, Profit = {profit_amount:.2f}, {my_time}")
    time.sleep(86400)
