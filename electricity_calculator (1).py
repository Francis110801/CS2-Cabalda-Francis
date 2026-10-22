# Electricity Bill Calculator
RATE = 12.90
while True:
    name = input("Enter customer name: ")

    if name.strip() != "":
        break
    else:
        print("Invalid user please try again")
    
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if 0 <= previous:
        print("Valid Value")
        break
    else:
        print("Invalid Value. Try  again")
while True:
    current = int(input("Enter current meter reading: "))
    
    if 0 <= current:
            print("Valid Value")
            break
    else:
        print("Invalid Value. Try again")


consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
