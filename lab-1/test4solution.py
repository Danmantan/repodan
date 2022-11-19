a = int(input())

break_1 = (a // 2) * 5
break_2 = (a - 1) // 2 * 15

minute = 9 * 60 + a * 45 + break_1 + break_2
print(f'{minute//60} {minute%60}')

