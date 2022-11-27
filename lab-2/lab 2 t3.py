n = int(input())
number = 1
while number <= n:
    if n % number == 0:
        print(number, end=" ")
    number += 1
print()
  #  принтит при условии того что делит без остатка
