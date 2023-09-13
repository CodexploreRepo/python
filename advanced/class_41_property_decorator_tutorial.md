# `property()` Add Managed Attributes to Your Classes
- **Data Validation**: One of the most common use cases of `property()` is building managed attributes that validate the input data before storing or even accepting it as a secure input.
```Python
  # point.py

class Point:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

pt = Point("none", 2) # -> ValueError: "x" must be a number
pt = Point(12)
# Validated!
pt.x = 4
# Validated!
point.x = "one" # -> ValueError: "x" must be a number

```
- **Providing Computed Attributes**
```Python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```
