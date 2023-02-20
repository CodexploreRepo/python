# dataclass
from dataclasses import asdict, dataclass, field

# frozen=True create objects that are read-only,
# prevent anyone from modifying the values of
# @dataclass(frozen=True)
# class Person:
#     first_name: str
#     last_name: str
#     age: int
#     job: str


@dataclass
class Person:
    """Data Class with default value"""

    first_name: str = "Code"
    last_name: str = "Xplore"
    age: int = 30
    job: str = "Data Scientist"
    # field(init=False): create attribute that is only defined internally,
    # not when the class is instantiated.
    # If we try to access it, an AttributeError is thrown.
    full_name: str = field(init=False, repr=False)

    def __post_init__(self):
        """__post_init__ to perform initialization of attributes that depend on others"""
        self.full_name = self.first_name + " " + self.last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}: {self.age}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.age == other.age
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.age < other.age
        return NotImplemented


if __name__ == "__main__":
    student = Person("Quan", "Nguyen", 28, "student")
    doctor = Person("WY", "Peh", 30)
    print(student)
    print(student < 5)
    print(asdict(student))  # convert to dictionary
