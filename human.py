# Creating parent class with functions - Human Opp Task

class Human:

    # __init is used to declare class attributes
    def __init__(self):  # using __init to declare the class variable on this current parent class.
        self.living = True    # defining the conditions being met which are key to human existence
        self.spine = True
        self.ears = True

    # Creating functions for key human behaviours
    def wakeup(self):
        return " Waking up early morning is good for health."
    def work(self):
        return  "Go to work and earn money to live"
    def sleep(self):
        return "Please get enough sleep as deprived sleep will deteriorate health"

# create an object of the class before using it
cat = Human()

print(cat.sleep()) # we abstracted how was eat created or what info is available.