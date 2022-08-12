fib_list = [0,0,1,2]

def next_fib():
    fib_list.append(fib_list[len(fib_list)-1] + fib_list[len(fib_list) - 2])

def get_length(num):
    return len(str(num))

index = 3

while len(str(fib_list[len(fib_list) - 1])) < 1000:
    next_fib()
    index += 1

print(index)