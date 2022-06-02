def arb_args(*args):
    for i in args:
        print(i)

def inner_func(a, b):
    def mult():
        return (a*b)

    def sub():
        return (a-b)

    print(mult() + sub())

def lunch_lady(name, pref):
    if not pref:
        print(name, " has been fed Mystery Meat")
    else:
        print(name, " has been fed ", pref)

def sum_n_product(a, b):
    print((a+b), (a*b))
