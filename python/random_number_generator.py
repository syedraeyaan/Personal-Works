import random

int_num1 = int(input("Enter the lower value: "))
int_num2 = int(input("Enter the upper value: "))

print(f"Random number between {int_num1} & {int_num2} = {random.randint(int_num1, int_num2)}")
print(f"Random number between 0 to 1 using random() = {random.random()}")

flo_num1 = float(input("Enter the lower floating value: "))
flo_num2 = float(input("Enter the upper floating value: "))

print(f"Random floating number between {flo_num1} & {flo_num2} = {random.uniform(flo_num1, flo_num2)}")