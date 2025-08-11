present_units = float(input("Enter the present meter reading (units): "))
previous_units = float(input("Enter the previous meter reading (units): "))

units_consumed = present_units - previous_units

rate_per_unit = 5.0

power_bill = units_consumed * rate_per_unit

print(f"Units Consumed: {units_consumed}")
print(f"Power Bill: {power_bill} currency units")

