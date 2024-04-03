number1 = int(input("Enter a number for multiplication: "))
number2 = int(input("Enter a range for muliplication: "))
for i in range(1,number2+1):
 mulitply = number1 * i
 print(f"{number1} X {i} = {mulitply}")