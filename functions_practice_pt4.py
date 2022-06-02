# Finds the maximum of three numbers
def max_num(a,b,c):
    # sets the largest to a by default
    largest = a
    # if b is larger, set largest to b
    if b > largest :
        largest = b
    # if c is larger, set largest to c
    if c > largest :
        largest = c
    print(largest)
    return largest

# Multiplies all the numbers in a list
def multi_list(*args):
    # sets total to 1
    total = 1
    # for every x in args, multiply by the total 
    for x in args:
        total = x * total
    print(total)
    return total

# Reverses a string
def rev_string(string):
    reverse = string[::-1]
    print(reverse)

# checks whether a number falls in a given range
def num_within(num, start, end):
    for x in range(start, end):
        if x == num :
            print("true")
            return True
    else :
        print("false")
        return False

# Pascal's triangle?
def pascal(n):
    what = "how?"




