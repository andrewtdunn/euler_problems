print("ok")


factorials = [0, 0, 2, 6]

for i in range(4,101):
    factorials.append(i * factorials[len(factorials) - 1])

last = factorials[-1]
factorial_string = str(last)
last_list = [int(a) for a in factorial_string]
print(sum(last_list))