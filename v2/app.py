print("Calculator")
print("Thanks for using this basic calculator")
first = float(input("First: "))
second = float(input("Second: "))
while True:
    dependor = input("Operator (+, -, *, /): ")
    if dependor in ["+", "-", "*", "/"]:
        break
    else:
        print(f"Hey, the operator you have chose ({dependor}) isn't a valid operator!")
if dependor == "+":
    print("The answer is", first + second)
elif dependor == "-":
    print("The answer is", first - second)
elif dependor == "*":
    print("The answer is", first * second)
elif dependor == "/":
    if second != 0:
        print("The answer is", first / second)
    else:
        print("You have divided by 0, or you have not did a proper sum. Please try again!")
print(f"Sum just for debugging: {first} {dependor} {second}")
