"""
Encapsulation: hiding the change

Access modifiers  
1. Public
2. Protected: '_'
3. Private
"""


# --- Public ---
class Person:
    def __init__(self, id):
        self._id = id


class Student(Person):
    """Student is a derived class from person"""

    school_name = "NTU"  # public class attribute

    def __init__(self, name, id, class_no, age):
        super(Student, self).__init__(id)
        self.name = name
        self._class_no = class_no
        self.__age = age  # protected instance attribute

    def __private_method(self):
        print("This is private method")

    def __str__(self):
        return f"Student {self.name}, ID: {self._id}, Age: {self.__age} y.o, is at class {self._class_no}"


if __name__ == "__main__":
    s1 = Student("Bob", "GM18999M", "10A1", "16")
    print(s1)
    # print(dir(s1))
    # print(help(s1))

    # protected member can be accessed but should not be done due to convention
    print(s1._class_no)
    # private attribute/method still can access outside the class
    # via _object._<class_name>__<private_attribute>
    print(s1._Student__age)
    s1._Student__private_method()
    print(s1.__age)
