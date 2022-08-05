from human import Human
class Female(Human): # implement class with parent class

    def __init__(self): # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.title = "Miss"
        self.name = "Tara"
        self.height = "1.66"
        self.femin_oestro = True
        self.reproduce = True
        self._ethnicity = "Asian"
        self.__condition = "PCOS"

    def called(self): # class method returns a concatenated string using variables
        return self.title, "They are addressed as Miss"
    def name(self): #
        return self.title, "They are addressed as Miss"

    def produce(self):
        return "It is", self.title, self.name, " that can produce oestrogen"
    def pregnancy(self):
        return self.name, "can get pregnant"

    def condition(self):
        return self.__condition # function trying to access private information

female_object = Female()
print(female_object.pregnancy())
