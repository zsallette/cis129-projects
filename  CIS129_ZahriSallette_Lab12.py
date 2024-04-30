# CIS 129 Lab
# Zahri Sallette
# Creating a pet class
class Pet:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


def main():
    # Declare input variables
    inputName = ""
    inputType = ""
    inputAge = 0

    # Create a Pet object
    Animal = Pet()

    # Get values for a pet
    print("Enter a pet name:")
    inputName = input()
    Animal.setName(inputName)

    print("Enter a pet type:")
    inputType = input()
    Animal.setType(inputType)

    print("Enter a pet age:")
    inputAge = int(input())
    Animal.setAge(inputAge)

    # Show values for this pet
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())


if __name__ == "__main__":
    main()
