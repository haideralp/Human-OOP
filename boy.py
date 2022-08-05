# Creating boy (base) class whilst inheriting from Male class

from male import Male

class Boy(Male):  # implement class from Male

    def __init__(
            self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.school_name = "Whittmore High School"
        self.fav_food = "chicken dishes"
        self.sports = "football"


    def goeschool(self):  # class method returns a concatenated string using variables
        return self.school_name, " goes to Whittmore High School"

    def eat(self):  #
        return self.fav_food, "likes eating chicken dishes only"

    def plays_sports(self):
        return "It is", self.title, self.name, " that loves playing football"



boy_object = Boy()
print(boy_object.plays_sports())
