def hello():
    print("Greetings, user.")

def pack(a,b,c):
    print(a,b,c)

def eat_lunch(list):
    if not list:
        print("My lunchbox is empty!")
    else:
        for item in list:
            print("I eat ", item)


hello()
pack("Food","Snacks","Tasty")
eat_lunch(["Apple","Sandwich","Capri Sun"])
