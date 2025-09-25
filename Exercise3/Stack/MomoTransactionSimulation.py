print("Welcome to simple Momo Transaction Simulation")
transaction = []
print("Enter the payment amount:")
amount = int(input())
print("\n")
transaction.append(amount) 
print ("Enter pin code:")
pin = int(input())
print("\n")
transaction.append(pin)
print("Retype pin code to confirm:")
pin_confirm = int(input())
print("\n")
transaction.append(pin_confirm)
if pin == pin_confirm:
    print("Transaction Successful")
    print(f"Transaction details: {transaction}")
elif pin != pin_confirm:
    print("Transaction Failed. Pin codes do not match.\n")
    print(f"Original transaction details: {transaction}\n")
    transaction.pop()
    print(f"Transaction details: {transaction}\n")
    print("Now the top element in the transaction stack is:", transaction[-1])



