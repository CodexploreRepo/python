a_list = [1, 2, 3]
b_list = [2, 10]
print(a_list)
print(*a_list)


def product_list(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(product_list(*a_list, *b_list))


# merging_dicts.py
my_first_dict = {"A": 1, "B": 2, "C": 3, "D": 4}
my_second_dict = {
    "country_capital": {"Vietnam": "Ha Noi", "England": "London", "Japan": "Tokyo"},
    "colors": ["red", "white", "blue"],
}
config_dict = {**my_first_dict, **my_second_dict}
print(config_dict)


def demo_func(colors, country_capital, A, B, C, D):
    print("\n")
    print(colors)
    print(country_capital)


demo_func(**config_dict)
