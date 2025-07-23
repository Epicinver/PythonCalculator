# Please credit me if you upload this again
# Thanks :)
# By Arran :D
print("Calculator")
first = input("First: ")
second = input("Second: ")
dependor = input("Dependor: ")
if dependor == "+":
  print(float(first) + float(second))
if dependor == "-":
  print(float(first) - float(second))
if dependor == "*":
  print(float(first) * float(second))
if dependor == "/":
  print(float(first) / float(second))
print(f"Sum just for debugging: {first} {dependor} {second}")
