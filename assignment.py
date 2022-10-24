for num in range (1,31):
    if num%2 == 0:
        print ("FOR Even: " + str(num))

num = 1
while num <= 30:
    if num%2 == 0:
        print ("WHILE Even: " + str(num))
    num += 1


for num in range (1,31):
    if num%2 == 1:
        print ("FOR Odd: " + str(num))

num = 1
while num <= 30:
    if num%2 == 1:
        print ("WHILE Odd: " + str(num))
    num += 1



# ####################################################333
start_amount = 50000
marketing_percentage = 0.25
operations_percentage = 0.5
customeracq_percentage = 0.25
acquisition_cost = 5


marketing_cost = marketing_percentage * start_amount
operations_cost = operations_percentage * start_amount
customer_cost = customeracq_percentage * start_amount
customers_acquired = int(customer_cost/acquisition_cost)

print("FINANCIAL STATEMENT \n" + "COST OF MARKETING: "  +"GHC "+ str(marketing_cost) + "\n" + "COST OF OPERATIONS: " + "GHC "+ str(operations_cost) + "\n" + "CUSTOMER ACQUISITION: " + "GHC "+ str(customer_cost) + "\n" + "CUSTOMERS ACQUIRED: " + str(customers_acquired) + " customers")

