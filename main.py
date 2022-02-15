"""
Task (2.1): Create a function named drinks that takes an integer n as input and prints:
 "Pepsi" when n is divisible by 2
 "Coke" when n is divisible by 3
 "PepsiCoke" when n is divisible by both
 "PaperBoat" otherwise
Task (2.2): Given a integer list as input. Use drinks function from Task 2.1 that takes each element from the list and prints the name of drinks based on its value.
[5,13,15,20,36]
"""

def drinks(n):
  if n%2==0 and n%3!=0:
    return "Pepsi"
  elif n%3==0 and n%2!=0:
    return "Coke"
  elif n%2==0 and n%3==0:
    return "PepsiCoke"
  else:
    return "PaperBoat"

ls = [5,13,15,20,36]
ln = len(ls)
for i in range(0, ln):
  e = ls[i]
  print(f"{e}: {drinks(e)}")
  