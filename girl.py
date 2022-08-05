# Creating boy (base) class whilst inheriting from Male class

from female import Female

class Girl(Female):  # implement class from Female Class

    def __init__(
            self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.school_name = "Cranford High School"
        self.fav_food = "chinese dishes"
        self.sports = "netball"


    def goeschool(self):  # class method returns a concatenated string using variables
        return self.school_name, " goes to Cranford High School"

    def eat(self):  #
        return "likes eating chinese dishes only"

    def plays_sports(self):
        return "and loves playing netball"



girl_object = Girl()
print(girl_object.plays_sports())