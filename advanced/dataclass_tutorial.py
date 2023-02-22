# dataclass
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import List

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


@dataclass
class Product:
    name: str = field(compare=True)  # use for comparison Product's instance
    category: str = field(compare=True)
    shipping_weight: float = field(compare=False)
    unit_price: int = field(compare=False)
    tax_percent: float = field(compare=False)

    def __post_init__(self) -> None:
        if self.unit_price < 0:
            raise ValueError("unit_price attribute must greater then zero.")

        if self.shipping_weight < 0:
            raise ValueError("shipping_weight attribute must greater then zero.")

        if not 0 < self.tax_percent < 1:
            raise ValueError("tax_percent attribute must be between zero and one.")


@dataclass
class Order:
    creation_date: date = date.today()
    products: List[Product] = field(default_factory=list)  # default value is a List

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    @property
    def sub_total(self) -> int:
        return sum((p.unit_price for p in self.products))

    @property
    def tax(self) -> float:
        return sum(
            (product.unit_price * product.tax_percent for product in self.products)
        )

    @property
    def total_price(self) -> float:
        return self.sub_total + self.tax

    @property
    def total_shipping_weight(self) -> float:
        return sum((product.shipping_weight for product in self.products))


def test_product_order_dataclasses() -> None:
    banana = Product(
        name="banana",
        category="fruit",
        shipping_weight=0.5,
        unit_price=215,
        tax_percent=0.07,
    )

    mango = Product(
        name="mango",
        category="fruit",
        shipping_weight=2,
        unit_price=319,
        tax_percent=0.11,
    )
    mango_large = Product(
        name="mango",
        category="fruit",
        shipping_weight=10,
        unit_price=319,
        tax_percent=0.11,
    )

    expensive_mango = Product(
        name="Mango",
        category="Fruit",
        shipping_weight=4.0,
        unit_price=800,
        tax_percent=0.20,
    )

    order = Order()
    for product in [banana, mango, mango_large, expensive_mango]:
        order.add_product(product)

    print(f"Comparison between mango and expensive mango: {mango == expensive_mango}")
    print(f"Comparison between mango and mango large: {mango == mango_large}")
    print(f"Total order price: ${order.total_price/100:.2f}")
    print(f"Subtotal order price: ${order.sub_total/100:.2f}")
    print(f"Value paid in taxes: ${order.tax/100:.2f}")
    print(f"Total weight order: {order.total_shipping_weight} kg")


if __name__ == "__main__":
    student = Person("Quan", "Nguyen", 28, "student")
    doctor = Person("WY", "Peh", 30)
    print(student)
    # print(student < 5)
    print(asdict(student))  # convert to dictionary

    test_product_order_dataclasses()
