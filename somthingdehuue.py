
class isString():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_string(self):
        print("The string is: ", self.str1.upper())

    def get_length(self):
        return len(self.str1)

str1 = isString()
str1.get_string()
str1.print_string()
print("The length of the string is: ", str1.get_length())