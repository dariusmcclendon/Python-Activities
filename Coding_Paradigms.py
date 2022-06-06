# Reflecting on Coding Paradigms 


# Functional Prompt
# Implement a function that wil flatten and sort an array of integers in ascending order
def flat_sort(*args):
    # flatten?
    flat_list = [item for sublist in args for item in sublist]
    # return sorted flat_list
    return sorted(flat_list, key=int)

print(flat_sort([50,24,1,2,3,87,15]))

# Object Oriented Prompt

# Podracer class. Condition needs to be enum? Unsure how to implement.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "Repaired"

# Extends Podracer
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed = self.max_speed * 2

# Extends Podracer 
class SebulbasPod(Podracer):
    def flame_jet(target):
        target.condition = "Trashed"