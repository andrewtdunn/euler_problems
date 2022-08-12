

print("ok")
#         J   F   M   A   M   J   J   A   S   O   N   D
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# find first of the months

firsts = [1]

for year in range(1901, 2001):
    for days_in_month in months:
        if days_in_month == 28 and year/4 == 0 and  ( year % 100 != 0 or ( year % 100 == 0 and year % 400 == 0)):
            days_in_month += 1
        next_first = firsts[len(firsts) - 1] + days_in_month
        firsts.append(next_first)

print(len(firsts))
# print(firsts[len(firsts) - 1])
firsts.pop()
firsts.pop()
print(len(firsts))
# print(firsts[len(firsts) - 1])

first_sundays = 0
for first in firsts:
    if (first % 7 == 0):
        # print("sunday: %s" % first)
        first_sundays += 1

print("first sundays: %s" % first_sundays)
# print(months)

# print(firsts)


# 1 M
# 2 T
# 3 W
# 4 TH
# 5 F
# 6 SA 
# 7 SUN