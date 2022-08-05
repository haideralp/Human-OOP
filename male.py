# Creating male (base) class whilst inheriting from human (parent class)
from human import Human


class Male(Human):  # implement class with parent class

    def __init__(
            self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.title = "Mr"
        self.name = "Maximus"
        self.height = "1.76"
        self.masc_testos = True         #. (attribute) - define as public variables for access.
        self.reproduce = False
        self._ethnicity = "Caucasian"    # _.ethnicity (single underscore) defined as protected information
        self.__medical_condition = "ADHD"  #.__medical_condition (double underscore) defined as private information
    def called(self):  # class method returns a concatenated string using variables
        return self.title, "They are addressed as Mr"

    def name(self):  #
        return self.title, "They are addressed as Mr"

    def produce(self):
        return "It is", self.title, self.name, " that can produce testosterone"

    def pregnancy(self):
        return self.name, "cannot get pregnant"


male_object = Male()
print(male_object.masc_testos)
