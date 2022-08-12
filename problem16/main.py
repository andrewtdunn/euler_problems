# If the numbers 1 to 5 are written out in words: one, two, three, 
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
# out in words, how many letters would be used?

first_ten = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


output_len = 0

for j in range(0, 10):
    start = ""
    if j > 0:
     start += first_ten[j] + "hundredand"
    # distributed property
    for i in range (0, 100):
        if i == 0:
            output_len += len(start.replace("and",""))
        elif i < 10:
            output_len += len(start + first_ten[i])
        elif i < 20:
            output_len += len(start + teens[i-10])
        else:
            output_len += len(start + tens[i/10] + first_ten[i % 10])

output_len += len("onethousand")


print(output_len)
