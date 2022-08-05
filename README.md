# Demonstrating Ojected Oriented Programming (Human)
 
## What is OOP ?


## What Are The Four Key Pillars of OOP:
-  Abstraction
-  Inheritance
-  Encapsulation
-  Polymorphism

### Diagram Showing An Overview of Design
![Planning](https://user-images.githubusercontent.com/97620055/183029584-b7cc7a3a-c54a-4a2a-9421-f79008422f70.png)


### Step 1 Code for displayed for Human Parent Class 
```python
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
```

### Step 2: Code displayed for Male Subclass
``` Python
class Male(Human):  # implement class with parent class

    def __init__(
            self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.title = "Mr"
        self.name = "Maximus"
        self.height = "1.76"
        self.masc_testos = True         #. (attribute) - define as public variables for access.
        self.reproduce = False
        self._ethnicity = "Caucasian"    # _.ethnicity (single underscore) defined as protected information (Encapsulation)
        self.__medical_condition = "ADHD"  #.__medical_condition (double underscore) defined as private information
    def called(self):  # class method returns a concatenated string using variables
        return self.title, "They are addressed as Mr"

    def name(self):  #
        return self.name, "They are addressed as Maximus"

    def produce(self):
        return "It is", self.title, self.name, " that can produce testosterone"

    def pregnancy(self):
        return self.name, "cannot get pregnant"

    def ethnicity(self):
        return self._ethnicity  # function trying to access protected member within class.

male_object = Male()
print(male_object.masc_testos)
print(male_object.ethnicity())
```
### Step 3: Code displayed for Female Subclass

``` Python
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
        return self.__condition # function trying to access private information returns with attribute error.

female_object = Female()
print(female_object.pregnancy())
```
### Step 4: Code displayed for Boy Subclass

``` python
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
```

### Step 5: Code displayed for Girl Subclass

``` Python
from female import Female

class Girl(Female):  # implement class from Female Class

    def __init__(
            self):  # use constructor to initialise attributes, using super() to initialise parent class' attributes as well
        super().__init__()
        self.height = "1.57"  # Re-assigned correct height in girl subclass (Polymorphism)
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

``` 
