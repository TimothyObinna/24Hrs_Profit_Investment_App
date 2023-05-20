
import time
import datetime


investment_amount = 1000 # initial investment amount

print("")
print('Welcome To Cohort_One Investment Station!')
print("")
time.sleep(3)
print("Below are your Running Daily Investment Amounts, Profits And Time Stamps:")

time.sleep(5)




while True:
    my_time = datetime.datetime.now()
    profit_amount = investment_amount * 0.1 # Where 0.1 represents 10% 
    investment_amount = investment_amount + profit_amount
    print(f"Daily Investment amount = {investment_amount:.2f}, Profit = {profit_amount:.2f}, {my_time}")
    time.sleep(86400) #Time delay for each iteration.
