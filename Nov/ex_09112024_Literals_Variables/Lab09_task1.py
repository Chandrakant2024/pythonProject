# Take a 2 input from the user
# Print the Quotient and Remainder
# 20 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

a = int(input("Enter first number "))
b = int(input("Enter second number "))
Quotient = a/b
Remainder = a%b
print("Quotient is ",int(Quotient))
print("Remainder is ",Remainder)
print(f"Quotient is {Quotient:2f}")
print(f"Remainder {Remainder}")